import json, datetime, os.path, requests

dirname = os.path.dirname(__file__)

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
            return False

    def fetch_ratio(self):
        url = 'https://api.exchangerate.host/convert?from='+self.base+'&to='+self.target
        data = requests.get(url).json()
        if data.get('success')==True:
            self.save_ratio(data.get('result'))

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

    def get_matched_ratio_value(self):
        filename = self.base+'2'+self.target+'.json'
        filepath = os.path.join(dirname, filename)
        f=open(filepath,)
        check=json.load(f)
        rtio=(check.get('ratio'))
        return rtio