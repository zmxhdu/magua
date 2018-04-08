# coding = utf-8

import requests

repo_url = 'https://api.github.com/search/repositories?q='


def get_project(language, size, last_week):
    url = repo_url + 'language:' + language + '+size:' + size + '+created:' + last_week
    info = requests.get(url).json()['items']
    for i in info:
        print(i['html_url'])


get_project('python', '<200', '>2018-04-01T00:00:00Z')
