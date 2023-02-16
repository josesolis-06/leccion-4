import requests, json
url = "https://pokeapi.co/api/v2/pokemon"
response = requests.request("GET", url)
# print(response.text)


mi_diccionario = json.loads (response.text)
print(mi_diccionario["results"][0])

resultados = mi_diccionario ["results"]
for resultado in resultados:
    print(resultado)
