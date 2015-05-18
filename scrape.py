import json

import requests
from bs4 import BeautifulSoup

justicesJson = [] 

r = requests.get('http://en.wikipedia.org/wiki/List_of_Justices_of_the_Supreme_Court_of_the_United_States')
if r.status_code == 200:
  soup = BeautifulSoup(r.text)
  justices = soup.find_all('table')[1]
  for j in justices.find_all('tr'):
    justice = j.find_all('td')

    if len(justice) > 0:
      j = {}
      j['jid'] = justice[0].text
      j['name'] = justice[1].find('a').text
      j['state'] = justice[2].find('a').text
      j['serving_range'] = '%s' % justice[4].contents[1]
      j['president'] =  justice[7].find('a').text

      justicesJson.append(j)

with open('justices.json', 'w') as f:
  json.dump(justicesJson, f)
