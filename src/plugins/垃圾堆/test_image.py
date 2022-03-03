from nonebot.adapters.mirai import Bot, MessageEvent, message
from nonebot.plugin import on_keyword
from nonebot.rule import to_me

test_image = on_keyword(keywords={'tu'}, rule=to_me())

native_image = message.MessageSegment.image(
    # path='D:\\PycharmProjects\\NoneBot\\testNonebot_Mirai\\src\\plugins\\interlude_partner.png') # 失效
    # path='../../../../src/plugins/82671621_p13.jpg') # 有效
    url="https://i1.hdslb.com/bfs/archive/8b8a4fcda908bfe295be57819b10585c04c0c3bc.jpg@412w_232h_1c.jpg")  # 有效


@test_image.handle()
async def send_pic(bot: Bot, event: MessageEvent):
    await bot.send(event, message=())
