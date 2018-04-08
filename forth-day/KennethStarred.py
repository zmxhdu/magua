# coding = utf-8

import requests
import webbrowser
import time


api = 'https://api.github.com/users/kennethreitz/starred'
info = requests.get(api).json()
starred = []

for i in info:
    starred.append(i['id'])

while True:
    info = requests.get(api).json()
    for i in info:
        if not i['id'] in starred:
            starred.append(i['id'])
            web_page = i['html_url']
            webbrowser.open(web_page)
    time.sleep(600)
