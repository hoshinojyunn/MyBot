import requests
from nonebot.plugin import on_command
from nonebot.rule import to_me
from nonebot.adapters.mirai import Bot, MessageEvent

api = 'https://www.tianqiapi.com/free/day?appid=66413191&appsecret=EUY3M6Ea'


def request_data(request_params: dict) -> dict:
    try:
        _data = requests.get(url=api, params=request_params, timeout=6).json()
    except requests.exceptions.ConnectTimeout as t:
        print("Time out!", t.errno)
    except requests.exceptions.HTTPError as h:
        print('HTTP erro!', h.errno)

    return _data


def get_data(city='', cityid='', ip=''):
    city_data = request_data({
        'cityid': cityid,
        'city': city,
        'ip': ip
    })
    return f"\n{city_data['city']}的天气是 {city_data['wea']}!\n" \
           f"空气质量:{city_data['air']} ~\n" \
           f"实时温度是 {city_data['tem']}℃ 哟~\n" \
           f"(白天温度: {city_data['tem_day']}℃; 夜间温度: {city_data['tem_night']}℃)\n" \
           f"风向:{city_data['win']} 风速:{city_data['win_speed']},{city_data['win_meter']}\n" \
           f""f"[最近一次更新时间:{city_data['update_time']}]"


weather_cmd = on_command(cmd="天气", rule=to_me())


@weather_cmd.handle()
async def w(bot: Bot, event: MessageEvent):
    args = event.get_plaintext()
    await bot.send(event, get_data(args), at_sender=True)
