from Http_Request import Http_Connect

url = Http_Connect.HTTP(url="http://localhost:9870/characters")
json = url.get_UrL(query={})
print(json)
with open("server_data.json", "w") as W:
     W.write(str(json))
W.close()