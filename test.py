import requests

response = requests.get(
  url='https://proxy.scrapeops.io/v1/',
  params={
      'api_key': '075ac258-07b8-4a01-ab3f-e1a504a76e6e',
      'url': 'https://hermes.com/', ## DataDome protected website 
      'bypass': 'datadome',
  },
)

print('Body: ', response.content)