from selenium import webdriver
import argparse
import pandas as pd

#selenium start guide : http://selenium-python.readthedocs.io/getting-started.html
#download chrome webdriver from https://sites.google.com/a/chromium.org/chromedriver/downloads
def search_results(first_name, last_name, search_query, display=None):
  #driver = webdriver.Chrome()
  base_url = 'https://www.linkedin.com/search/results/index/?keywords=firstname%3A{0}%20AND%20lastname%3A{1}%20AND%20{2}&origin=GLOBAL_SEARCH_HEADER'.format(first_name, last_name, search_query)
  base_url= base_url.replace(' ', '%20')
  if display:
    driver = webdriver.Chrome()
    driver.get(base_url)
  return base_url

def main(dict):
  #input is {key: [A-first, A-last], [B-first, B-last], ...}
  print 'hi'
  

if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  dict = {'machine learning': [['John', 'Doe'], ['Bob', 'Smith']]}
  #input is {key: [A-first, A-last], [B-first, B-last], ...}

  csv_dict = {'name':[], 'url':[], 'keyword':[]}

  for key in dict:
    for i in range(len(dict[key])):
      csv_dict['url'].append(search_results(dict[key][i][0], dict[key][i][1], key))
      csv_dict['name'].append( [dict[key][i][0], dict[key][i][1]])
      csv_dict['keyword'].append(key)

  pd.DataFrame(csv_dict).to_csv('tmp.csv', index=False) 
      




