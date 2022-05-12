import requests
import json

pais = input()

data = requests.get("http://181.129.219.106:3002/" + pais)

continentes = json.loads(data.text)

if pais in continentes["America"]:
    print(continentes["America"][pais]["capital"])
    print(continentes["America"][pais]["idiomas"])
    print(continentes["America"][pais]["ciudades"])
    print(continentes["America"][pais]["gentilicio"])


if pais in continentes["Africa"]:
    print(continentes["Africa"][pais]["capital"])
    print(continentes["Africa"][pais]["idiomas"])
    print(continentes["Africa"][pais]["ciudades"])
    print(continentes["Africa"][pais]["gentilicio"])
