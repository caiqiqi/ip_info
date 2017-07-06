#!/usr/bin/env python
#coding=utf-8
__author__ = 'caiqiqi'

import sys


import requests
from lxml import html

url = 'http://www.ipip.net/ip.html'

xpath_basics  = "//*[@id='myself']"
xpath_details = "//td[2]"
#xpath_details = "/html/body/div[2]/div[4]/table[1]/tbody/tr[2]/td[2]"

header = {
'Host':"www.ipip.net",
'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:50.0) Gecko/20100101 Firefox/50.0",
#'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
'Referer':"http://www.ipip.net/",
'Connection':"keep-alive",
'Content-Type':"application/x-www-form-urlencoded"
}

def parse_html_by_bs(html_str):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html_str, "lxml")
    return soup.find(id='myself').get_text()

def parse_html_by_xpath(html_str):
    tree = html.fromstring(html_str)
    basics  = tree.xpath(xpath_basics)
    details = tree.xpath(xpath_details)
    for i in basics:
        print i.text
    for i in details:
        if i.text:
            print i.text


def parse_html_by_pq(html_str):
    from pyquery import PyQuery as pq
    doc = pq(html_str)
    return doc('#myself').text()

s = requests.Session()
payload = ''

try:
    payload = 'ip=' + sys.argv[1]
except IndexError as e:
    print "[!] 未输入查询IP, 直接返回当前IP"

if __name__ == '__main__':
    r = s.post(url, data=payload, headers=header)
    #print parse_html_by_bs(r.content)
    parse_html_by_xpath(r.content)
    #print parse_html_by_pq(r.content)
    s.close()
