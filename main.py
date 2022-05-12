import requests
import json

data = requests.get("https://raw.githubusercontent.com/kerenv95/mundo/main/continentes.json")

continentes = json.loads(data.text)

pais = input()

if pais in continentes["America"]:
    print(continentes["America"][pais]["capital"])
    print(continentes["America"][pais]["idiomas"])
    print(continentes["America"][pais]["ciudades"])


if pais in continentes["Africa"]:
    print(continentes["Africa"][pais]["capital"])
    print(continentes["America"][pais]["idiomas"])
    print(continentes["America"][pais]["ciudades"])
