from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import re
import random

def yt_hot():
    chrome_options = Options()

    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument('--headless') # 不提供可視化界面
    chrome_options.add_argument('--disable-gpu') # 規避 bug 
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument('blink-settings=imagesEnabled=false') # 不加載圖片
    
    chrome = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
    
    chrome.get("https://www.youtube.com/feed/trending")
    soup = BeautifulSoup(chrome.page_source,'html.parser')
    yt_target = 5
    yt_hot = ''
    yt_counter = 0
    # https://www.youtube.com/watch?v=UoSxTDOp6mY
    for a_tag in soup.find_all('a', {'id': 'video-title'}):
        if a_tag:
            yt_counter += 1
            tmp = a_tag['aria-label'].split()
            yt_hot += '🌟' + a_tag.getText() 
            for context in tmp:
                if '上傳者' in context:
                    yt_hot += context.replace('上傳者：','') + '\n'
            yt_hot += 'https://youtube.com' + a_tag['href']
            yt_hot += '\n --- \n'
            if yt_counter == yt_target:
                break
    yt_hot = yt_hot[:len(yt_hot)-1]
    return yt_hot
def dcard_hot():

    res = requests.get("https://www.dcard.tw/f")
    soup = BeautifulSoup(res.text,'html.parser')
    url_dcard = []
    title_dcard = []
    counter_h3 = 0
    counter_hot = 0
    target = 5
    final_dcard_data = ''

    for img in soup.select('a'):

        pattern = re.compile(r'.*href="(/f/.*?/p/\d{9})-(.*?)"')
        match = pattern.search(str(img))
        if pattern.match(str(img)):
            counter_hot += 1
            # print(match.group(1),match.group(2))
            title_dcard.append(match.group(2))
            url_dcard.append('https://www.dcard.tw/'+str(match.group(1)))
            if counter_hot == target:
                break

    # test data --> https://www.dcard.tw /f/funny/p/227134670-朋友的朋友的限時 "> 
    for i in range(target):
        final_dcard_data += (title_dcard[i]+' '+url_dcard[i]+'\n')
    final_dcard_data = final_dcard_data[:len(final_dcard_data)-1]
    return final_dcard_data

def kkbox_daily():

    kkbox_daily_top = []
    res = requests.get("https://www.kkbox.com/tw/tc/rss/charts-chinese-daily.xml")
    soup = BeautifulSoup(res.text,'html.parser')
    target = 4
    kkbox_daily_top_string = ''
    for index,text in enumerate(soup.find_all('description')):
        if index==1:
            # print(text)
            # pattern = re.compile(r'.*nbsp;')
            # match = pattern.search(str(text))
            match = re.search(r'.*nbsp;(.*?/.*?/.*?)&lt',str(text))
            if match:
                # print(match.group(1))
                kkbox_daily_top.append(' '+str(match.group(1)))

            # findall 匹配多項
            match2 = re.findall(r'.*&gt;(.*?/.*?/.*?)&lt',str(text))
            # if match2:
                # print(match2)

    for i in range(target):
        kkbox_daily_top.append(match2[i])

    for i in kkbox_daily_top:
        kkbox_daily_top_string += '🌟' + i + '\n'

    kkbox_daily_top_string = kkbox_daily_top_string[:len(kkbox_daily_top_string)-1]
    return kkbox_daily_top_string

# print(kkbox_daily())
def beauty_hot():
    random_page = random.randint(2250,2264)
    # print(random_page)

    # https://webptt.com/m.aspx?n=bbs/Beauty/index2264.html
    # print("程式進入")
    res = requests.get("https://webptt.com/m.aspx?n=bbs/Beauty/index"+str(random_page)+'.html')
    soup = BeautifulSoup(res.text,'html.parser')

    beauty_gril_article = []
    beauty_gril_url = []
    # <a href="./m.aspx?n=bbs/Beauty/M.1504596296.A.331.html">[正妹] 台北雙層巴士</a>
    # print("執行第一迴圈")
    for a_tag in soup.select('a'):
        # print(a_tag)
        match = re.search(r'.*href="\./m\.aspx\?n=bbs/Beauty/M(.*?)">\[正妹\]',str(a_tag))
        if match:
            # print(match.group(1))
            beauty_gril_article.append('https://webptt.com/m.aspx?n=bbs/Beauty/M'+match.group(1))
            # https://webptt.com/m.aspx?n=bbs/Beauty/M.1504590665.A.10B.html

    # print(beauty_gril_article)

    # for url in beauty_gril_article:

    while True:
        res = requests.get(beauty_gril_article[(random.randint(0,len(beauty_gril_article)-1))])
        soup = BeautifulSoup(res.text,'html.parser')

        # beauty_target = 5
        # beauty_counter = 0
        # print("執行第二迴圈")
        for a_tag in soup.select('a'):
            # print(div_tag)
            match_img = re.findall(r'href="(http.*?.jpg)"',str(a_tag))
            if match_img:
                # beauty_counter += 1
                beauty_gril_url.append(match_img)
                # print(match_img)
                # if beauty_counter == beauty_target:
                #     break
                # break
        if len(beauty_gril_url)!=0:
            break


    # print(len(beauty_gril_url)-1)
    random_range = random.randint(0,len(beauty_gril_url)-1)
    final_url = ''.join(beauty_gril_url[random_range])
    # print(final_url)
    if final_url[4]!='s':
        final_url = final_url.replace('http', 'https')
    
    return final_url
def invoice():

    res = requests.get("https://bluezz.com.tw")
    soup = BeautifulSoup(res.text,'html.parser')    

    for img in soup.select('img'):
        match = re.search(r'<img alt=.*(https:.*\.jpg)',str(img))
        if match:
            # print(match.group(1))
            return str(match.group(1))
