import json, datetime, urllib.request, os.path, requests

dirname = os.path.dirname(__file__)
#filename = os.path.join(dirname, 'ratios.json')

class RatioObtainer:
    base = None
    target = None

    def __init__(self, base, target):
        self.base = base
        self.target = target

    def was_ratio_saved_today(self):
        filename = self.base+'2'+self.target+'.json'
        filepath = os.path.join(dirname, filename)
        if os.path.isfile(filepath)==True:
            f=open(filepath,)
            check=json.load(f)
            date=(check.get('date_fetched'))
            if datetime.datetime.now().strftime("%Y-%m-%d")!=date:
                f.close
                return False
            else:
                f.close
                return True
        else:
            f.close
            return False

        # This function checks if given ratio was saved today and if the file with ratios is created at all
        # should return false when file doesn't exist or if there's no today's exchange rate for given values at all
        # should return true otherwise

    def fetch_ratio(self):
        url = 'https://api.exchangerate.host/convert?from='+self.base+'&to='+self.target
        print(url)
        response = requests.get(url)
        data = response.json()
        if data.get('success')==True:
            self.save_ratio(data.get('result'))
        # This function calls API for today's exchange ratio
        # Should ask API for today's exchange ratio with given base and target currency
        # and call save_ratio method to save it
        pass

    def save_ratio(self, ratio):
        filename = self.base+'2'+self.target+'.json'
        filepath = os.path.join(dirname, filename)
        f=open(filepath,'w')
        rat={}
        rat["base_currency"] = self.base
        rat["target_currency"] = self.target
        rat["date_fetched"] = datetime.datetime.now().strftime("%Y-%m-%d")
        rat["ratio"] = ratio
        rat=json.dumps(rat, indent=4, separators=(", ", " : "))
        f.write(rat)
        f.close
        # Should save or update exchange rate for given pair in json file
        # takes ratio as argument
        # example file structure is shipped in project's directory, yours can differ (as long as it works)

    def get_matched_ratio_value(self):
        # TODO
        # Should read file and receive exchange rate for given base and target currency from that file
        pass
