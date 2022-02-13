import json
from requests import get


url_heybox_search = "https://api.xiaoheihe.cn/game/search/?os_type=web&version=999.0.0&q="

# 小黑盒爬虫
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
    if page['result']['games'][0]['price']['discount']!=0:
        deadline=page['result']['games'][0]['price']['deadline']
    if page['result']['games'][0]['price']['discount'] == 0:


    return

# def heybox_lowest_crawler():
#     return
