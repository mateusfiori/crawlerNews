from bs4 import BeautifulSoup
import requests
import pandas as pd

#requisicao 
result = requests.get("https://br.advfn.com/indice/iee").text
soup = BeautifulSoup(result, 'html.parser')

print(div.text)