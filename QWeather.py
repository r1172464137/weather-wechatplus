import requests


class QWeather(object):
    def __init__(self, KEY):
        self.KEY = KEY
        self.api_host = 'https://devapi.qweather.com/v7/weather/'

    def request(self, method, url, data=None, params=None, headers=None):
        """发请求"""
        if headers is None:
            headers = {
                'user-agent': 'wasp',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8'
            }

        return requests.request(method, url, data=data, params=params, headers=headers)

    def _get_location(self, city_name):
        api = 'https://geoapi.qweather.com/v2/city/lookup'

        params = {
            'key': self.KEY,
            'location': city_name
        }

        # 仅获取相关度最高的数据
        result = self.request('GET', api, params=params).json()['location'][0]

        return result['name'], result['id']

    def _get_weather_info(self, time, city_name):
        if time in {'3d', '7d', 'now'}:
            api = self.api_host + time

            name, location = self._get_location(city_name)

            params = {
                'location': location,
                'key': self.KEY
            }

            response = self.request('GET', api, params=params).json()

            return response
        else:
            print('不支持的日期类型:', time)

    def get_now_weather(self, city_name):
        return self._get_weather_info('now', city_name)

    def get_3d_weather(self, city_name):
        return self._get_weather_info('3d', city_name)

    def get_7d_weather(self, city_name):
        return self._get_weather_info('7d', city_name)
