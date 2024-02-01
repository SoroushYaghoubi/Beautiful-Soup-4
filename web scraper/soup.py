from bs4 import BeautifulSoup
import requests
from Lawyer import Lawyer

# get page html code
response = requests.get("https://www.justia.com/lawyers/probate/georgia")
if response.status_code == 200:
    html_content = response.text
else:
    html_content = "sorry nothing found :("
    print("Failed to retrieve the webpage")

# make soup
soup = BeautifulSoup(html_content, 'lxml')

# find lawyers

Profiles = soup.find_all('div', attrs={'data-vars-category': 'ProfileView'})
for profile in Profiles:
    if profile:
        print(profile.get_text())
