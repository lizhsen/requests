# -*- coding: utf-8 -*-

import requests
import json

url = 'https://api.github.com/search/repositories?q=langue:python&sort=stars'
r = requests.get(url)
print (r.status_code)
response_dict = r.json()
print str(response_dict)
