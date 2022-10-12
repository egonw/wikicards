from Bio import Entrez
import urllib
import requests
import wikipedia
import json


def get_entrez_summary(entrez_id, email="tiago.lubiana.alves@usp.br"):
    Entrez.email = email
    handle = Entrez.esummary(db="gene", id=entrez_id)

    record = Entrez.read(handle)
    return record["DocumentSummarySet"]["DocumentSummary"][0]["Summary"]


def get_wikipedia_summary(page_name):
    print(page_name)
    r = requests.get(f"https://en.wikipedia.org/api/rest_v1/page/summary/{page_name}")
    print(r.text)
    return json.loads(r.text)