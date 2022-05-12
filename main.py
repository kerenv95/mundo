import requests
import json

pais = input()

data = requests.get("https://restcountries.com/v3.1/name/" + pais)

continentes = json.loads(data.text)

print(json.dumps(continentes, indent=2))

"""
if pais in continentes["America"]:
    print(continentes["America"][pais]["capital"])
    print(continentes["America"][pais]["language"])
    print(continentes["America"][pais]["cities"])


if pais in continentes["Africa"]:
    print(continentes["Africa"][pais]["capital"])
    print(continentes["America"][pais]["language"])
    print(continentes["America"][pais]["cities"])
"""

