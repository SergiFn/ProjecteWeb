import requests
import pprint
import json

class Client(object):
    
    def __init__(self) -> None:
        self.url1 = "http://api.ipify.org/?format=json"
        self.url2 = "https://ipinfo.io/"
        self.ur2suf = "/geo"

    def get_api(self, url):
        result = requests.get(url)
        dades = json.loads(result.text)
        return dades

    def get_myip(self):
        dades = self.get_api(self.url)
        return dades["ip"]

    def get_info(self, ip):
        dades = self.get_api(self.url+ip+self.url2suf)
        return dades

    def get_data(self):
        # descarregar web
        myip = self.get_myip()
        # llegir html
        dades = self.get_info(dades)
        # retornar dades
        return dades

    def get_api(query):
        pass

if __name__=="__main__":
    client = Client()
    dades = client.get_data()
    pprint.print(dades)