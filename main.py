import requests
from bs4 import BeautifulSoup

def scrape_the_list(url):
    try:
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Failed to get the webpage: {response.status_code}")
            return []
        
        soup = BeautifulSoup(response.text, 'html.parser')

        watches_list = soup.find_all('section', class_ = "CategorySearchCard__CategorySearchCardGrid-sc-1o7izf2-1 dliokm")

        watches_dict = dict()

        for index, watch in enumerate(watches_list, 1):
            
            item_name = soup.find('span', class_ = 'hui-text-body-primary text-text-primary').text

            item_price_str = soup.find('span', class_ = 'FormattedCurrency__StyledFormattedCurrency-sc-1ugrxi1-0 cqnbDD').text
            
            watches_dict[index] = {}
            watches_dict[index]["Name"] = item_name
            watches_dict[index]["Price"] = item_price_str

        return watches_dict

    except Exception as e:
        print(f"Error has occurred: {e}")
        return []    

def get_watches(url):
    # url: string of https URL from liveauctioneers.com

    results = scrape_the_list(url)

    return results

url = "https://www.liveauctioneers.com/c/watches/97/"