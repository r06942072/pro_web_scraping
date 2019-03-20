import requests
import webbrowser
par = {"wd": "莫烦Python"}  # 搜索的信息
r = requests.get('http://www.baidu.com/s', params=par)  #combine to one url
print(r.url)
webbrowser.open(r.url)

# http://www.baidu.com/s?wd=%E8%8E%AB%E7%83%A6Python
