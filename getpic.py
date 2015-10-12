# -*- coding: cp936 -*-
#coding = utf-8
import re
import urllib

url_part1 = "http://tieba.baidu.com/p/3641827184"
url = "http://tieba.baidu.com/p/3641827184"

picnum = 0

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
def getImg(html):
    global picnum
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre =re.compile(reg)
    imglist = re.findall(imgre,html)
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg' % picnum)
        picnum+=1
    return picnum
def getPageNum(html):
    #<a href="/p/3215166874?pn=4340">尾页</a>
    reg = r'<a href="\/p\/.+=(\d+)">.+</a>'
    pagere =re.compile(reg)
    pagelist = re.findall(pagere,html)
    return pagelist

html = getHtml(url)

getImg(html)
pagelist = getPageNum(html)
list_a = map(eval, pagelist)
maxpage = max(list_a)
for ipage in range(1,maxpage+1):
    url_part2 = "?pn=%d"%ipage
    url_item = url_part1 + url_part2
    print url_item
    html = getHtml(url_item)
    print getImg(html)

