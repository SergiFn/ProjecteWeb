import urllib.request
import xmltodict
import pprint

class Client(object):
    
    def __init__(self) -> None:
        self.url = "http://export.arxiv.org/api/query?start=0&max_results=10&search_query=all"

    def get_api(self, query):
        url_file = urllib.request.urlopen(self.url+query)
        xmldata = url_file.read().decode('utf-8')
        return xmldata

    def parse_xml(self, xmldata):
        dades = xmltodict.parse(xmldata)
        return dades

    def select_data(self, data):
        dades = []
        for e in data['feed']['entry']:
            title = e['title']
            dades.append(title)
        return dades
        # dades = [e['title'] for e in data['data']['entry']]

    def get_data(self, query):
        # descarregar web
        dades = self.get_api(query)
        # llegir html
        dades = self.parse_xml(dades)
        # retornar dades
        dades = self.select_data(dades)
        return dades

    def get_api(query):
        pass

if __name__=="__main__":
    client = Client()
    dades = client.get_data("lstm")
    pprint.print(dades)