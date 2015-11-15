# -*- coding: utf-8 -*-
from grab import Grab
import urllib
import csv
import time


def download_csv(word, num):
    time.sleep(2)
    res = urllib.quote(word.encode('utf8')) 

    url = "".join([
    	"http://zakupki.gov.ru/epz/order/quicksearch/orderCsvSettings/quickSearch/download.html?",
    	"placeOfSearch=FZ_44&_placeOfSearch=on",
    	"&placeOfSearch=FZ_223&_placeOfSearch=on",
    	"&placeOfSearch=FZ_94&_placeOfSearch=on",
    	"&priceFrom=0",
    	"&priceTo=200+000+000+000",
    	"&publishDateFrom=13.11.2015",
    	"&publishDateTo=14.11.2015",
    	"&updateDateFrom=",
    	"&updateDateTo=",
    	"&orderStages=AF&_orderStages=on",
    	"&orderStages=CA&_orderStages=on",
    	"&_orderStages=on&_orderStages=on",
    	"&sortDirection=false",
    	"&sortBy=UPDATE_DATE",
    	"&recordsPerPage=_10",
    	"&pageNo=1",
    	"&searchString=", res,
    	"&strictEqual=false",
    	"&morphology=false",
    	"&showLotsInfo=false",
    	"&isPaging=false",
    	"&isHeaderClick=",
    	"&checkIds=",
    	"&quickSearch=true",
    	"&userId=null",
    	"&conf=true;true;true;true;true;true;true;true;true;true;true;true;true;true;true;true;true;"])

    g = Grab()
    g.go(url)
    g.response.save("static/" + str(num) + ".csv")


def read_inplist():
    res_line = ''
    f = open('input.txt', 'rb')
    for line in f:
        res_line += line
    f.close()
    return unicode(res_line, "utf8").split('\n')

inp_list = read_inplist()


for i, inp_word in enumerate(inp_list):
    download_csv(inp_word, i)
    print "static/" + str(i) + ".csv was successfully downloaded"

##print inp_list[0].encode('utf8')
