from bs4 import BeautifulSoup
import requests
from Lawyer import Lawyer

response = requests.get("https://www.justia.com/lawyers/probate/georgia")
if response.status_code == 200:
    html_content = response.text
else:
    html_content = "sorry nothing found :("
    print("Failed to retrieve the webpage")

soup = BeautifulSoup(html_content, 'lxml')

Lawyers = []

Profiles = soup.find_all('div', attrs={'data-vars-category': 'ProfileView'})
n = 1
for profile in Profiles:
    my_Lawyer = Lawyer()

    # count the number of scrapes
    print(n)
    n += 1

    # scrape pages
    web_page = profile.find('a')
    if web_page:
        my_Lawyer.web_page = web_page.get('href')
    else:
        my_Lawyer.web_page = "no page found"

    # scrape names
    name = profile.find('strong', class_='name')
    if name:
        my_Lawyer.name = name.get_text()
    else:
        my_Lawyer.name = "no name found"

    # scrape lawyer-expl
    expl = profile.find('div', class_='lawyer-expl')

    if expl:
        my_Lawyer.expl = expl.get_text()
    else:
        my_Lawyer.expl = "no explanation found"

    # scrape info
    detailed_info = profile.find(
        'div', class_='lawyer-detailed-info').find('div', class_="-lawyer-address")

    if detailed_info:
        my_Lawyer.telefon = detailed_info.find('strong', class_="-phone")
        my_Lawyer.addr = detailed_info.find('span', class_="-address")
    else:
        my_Lawyer.telefon = "no detailed info found :("

    Lawyers.append(my_Lawyer)


print(Lawyers[0])
