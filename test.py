import requests
response = requests.get('http://chardonnay.ucs.louisiana.edu:9080/EDBC/Newspaper/newspaper02.jsp?subject=CSCE&term=SP15')
f = open("ulink.txt","w")
f.write(response.text + '\n')
f.close()
