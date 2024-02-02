from bs4 import BeautifulSoup
import requests

page_num = "?page="


def get_profiles(url) -> BeautifulSoup:
    # get page html code
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
    else:
        html_content = "sorry nothing found :("
        print("Failed to retrieve the webpage")

    # make soup
    soup = BeautifulSoup(html_content, 'lxml')

    # find lawyers
    Profiles = soup.find_all(
        'div', attrs={'data-vars-category': 'ProfileView'})

    return Profiles


with open('lawyers.txt', 'w') as f:
    for i in range(2, 5):
        Profiles = get_profiles(
            "https://www.justia.com/lawyers/probate/georgia" + "?page=" + str(i))

        for prfl in Profiles:
            f.write(prfl.get_text())

        f.write("______________________________________________")
