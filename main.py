import requests
from bs4 import BeautifulSoup

def scrape_the_list(url):
    try:
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Failed to get the webpage: {response.status_code}")
            return []
        
        soup = BeautifulSoup(response.text, 'html.parser')

        watches = soup.find_all('section', class_ = "CategorySearchCard__CategorySearchCardGrid-sc-1o7izf2-1 dliokm")

        return watches

    except Exception as e:
        print(f"Error has occurred: {e}")
        return []    

def get_watches():
    url = "https://www.liveauctioneers.com/c/watches/97/"

    watches = scrape_the_list(url)

    print(watches)

get_watches()