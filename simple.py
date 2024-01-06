import requests
from bs4 import BeautifulSoup

urls = ("https://wuzzuf.net/search/jobs/?a=hpb&q=cyber%20security&start=0","https://wuzzuf.net/search/jobs/?a=hpb&q=cyber%20security&start=1","https://wuzzuf.net/search/jobs/?a=hpb&q=cyber%20security&start=2")

for pages in urls:
	response = requests.get(pages)
	soup = BeautifulSoup(response.content, "html.parser")

	results = soup.find(id="app")
	job_elements = results.find_all("div", class_="css-1gatmva e1v1l3u10")

	for job_element in job_elements:
	    title = job_element.find("h2", class_="css-m604qf")
	    company = job_element.find("a", class_="css-17s97q8")
	    city = job_element.find("span", class_="css-5wys0k")
	    job_time = job_element.find("span", class_="css-1ve4b75 eoyjyou0")
	    description = job_element.find("a", class_="css-5x9pm1")
	    print("Job-Title : ",title.text)
	    print("Company-Name : ",company.text)
	    print("Country : " ,city.text)
	    print("Job-Time : " ,job_time.text)
	    print("Description :" ,description.text)
	    print()
	    print("----------------------------------")
	    print()