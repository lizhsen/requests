# -*- coding: utf-8 -*-

import requests
import json
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print (r.status_code)
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print ("Repositories returned:", len(repo_dicts))

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict={
        'value':repo_dict['stargazers_count'],
        'xlink':repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)

# 可视化
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend= False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
# 研究第一个仓库
repo_dict = repo_dicts[0]
print ("\nSelected information about first repository")