import urllib.request as request

import urllib.parse as parse

url='http://chardonnay.ucs.louisiana.edu:9080/EDBC/Newspaper/newspaper01.jsp'

data=parse.urlencode({"course":"598  ","avail":"YES","subject":"CSCE","term":"SP15"})

data=data.encode("utf8")

req=request.urlopen(url,data)

print req

