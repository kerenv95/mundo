import requests
import json

data = requests.get("https://raw.githubusercontent.com/kerenv95/mundo/main/continentes.json")

continentes = json.loads(data.text)

pais = input()

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
