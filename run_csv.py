# -*- coding: utf8 -*-
from grab import Grab
import urllib
import csv

u = 'карандаш'
res = urllib.quote(u) 
inp_list = csv.reader(open("input.csv", "r"))


url = "http://zakupki.gov.ru/epz/order/quicksearch/orderCsvSettings/quickSearch/download.html?"+\
		"placeOfSearch=FZ_44&_placeOfSearch=on&"+\
		"placeOfSearch=FZ_223&_placeOfSearch=on&"+\
		"placeOfSearch=FZ_94&_placeOfSearch=on&" +\
		"priceFrom=0&"+\
		"priceTo=200+000+000+000&"+\
		"publishDateFrom=13.11.2015&"+\
		"publishDateTo=14.11.2015&"+\
		"updateDateFrom=&"+\
		"updateDateTo=&"+\
		"orderStages=AF&_orderStages=on&"+\
		"orderStages=CA&_orderStages=on&"+\
		"_orderStages=on&_orderStages=on&"+\
		"sortDirection=false&"+\
		"sortBy=UPDATE_DATE&"+\
		"recordsPerPage=_10&"+\
		"pageNo=1&"+\
		"searchString=" + res + "&" +\
		"strictEqual=false&"+\
		"morphology=false&"+\
		"showLotsInfo=false&"+\
		"isPaging=false&"+\
		"isHeaderClick=&"+\
		"checkIds=&"+\
		"quickSearch=true&"+\
		"userId=4752519c-eb29-43ba-88e0-8ee913772035&"+\
		"conf=true;true;true;true;true;true;true;true;false;true;true;true;true;true;true;true;false;"

g = Grab()
g.go(url)
g.response.save('static/out.csv')

