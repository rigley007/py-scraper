import urllib.request as request

import urllib.parse as parse

url='http://chardonnay.ucs.louisiana.edu:9080/EDBC/Newspaper/newspaper01.jsp'

data=parse.urlencode({"course":"598  ","avail":"YES","subject":"CSCE","term":"SP15"})

data=data.encode("utf8")

req=request.urlopen(url,data)

s=req.read()

s=s.decode("utf8")

with open("temphtml.html","w") as f:
	print(s,file=f)
pass

