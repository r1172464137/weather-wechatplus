import requests

def send_msg_to_qq_group(content):
    group_api = 'https://red-bar-1d38.coupile1.workers.dev'
    title = "昆山天气"
    url= 'https://www.qweather.com/'
    params={
        'title':title,
        'description':content,
        'url':url
    }

    return requests.get(group_api, params=params).json()
    print(response)

