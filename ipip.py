#!/usr/bin/env python
#coding=utf-8
__author__ = 'caiqiqi'

import sys
import requests
from lxml import html

url = 'http://www.ipip.net/ip.html'

xpath_basics  = "//*[@id='myself']"
xpath_details = "//td[2]"
#xpath_details_2 = "/html/body/div[2]/div[3]/div[2]/div[1]"

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
    print soup.find(id='myself').get_text().encode("utf-8")

def parse_html_by_xpath(html_str):
    tree = html.fromstring(html_str)
    basics  = tree.xpath(xpath_basics)
    details = tree.xpath(xpath_details)
    #details_2 = tree.xpath(xpath_details_2)
    for i in basics:
        print i.text.encode("utf-8").lstrip()
    for i in details:
        if i.text:
            print i.text.encode("utf-8")


def parse_html_by_pq(html_str):
    from pyquery import PyQuery as pq
    doc = pq(html_str)
    print doc('#myself').text()
    for i in doc('td'):
        if i.text:
            print i.text.encode("utf-8").strip()


s = requests.Session()
payload = ''

try:
    payload = 'ip=' + sys.argv[1]
except IndexError as e:
    print u"[!] 未输入查询IP, 直接返回当前IP"

if __name__ == '__main__':
    r = s.post(url, data=payload, headers=header)
    #parse_html_by_bs(r.content)
    parse_html_by_xpath(r.content)
    #parse_html_by_pq(r.content)
    s.close()
