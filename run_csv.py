# -*- coding: utf-8 -*-
from grab import Grab
import urllib
import csv
import time
import os
import datetime

def ts(): # return timestamp
	return '[' + str(datetime.datetime.now()) + ']'

def download_csv(word,df,dt,sec):
    time.sleep(sec)
    res = urllib.quote(word.encode('utf8'))

    url = "".join([
    	"http://zakupki.gov.ru/epz/order/quicksearch/orderCsvSettings/quickSearch/download.html?",
    	"placeOfSearch=FZ_44&_placeOfSearch=on",
    	"&placeOfSearch=FZ_223&_placeOfSearch=on",
    	"&placeOfSearch=FZ_94&_placeOfSearch=on",
    	"&priceFrom=0",
    	"&priceTo=200+000+000+000",
    	"&publishDateFrom=", df,
    	"&publishDateTo=14.11.2015", dt,
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
    # g.response.save("static/" + str(num) + ".csv")
    return g.response.body

def read_inplist():
    res_line = ''
    f = open(path + 'input.txt', 'r')
    for line in f:
        res_line += line
    f.close()
    return res_line.decode('utf8').split(chr(13))

path = os.path.abspath(os.path.dirname(__file__)) + "/../gh-crappy/parse/"
yesterday = (datetime.date.today() - datetime.timedelta(1)).strftime("%d.%m.%Y")
today = datetime.date.today().strftime("%d.%m.%Y")
inplist = read_inplist()
length = len(inplist)
delta = 1


print "[" + str(length) + " files]      wait about:", str(datetime.timedelta(seconds=delta*length))
f = open(path + "media/result_file.csv", "w")
for i, inp_word in enumerate(inplist):
	f.write(download_csv(inp_word, yesterday, today, delta))
	f.write("\n")
	print ts(), "csv file", str(i+1), "(from", length, ") was successfully downloaded"

