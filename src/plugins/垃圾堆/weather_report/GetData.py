"""
用于获取天气数据
"""
import json
import sys
import time

import requests
import requests.exceptions


class WeatherData(object):

    # 从config.json中获取天气预报api
    @classmethod
    def get_api(cls) -> str:
        try:
            with open('config.json', 'r', encoding='utf-8') as fp:
                cfg = json.load(fp)
                if cfg['weatherAPI'] == 0:
                    print('要在插件中的[config.json]中填写接口地址哟~\n')

        except FileNotFoundError:
            with open('config.json', 'w', encoding='utf-8') as fp:
                _dict = {
                    'weatherAPI': ''
                }
                json.dump(_dict, fp, indent=4, ensure_ascii=False)
                print('要在插件中的[config.json]中填写接口地址哟~\n')
                time.sleep(0.5)
                sys.exit()
        return cfg['weatherAPI']

    # 请求数据
    @classmethod
    def request_data(cls, request_params: dict) -> dict:
        try:
            _data = requests.get(url=cls.get_api(), params=request_params, timeout=6).json()
        except requests.exceptions.MissingSchema:
            print('请在"weatherAPI"中输入正确的地址哦~ >_<')
        except requests.exceptions.ConnectTimeout as t:
            print("Time out!", t.errno)
        except requests.exceptions.HTTPError as h:
            print('HTTP erro!', h.errno)

        return _data




