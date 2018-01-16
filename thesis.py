# -*- coding: utf-8 -*-

import pygal

line_chart = pygal.Line()
line_chart.title = u'包层直径数据'
line_chart.x_labels = [u'第一类测量', u'第二类测量', u'第三类测量', u'第四类测量', u'第五类', u'第六类']
line_chart.add(u'第一次', [125.12, 125.22, 125.03, 124.93, 124.84, 124.97])
line_chart.add(u'第二次', [125.07, 125.24, 125.07, 124.76, 124.94, 124.92])
line_chart.add(u'第三次', [125.08, 125.23, 124.93, 125.03, 124.81, 125.03])
line_chart.add(u'平均', [125.09, 125.23, 125.01, 124.91, 124.86, 124.97])
line_chart.add(u'富通', [125.15, 125.83, 124.88, 124.68, 124.53, 124.83])
line_chart.render_to_file('thesis.svg')
