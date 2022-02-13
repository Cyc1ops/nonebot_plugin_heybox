from nonebot.params import State, CommandArg
from nonebot import on_command, on_regex, on_keyword
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, GROUP, MessageSegment, Event, Message, GroupMessageEvent
from .heybox_crawler import *

heybox_search = on_command("小黑盒搜", block=True)
heybox_lowest = on_command("小黑盒史低", priority=46, block=True)


@heybox_search.handle()
async def _(bot: Bot, event: GroupMessageEvent, args: Message = CommandArg()):
    game_name = args.extract_plain_text().strip()
    if not args:
        await heybox_search.finish("请输入你要查询的游戏名称捏~")
    else:
        try:
            mes_list = heybox_search_crawler(game_name)
            if len(mes_list) != 1:
                await bot.send(event, "正在搜索并生成合并消息中~", at_sender=True)
                await bot.send_group_forward_msg(group_id=event.group_id, messages=mes_list)
            else:
                await bot.send(event, "无搜索结果")
        except:
            await bot.send(event, "出错了，请检查主机网络情况、查看运行日志")

@heybox_lowest.handle()
async def _(bot: Bot, event: GroupMessageEvent, args: Message = CommandArg()):

    msg = heybox_lowest_crawler()
    await heybox_lowest.finish(msg)