import requests
from bs4 import BeautifulSoup
import time, os
import pandas as pd
import schedule
import time
import datetime

def scraper(url, class_):
    response  = requests.get(url)
    page = response.text
    soup = BeautifulSoup(page, 'html.parser')

    def get_data(tr, tag='td'):
        text_list = [td.get_text(strip=True) for td in tr.find_all(tag)[1:5]]
        return text_list

    scraped_items = []

    table = soup.find('table', class_=class_)
    trs = table.find_all('tr')
    for tr in trs: 
        scraped_items.append(get_data(tr, 'td'))
    
    return scraped_items

def extract_justices():
    justice_data = scraper('https://constitution.congress.gov/resources/supreme-court-justices/', 
                        'table table-sticky-thead table-bordered')
    justice_cols = ['Justice Name', 'Term Start Date', 'Term End Date', 'Appointing President']
    justice_df = pd.DataFrame(justice_data[1:], columns=justice_cols)
    justice_df.to_csv('justices.csv')

def extract_parties():
    pres_party_data = scraper('https://www.theguardian.com/news/datablog/2012/oct/15/us-presidents-listed', 
                            'in-article sortable')
    pres_party_cols = ['President', 'Party']
    pres_party_df = pd.DataFrame(pres_party_data[1:], columns=pres_party_cols)
    pres_part_df.to_csv('pres_parties.csv')


schedule.every(4).seconds.do(extract_justices())
schedule.every(4).seconds.do(extract_parties())

    # while True:
    #    schedule.run_pending()
    #    time.sleep(1)
    # while True:
    # schedule.run_pending()
    # # 5 minutes == 300 seconds
    # if (datetime.datetime.now() - start).seconds >= 300:
    #     break
    # # And here we halt execution for a second
    # time.sleep(1)
      


