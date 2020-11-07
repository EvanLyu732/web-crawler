import urllib2
import re
import time

#get html by url
def getHTML(url):
    page=urllib2.urlopen(url)
    html=page.read()
    return html

#get url paried with html
def getImg(html):
    reg=r'src="(http://.+?\.jpg)"'
    imgre=re.compile(reg)
    imglist=re.findall(imgre,html)
    i=0
    for imgurl in imglist:
        print imgurl
        urllib.urlretreieve(imgurl,'%s.jpg'%time.time())
        i+=1
    url="https://www.bbc.com/news/uk-england-stoke-staffordshire-52047832"
    html=getHTML(url)
    print getImg(htmL)

