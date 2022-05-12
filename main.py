import requests
import json

pais = input()

data = requests.get("https://restcountries.com/v3.1/name/" + pais)

continentes = json.loads(data.text)

print(json.dumps(continentes, indent=2))

"""
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
