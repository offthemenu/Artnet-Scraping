import requests
from bs4 import BeautifulSoup

def get_watches(page_count):
    
    watches_dict = {}

    try:
        for n in range(1, page_count+1):
            url = f"https://www.liveauctioneers.com/c/watches/97/?page={n}"

            response = requests.get(url)

            if response.status_code != 200:
                print(f"Failed to get the webpage: {response.status_code}")
                return []

            soup = BeautifulSoup(response.text, 'html.parser')

            watches_list = soup.find_all('section', class_ = "CategorySearchCard__CategorySearchCardGrid-sc-1o7izf2-1 dliokm")

            for watch in watches_list:
                
                name_element = watch.find('span', class_='hui-text-body-primary text-text-primary')
                if name_element:
                    watch_name = name_element.text
                else:
                    # Skip or log the missing name
                    print(f"Missing watch name on page {n}")
                    continue

                price_element = watch.find('span', class_ = 'FormattedCurrency__StyledFormattedCurrency-sc-1ugrxi1-0 cqnbDD')

                if price_element:
                    watch_price_str = price_element.text
                    if watch_price_str[0] != "$":
                        print(f"Not in USD in page {n}. Excluding result to avoid confusion")
                        continue 
                    else:
                        watch_price = float(watch_price_str.replace('$', '').replace(',', ''))
                else:
                    print(f"Missing watch price on page {n}")
                    continue
                
                watches_dict[watch_name] = watch_price
        
        return watches_dict
    
    except Exception as e:
        print(f"Error has occurred: {e}")
        return []

url = "https://www.liveauctioneers.com/c/watches/97/"