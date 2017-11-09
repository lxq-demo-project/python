# -*- coding: utf-8 -*-

#判断帖子是否被删
import urllib.request
import ssl
import re
from bs4 import BeautifulSoup

ssl._create_default_https_context = ssl._create_unverified_context

allUrl = open('url.txt','r')
s = allUrl.readline()
while s:
	f = urllib.request.urlopen(s)
	content = f.read()
	soup = BeautifulSoup(content,"html.parser")
	t = soup.find_all('div', id='errorText')
	if len(t)==0:
		print('未被删除')
	else:
		print('已被删除')
	s = allUrl.readline()
allUrl.close()