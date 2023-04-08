import os
import random

from nonebot import on_command, on_keyword
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from nonebot.adapters.onebot.v11.permission import GROUP
from nonebot.rule import to_me

from configs.config import NICKNAME
from configs.path_config import IMAGE_PATH
from utils.message_builder import image
from utils.utils import FreqLimiter

__zx_plugin_name__ = "基本设置 [Hidden]"
__plugin_usage__ = "用法： 无"
__plugin_version__ = 0.1
__plugin_author__ = "HibiKier"


_flmt = FreqLimiter(300)

my_wife = on_keyword({"老婆"}, rule=to_me(), priority=5, block=True)


@my_wife.handle()
async def _():
    await my_wife.finish(image(IMAGE_PATH / "other" / "laopo.jpg"))
