import requests
import bs4
import smtplib
from sets import Set
coursesilike = Set(['274753', '513'])

def send_email(c_name, e_num):
	username = 'rui.ning.1990@gmail.com'
	password = 'qzhrstgvmemxrohm'
	recipient = ['rui.ning.1990@gmail.com']
	SUBJECT = "Empty Space for CSCE" + str(c_name) + "!"
	TEXT = "Total number of empty slot is: " + str(e_num) + "."
	content  = """\From: %s\nTo: %s\nSubject: %s\n\n%s""" % (username, ", ".join(recipient), SUBJECT, TEXT)
	session = smtplib.SMTP('smtp.gmail.com', 587)
	session.ehlo()
	session.starttls()
	session.login(username, password)
	session.sendmail(username, recipient, content)

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
		if (len(cells[0].text) == 3 and cells[1].text in coursesilike):
			#print (cells[0].text, cells[1].text, cells[2].text, cells[3].text)
			send_email(cnum, (int(cells[2].text) - int(cells[3].text))) 
			#cells = [ele.text.strip() for ele in cells]
			#print ("CSCE" + str(cnum),cells)
