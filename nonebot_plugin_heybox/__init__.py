from nonebot.params import State, CommandArg
from nonebot import on_command, on_regex, on_keyword
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, GROUP, MessageSegment, Event, Message, GroupMessageEvent
from .heybox_crawler import *

heybox_search = on_command("小黑盒搜",aliases={"查游戏","查史低"}, priority=46, block=True)
heybox_lowest = on_command("小黑盒史低", priority=46, block=True)


@heybox_search.handle()
async def _(bot: Bot, event: GroupMessageEvent, args: Message = CommandArg()):
    game_name = args.extract_plain_text().strip()
    if not game_name:
        await heybox_search.finish("请输入你要查询的游戏名称捏~")
    else:
        result = heybox_search_crawler(game_name)
        await heybox_search.finish(result)


# @heybox_lowest.handle()
# async def _(bot: Bot, event: GroupMessageEvent, args: Message = CommandArg()):
#
#     msg = heybox_lowest_crawler()
#     await heybox_lowest.finish(msg)