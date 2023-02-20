# http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=10

class Client(object):
    
    def __init__(self) -> None:
        self.url = "http://export.arxiv.org/api/query?start=0&max_results=10&search_query=all"


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
    print(dades)