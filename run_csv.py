# -*- coding: utf8 -*-
from grab import Grab
import urllib
import csv
import time
from renamer import latinizator


def download_csv(word, num):
	res = urllib.quote(word) 

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
	g.response.save("static/" + str(num) + " " + latinizator(word) + ".csv")



u = 'карандаш'
inp_list=["уличное освещение",
			"дорожное освещение",
			"осветительные приборы",
			"промышленное освещение",
			"промышленные светильники",
			"техническое освещение",
			"светодиодные технологии",
			"световой поток",
			"энергоэффективность",
			"энергосбережение",
			"светодиоды",
			"свет",
			"источник света",
			"цветовая температура",
			"индекс цветопередачи",
			"светодиод",
			"вторичная оптика",
			"корпус светильника",
			"Реконструкция сетей наружного освещения",
			"Реконструкция сетей уличного освещения",
			"Замена осветительного оборудования",
			"Энергосервисный контракт",
			"Система уличного освещения",
			"Система освещения",
			"Программа энергосбережения",
			"Программа энергоэффективности"]

for i, inp_word in enumerate(inp_list):
 	download_csv(inp_word, i)
 	time.sleep(2)
 	print "static/" + str(i) + " " + latinizator(inp_word) + ".csv was successfully downloaded"

