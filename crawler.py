from bs4 import BeautifulSoup
import requests
import pandas as pd

#requisicao 
result = requests.get("http://rss.uol.com.br/feed/noticias.xml").text
soup = BeautifulSoup(result, 'xml')

#encontra todas as noticias
noticias = soup.find_all('item')

#abre o arquivo de saida
link_file = open("./links.csv", "a")

link = []
old_links_array = []

#leitura dos arquivos
keywords = pd.read_csv("./keywords.csv").values.tolist()
old_links = pd.read_csv("./links.csv").values.tolist()

#conversao dos arquivos de leitura
for x in old_links:
    str_link = ''.join(str(e) for e in x)
    old_links_array.append(str_link)

#crawler 
for kw in keywords:
    str_kw = ''.join(str(e) for e in kw).upper()

    for news in noticias:
        if str_kw in news.title.text.upper():
            link.append(news.link.text)

#checa se o link ja existe e adiciona no arquivo de saida
for x in link:
    if(x not in old_links_array):
        link_file.write(x + "\n")

link_file.close()



