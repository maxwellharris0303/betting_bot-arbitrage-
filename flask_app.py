from flask import Flask, request, jsonify
from flask_cors import CORS
import main
from selenium import webdriver


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

firefox_profile_directory = 'C:/Users/Administrator/AppData/Roaming/Mozilla/Firefox/Profiles/yr5ttek5.default-release'
firefox_options = webdriver.FirefoxOptions()
firefox_options.profile = webdriver.FirefoxProfile(firefox_profile_directory)

driver = webdriver.Firefox(options=firefox_options)
driver.maximize_window()

@app.route('/scrape/middles')
def scrape_middles():
    return main.start_bot("https://oddsjam.com/betting-tools/middles", driver)

@app.route('/scrape/lowhold')
def scrape_lowhold():
    return main.start_bot("https://oddsjam.com/betting-tools/low-hold", driver)

@app.route('/scrape/arbitrage', methods=['GET'])
def scrape_arbitrage():
    return main.start_bot("https://oddsjam.com/betting-tools/arbitrage", driver)



if __name__ == '__main__':
    # app.run(debug=True, port=80)
    app.run(host='0.0.0.0', port=80)
