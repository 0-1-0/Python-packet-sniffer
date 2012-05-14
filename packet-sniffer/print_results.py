#!/opt/local/bin/python
# encoding: utf-8
from pickle import load
saved = open('out', 'rb')
hosts = load(saved)
print hosts['vkontakte.ru']


