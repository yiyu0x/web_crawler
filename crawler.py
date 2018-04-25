#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from yiyu_crawler_lib import dcard_hot,kkbox_daily,yt_hot,beauty_hot,invoice
from lottery import wei_li,big_lottery,colorful_539

function = '功能表 \
0)離開 \
1)dcard熱門 \
2)kkbox日榜 \
3)youtube熱門 \
4)ptt表特 \
5)統一發票兌獎 \
6)台灣彩卷兌獎'

while True:
    option = int(input(function))
    if option==0:
        exit()
    elif option==1:
        print(dcard_hot())
    elif option==2:
        print(kkbox_daily())
    elif option==3:
        print(yt_hot())
    elif option==4:
        print(beauty_hot())
    elif option==5:
        print(invoice())
    elif option==6:
        print("******************************************")
        wei_li()
        big_lottery()
        colorful_539()
