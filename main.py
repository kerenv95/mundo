import requests
import json

data = requests.get("https://raw.githubusercontent.com/kerenv95/mundo/main/continentes.json")

continentes = json.loads(data.text)

pais = input()

if pais in continentes["America"]:
    print(continentes["America"][pais]["capital"])
    print(continentes["America"][pais]["language"])
    print(continentes["America"][pais]["cities"])


if pais in continentes["Africa"]:
    print(continentes["Africa"][pais]["capital"])
    print(continentes["America"][pais]["language"])
    print(continentes["America"][pais]["cities"])
