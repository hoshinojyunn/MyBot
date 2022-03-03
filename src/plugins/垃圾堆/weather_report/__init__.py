"""
简易天气查询插件
查询当日天气情况

"""

from GetData import WeatherData
from nonebot.plugin import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.mirai import Bot, MessageEvent

# weather_keyword = on_keyword({"天气", "会不会下雨"}, rule=to_me(), priority=3)

# 命令触发
weather_cmd = on_command(("天气", "tianqi"), rule=to_me())


@weather_cmd.handle()
async def hanle_first_receive(bot: Bot, event: MessageEvent, state: T_State):
    args = str(event.get_message()).strip()  # 获取命令跟随的参数
    if args:
        state["city"] = args
    await bot.send(event, get_weather(args), at_sender=True)


def get_weather(cityid: str = '', city: str = '', ip: str = ''):
    city_data = WeatherData().request_data({'cityid': cityid, 'city': city, 'ip': ip})
    return f"{city_data['city']}的天气是{city_data['wea']}!\n更新时间:{city_data['update_time']}"
