from grab import Grab
from grab.tools.lxml_tools import drop_node
import xlwt
from datetime import datetime

url = 'http://zakupki.gov.ru/epz/order/quicksearch/update.html?placeOfSearch=FZ_44&_placeOfSearch=on&placeOfSearch=FZ_223&\
            _placeOfSearch=on&placeOfSearch=FZ_94&_placeOfSearch=on&priceFrom=0&priceTo=200+000+000+000&publishDateFrom=&\
            publishDateTo=&updateDateFrom=&updateDateTo=&orderStages=AF&_orderStages=on&orderStages=CA&_orderStages=on&\
            _orderStages=on&_orderStages=on&sortDirection=false&sortBy=UPDATE_DATE&recordsPerPage=_10&pageNo=1&searchString=&\
            strictEqual=false&morphology=false&showLotsInfo=false&isPaging=true&isHeaderClick=&checkIds='
xpath = '//td[@class="descriptTenderTd"]//dd[a][2]'

g = Grab(log_file='static/out.html')
g.go(url)
wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')

style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
    num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')


page = g.doc.select(xpath)
for i, element in enumerate(page):
    ws.write(i, 0, i)
    ws.write(i, 1, element.text())

##for elem in g.xpath_list(xpath):
##    print elem.text


##ws.write(0, 0, 1234.56, style0)
##ws.write(1, 0, datetime.now(), style1)
##
##ws.write(2, 2, xlwt.Formula("A3+B3"))

wb.save('static/result_file.xls')
