import json
from requests import get
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, GROUP, MessageSegment, Event, Message


url_heybox_search = "https://api.xiaoheihe.cn/game/search/?os_type=web&version=999.0.0&q="

# 小黑盒搜索游戏爬虫
def heybox_search_crawler(game_name):
    url = url_heybox_search + game_name
    response = get(url=url).text
    page = json.loads(response)
    if page['status']!='ok':
        msg="网络异常"
        return msg
    if page['result']['games']==None:
        msg="查询不到有叫这个名字的游戏哦~"
        return msg
    game=page['result']['games'][0]['name']
    initial_price=page['result']['games'][0]['price']['initial']
    current_price=page['result']['games'][0]['price']['current']
    lowest_price=page['result']['games'][0]['price']['lowest_price_raw']
    discount=str(page['result']['games'][0]['price']['discount'])
    game_pic=page['result']['games'][0]['image']
    if page['result']['games'][0]['price']['discount'] == 0:
        msg = f"【游戏名】:{game}\n"+MessageSegment.image(game_pic)+f"\n现在 {game} 是原价哦\n"
        msg = msg + f"【原价】:{initial_price}\n" +f"【当前】:{current_price}"+f"【史低】:{lowest_price}"
    elif page['result']['games'][0]['price']['is_lowest'] == 0:
        deadline = page['result']['games'][0]['price']['deadline']
        msg = f"【游戏名】:{game}\n" + MessageSegment.image(game_pic) + f"\n现在 {game} 的折扣是-{discount}%,还不是史低哦\n"
        msg = msg + f"【原价】:{initial_price}\n" +f"【当前】:{current_price}\n"+f"【史低】:{lowest_price}\n"
        msg = msg + f"本次折扣还{deadline}"
    elif page['result']['games'][0]['price']['is_lowest'] == 1 and page['result']['games'][0]['price']['new_lowest'] == 0:
        deadline = page['result']['games'][0]['price']['deadline']
        msg = f"【游戏名】:{game}\n" + MessageSegment.image(game_pic) + f"\n现在 {game} 的折扣是-{discount}%,是史低哦!!!\n"
        msg = msg + f"【原价】:{initial_price}\n" + f"【当前】:{current_price}\n" + f"【史低】:{lowest_price}\n"
        msg = msg + f"本次折扣还{deadline}"
    elif page['result']['games'][0]['price']['is_lowest'] == 1 and page['result']['games'][0]['price']['new_lowest'] == 1:
        deadline = page['result']['games'][0]['price']['deadline']
        msg = f"【游戏名】:{game}\n" + MessageSegment.image(game_pic) + f"\n现在 {game} 的折扣是-{discount}%,是新史低!!!快买买买!!!\n"
        msg = msg + f"【原价】:{initial_price}\n" + f"【当前】:{current_price}\n" + f"【史低】:{lowest_price}\n"
        msg = msg + f"本次折扣还{deadline}"
    return msg

    return

def heybox_lowest_crawler():
    return