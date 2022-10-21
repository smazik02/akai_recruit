#Funkcja 

import json, datetime, urllib.request, os.path, requests

dirname = os.path.dirname(__file__)
ratio=1.01
base='USD'
target='EUR'

#filename = base+'2'+target+'.json'
filename = 'ratios.json'
filepath = os.path.join(dirname, filename)
f=open(filepath,'w')
rat={}
rat["base_currency"] = base
rat["target_currency"] = target
rat["date_fetched"] = datetime.datetime.now().strftime("%Y-%m-%d")
rat["ratio"] = ratio
rat=json.dumps(rat, indent=4, separators=(", ", " : "))
f.write(rat)
f.close

# Should save or update exchange rate for given pair in json file
# takes ratio as argument
# example file structure is shipped in project's directory, yours can differ (as long as it works)
'''''
[
  {
    "base_currency": "PLN",
    "target_currency": "EUR",
    "date_fetched": "2019-09-27",
    "ratio": 0.2279721874
  },
  {
    "base_currency": "PLN",
    "target_currency": "USD",
    "date_fetched": "2019-09-27",
    "ratio": 0.2492875869
  },
  {
    "base_currency": "USD",
    "target_currency": "EUR",
    "date_fetched": "2019-09-27",
    "ratio": 0.9144947417
  }
]
'''''