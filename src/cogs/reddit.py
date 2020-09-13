import requests
import sys
import os
from dotenv import load_dotenv

# Steps to get reddit api connection
load_dotenv()
username = os.getenv('REDDIT_USERNAME')
password = os.getenv('REDDIT_PASSWORD')
appName = os.getenv('REDDIT_APPNAME')
appId = os.getenv('REDDIT_APPID')
appSecret = os.getenv('REDDIT_APPSECRET')

base_url = 'https://www.reddit.com/'
data = {'grant_type': 'password', 'username': username, 'password': password}
auth = requests.auth.HTTPBasicAuth(appId, appSecret)

r = requests.post(base_url + 'api/v1/access_token',
                  data=data,
                  headers={'user-agent': appName},
		  auth=auth)
d = r.json()

token = 'bearer ' + d['access_token']

base_url = 'https://oauth.reddit.com'

headers = {'Authorization': token, 'User-Agent': 'discordBot'}
response = requests.get(base_url + '/api/v1/me', headers=headers)

if response.status_code != 200:
    print("Error, api expirated")
    sys.exit()

payload = {'q': 'mexico', 'limit': 5, 'sort': 'relevance'}
response = requests.get(base_url + '/subreddits/search', headers=headers, params=payload)
values = response.json()
for i in range(len(values['data']['children'])):
    print(values['data']['children'][i]['data']['display_name'])
