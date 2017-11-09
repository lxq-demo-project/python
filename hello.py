# -*- coding: utf-8 -*-

#判断帖子是否被删
import urllib.request
import ssl
import re
from bs4 import BeautifulSoup

ssl._create_default_https_context = ssl._create_unverified_context
f = urllib.request.urlopen('https://tieba.baidu.com/p/5419350437')
content = f.read()
soup = BeautifulSoup(content,"html.parser")
for tag in soup.find_all('div', id='errorText'):
	if tag:
		print('已被删除')
print('end')
