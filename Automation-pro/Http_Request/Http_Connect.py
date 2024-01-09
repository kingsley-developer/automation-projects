import requests

class HTTP:
    def __init__(self, url: str):
        self.url = url
    def get_UrL(self, query: map = {}):
        if query == {}:
            r = requests.get(self.url)
            print(r.text)
            print("-------------------")
            print(r.content)
            print("-------------------")
            return r.json()

        r = requests.get(self.url, params=query)
        print(r.text)
        print("-------------------")
        print(r.content)
        print("-------------------")
        return r.json()

    def post_url(self, body: map):
        r = requests.post(self.url, data=body)
        print(r.text)
        print("-------------------")
        print(r.content)
        print("-------------------")
        return r.json()

    def delete_url(self):
        r = requests.delete(self.url)
        print(r.text)
        print("-------------------")
        print(r.content)
        print("-------------------")
        return r.json()

    def put_url(self, body:map):
        r = requests.post(self.url, data=body)
        print(r.text)
        print("-------------------")
        print(r.content)
        print("-------------------")
        return r.json()
