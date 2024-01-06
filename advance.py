import subprocess
import sys

def install(packege):
        subprocess.check_call([sys.executable, "-m", "pip", "install", packege])

try:
	import requests
	from bs4 import BeautifulSoup
	from termcolor import cprint
	import os
	import sys

except:
    list1 = ['termcolor','beautifulsoup4','requests']
    for i in list1:
        install(i)


os.system("cls")

cprint("""

-----------------------------------------------------------------------------
 __        __                               __                      _   
 \ \      / /  _   _   ____  ____  _   _   / _|      _ __     ___  | |_ 
  \ \ /\ / /  | | | | |_  / |_  / | | | | | |_      | '_ \   / _ \ | __|
   \ V  V /   | |_| |  / /   / /  | |_| | |  _|  _  | | | | |  __/ | |_ 
    \_/\_/     \__,_| /___| /___|  \__,_| |_|   (_) |_| |_|  \___|  \__|
                                                                        
-----------------------------------------------------------------------------
				CYBERALIENS.NET

	""" , "light_cyan")


job_name = input("Enter Job name (e.g., cyber security): ").replace(" ", "%20")
start_page = int(input("Enter Number of pages : "))

urls = [f"https://wuzzuf.net/search/jobs/?a=hpb&q={job_name}&start={i}" for i in range(0,start_page)]

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

        cprint(f"Job-Title : {title.text}", 'blue', attrs=["bold"])
        print()
        cprint(f"Company-Name : {company.text}", 'white', attrs=["bold"])
        cprint(f"Country : {city.text}", 'white', attrs=["bold"])
        cprint(f"Job-Time : {job_time.text}", 'cyan', attrs=["bold"])
        cprint(f"Description : {title.text}", 'white', attrs=["bold"])
        print()
        print("----------------------------------")
        print()

output_filename = input("Enter output file name (e.g., Jobs.txt): ")

with open(output_filename, "w", encoding="utf-8") as output_file:
    sys.stdout = output_file

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

            cprint(f"Job-Title : {title.text}", "blue", attrs=["bold"])
            print()
            cprint(f"Company-Name : {company.text}", "white", attrs=["bold"])
            cprint(f"Country : {city.text}", "white", attrs=["bold"])
            cprint(f"Job-Time : {job_time.text}", "cyan", attrs=["bold"])
            cprint(f"Description : {title.text}", "white", attrs=["bold"])
            print()
            print("----------------------------------")
            print()

    sys.stdout = sys.__stdout__

cprint(f"The output has been saved to : {output_filename}", "red", attrs=["bold"])
