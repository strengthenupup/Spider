import requests
from bs4 import BeautifulSoup
import bs4
import pymysql
def downloadpage():
    #爬取的URL
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2016.html'
    #定义个请求头
    myHeader = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    #连接mysql数据库
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='spider', charset='utf8')
    cursor = conn.cursor()
    ulist = []
    #发送请求
    r = requests.get(url,headers=myHeader)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    html = r.text
    #获取内容解析
    soup = BeautifulSoup(html, "html.parser")
    #遍历存入数据库
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string,tds[3].string])
    try:
        for i in range(ulist.__len__()):

            u = ulist[i]
            sql = "insert into cmdb_message(ulevel,uname,uaddr,ugrade) values('%s','%s','%s',%s)"%(u[0],u[1],u[2],u[3])
            cursor.execute(sql)
            conn.commit()
    except Exception as e:
        print(e)
    conn.commit()
    cursor.close()
    conn.close()

