# -*- coding: utf-8 -*-

import requests
import json

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print (r.status_code)
response_dict = r.json()
print("Total repositories:",response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print ("Repositories returned:", len(repo_dicts))

# 研究第一个仓库
repo_dict = repo_dicts[0]
print("\nKeys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print key
