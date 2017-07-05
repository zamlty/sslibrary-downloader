# -*- coding: utf-8 -*-

import os
import re
import requests
from threading import Thread
import time


def download(fname, jpgUrl):
    p = requests.get(jpgUrl)
    with open(fname, 'wb') as f:
        f.write(p.content)


# Modify here
url = 'http://img.sslibrary.com/n/slib/book/slib/11647684/4fae1823b856407795c25ba7a8af7432/4bd18516cf404e663f8d36e2f949ec43.shtml?dxbaoku=true'
path = r'D:\Downloads\doc\njulibpdf'
#path = os.path.abspath('.')
threads = 5
# End

text = requests.get(url).text
title = re.findall(r'<title>([\s\S]+)</title>', text)[0]
page = re.findall((r'\[\[1, 0\], \[1, (\d+)\], \[1, (\d+)\], \[1, (\d+)\], \['
                   r'1, (\d+)\], \[1, (\d+)\], \[1, 0\], \[2, 2\]\]'), text)[0]
page = list(map(int, page))
jpgPath = 'http://img.sslibrary.com' + re.findall(r'jpgPath: "(\S+)"', text)[0]

directory = os.path.join(path, title)
if not os.path.exists(directory):
    os.mkdir(directory)

num = sum(page) + 2
print(title)
print(num, 'pages')

head = ['bok', 'leg', 'fow', '!00', '000']
jpgList = []
for i, j in zip([1, 2], [1, num]):
    fname = os.path.join(path, title, '%03d.jpg' % j)
    if not os.path.exists(fname):
        jpgUrl = jpgPath + 'cov%03d' % i
        jpgList.append([fname, jpgUrl])

num = 2
for h, p in zip(head, page):
    for i in range(1, p+1):
        fname = os.path.join(path, title, '%03d.jpg' % num)
        if not os.path.exists(fname):
            jpgUrl = jpgPath + h + '%03d' % i
            jpgList.append([fname, jpgUrl])
        num += 1

if jpgList:
    downloaded = 0
    group = num // threads

    print('downloading...\t', end='')
    timeStart = time.time()

    for _ in range(group):
        threadList = [Thread(None, download, fname, (fname, jpgUrl)) for (
                      fname, jpgUrl) in jpgList[downloaded:downloaded+threads]]
        for t in threadList:
            t.start()
        for t in threadList:
            t.join()
        downloaded += threads

    threadList = [Thread(None, download, fname, (fname, jpgUrl)) for
                  (fname, jpgUrl) in jpgList[downloaded:]]
    for t in threadList:
        t.start()
    for t in threadList:
        t.join()

    timeEnd = time.time()
    print('%.1fs done' % (timeEnd - timeStart))

print(os.popen('java -jar img2pdf.jar "%s"' % directory).read())
