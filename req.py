import requests
import bs4

url='http://chardonnay.ucs.louisiana.edu:9080/EDBC/Newspaper/newspaper01.jsp'
for cnum in range(500,600):
	cnumber = str(cnum) + "  "
	postdata = {"course":cnumber,"avail":"YES","subject":"CSCE","term":"FA14"}
	s = requests.session()
	response = s.post(url, data = postdata)
	soup = bs4.BeautifulSoup(response.text)
	it_body = iter(soup.find_all("tr"))
	for course in it_body:
		cells = course.findAll("td")
		if len(cells[0].text) == 3: 
			cells = [ele.text.strip() for ele in cells]
			print ("CSCE" + str(cnum),cells)
