from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from time import sleep
import json



def start_bot(url, driver):
    driver.get(url)

    WebDriverWait(driver, 20).until(
        lambda driver: driver.execute_script("return document.readyState") == "complete"
    )


    def scroll_down(driver):
        page_height = driver.execute_script("return document.body.scrollHeight")
        scroll_distance = page_height // 5
        
        for i in range(1, 6):
            driver.execute_script(f"window.scrollTo(0, {scroll_distance * i});")
            sleep(1)

    count = 0
    while(count == 0):
        table_rows = driver.find_elements(By.ID, "betting-tool-table-row")
        count = len(table_rows)
        # print(count)

    scroll_down_count = 2
    for _ in range(scroll_down_count):
        scroll_down(driver)

    data = {}

    for index in range(count):
        table_rows = driver.find_elements(By.ID, "betting-tool-table-row")
        
        percent_profit = table_rows[index].find_element(By.ID, "percent-cell").text
        # print(percent_profit)
        event_time = table_rows[index].find_element(By.CSS_SELECTOR, "div[data-testid=\"event-cell\"]").text
        # print(event_time)
        event_teams = table_rows[index].find_element(By.CSS_SELECTOR, "p[class=\"text-sm text-inherit __className_e5b66b w-fit font-semibold\"]").text
        # print(event_teams)
        event_type = table_rows[index].find_element(By.CSS_SELECTOR, "p[class=\"text-sm text-inherit __className_e5b66b w-fit\"]").text
        # print(event_type)
        bet_type = table_rows[index].find_element(By.CSS_SELECTOR, "p[class=\"text-sm __className_e5b66b text-brand-purple\"]").text
        # print(bet_type)
        bet_names = table_rows[index].find_elements(By.CSS_SELECTOR, "p[class=\"text-sm text-inherit __className_e5b66b flex-1\"]")
        # print(bet_names[0].text)
        # print(bet_names[1].text)
        bet_odds = table_rows[index].find_elements(By.CSS_SELECTOR, "p[class=\"text-sm text-inherit __className_e5b66b font-bold\"]")
        # print(bet_odds[0].text)
        # print(bet_odds[1].text)
        try:
            bet_sizes = table_rows[index].find_elements(By.TAG_NAME, "input")
            # print(bet_sizes[0].get_attribute('value'))
            # print(bet_sizes[1].get_attribute('value'))
            profit = table_rows[index].find_element(By.CSS_SELECTOR, "div[class=\"tour__profit flex flex-col items-center justify-center gap-y-2\"]").text
            # print(profit)
        except:
            pass
        
        key = f"{bet_names[0].text} {bet_odds[0].text}"
        if url == "https://oddsjam.com/betting-tools/arbitrage":
            data[key] = {
                "team1": {
                    "percent_profit": percent_profit,
                    "event_time": event_time,
                    "event_teams": event_teams,
                    "event_type": event_type,
                    "bet_type": bet_type,
                    "bet_name": bet_names[0].text,
                    "bet_odds": bet_odds[0].text,
                    "bet_size": bet_sizes[0].get_attribute('value'),
                    "profit": profit
                },
                "team2": {
                    "percent_profit": percent_profit,
                    "event_time": event_time,
                    "event_teams": event_teams,
                    "event_type": event_type,
                    "bet_type": bet_type,
                    "bet_name": bet_names[1].text,
                    "bet_odds": bet_odds[1].text,
                    "bet_size": bet_sizes[1].get_attribute('value'),
                    "profit": profit
                },
            }
        else:
            data[key] = {
                "team1": {
                    "percent_profit": percent_profit,
                    "event_time": event_time,
                    "event_teams": event_teams,
                    "event_type": event_type,
                    "bet_type": bet_type,
                    "bet_name": bet_names[0].text,
                    "bet_odds": bet_odds[0].text,
                },
                "team2": {
                    "percent_profit": percent_profit,
                    "event_time": event_time,
                    "event_teams": event_teams,
                    "event_type": event_type,
                    "bet_type": bet_type,
                    "bet_name": bet_names[1].text,
                    "bet_odds": bet_odds[1].text,
                },
            }

    json_data = json.dumps(data, indent=4)
    print(json_data)
    return data   
