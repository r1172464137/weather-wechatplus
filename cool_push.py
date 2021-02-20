import requests

def send_msg_to_qq_group(content):
    group_api = 'https://**.workers.dev'  #填你自己的workers链接
    title = "天气推送"
    url= 'https://www.qweather.com/'
    params={
        'title':title,
        'description':content,
        'url':url
    }

    return requests.get(group_api, params=params).json()
    print(response)

