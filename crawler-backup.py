from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
'''

old_links_array = []
rss_array = []
'''
link = []

def listToStr(lista):
    
    aux_array = []
    for x in lista:
        aux_array.append(''.join(str(e) for e in x).lower())

    return aux_array 

#abre o arquivo de saida
link_file = open("./links.csv", "a")

'''
#leitura dos arquivos
keywords = pd.read_csv("./keywords.csv").values.tolist()
old_links = pd.read_csv("./links.csv").values.tolist()
rss = pd.read_csv("./rss.csv").values.tolist()
'''

keywords_array = listToStr(pd.read_csv("./keywords.csv").values.tolist())
old_links_array = listToStr(pd.read_csv("./links.csv").values.tolist())
rss_array = listToStr(pd.read_csv("./rss.csv").values.tolist())

'''
#conversao dos arquivos de leitura
for x in old_links:
    str_link = ''.join(str(e) for e in x)
    old_links_array.append(str_link)

for x in rss:
    str_rss = ''.join(str(e) for e in x)
    rss_array.append(str_rss)
'''

print(keywords_array)

while (True):


    for feed in rss_array:

        print(keywords_array)

        #requisicao 
        result = requests.get(feed).text
        soup = BeautifulSoup(result, 'xml')

        #encontra todas as noticias
        noticias = soup.find_all('item')

        #crawler 
        for kw in keywords_array:
            
            for news in noticias:
                if kw in news.title.text.lower():
                    link.append(news.link.text)

        #checa se o link ja existe e adiciona no arquivo de saida
        for x in link:
            if(x not in old_links_array):
                link_file.write(x + "\n")
                old_links_array.append(x)
                print("Link: {} adicionado.".format(x))

    time.sleep(6)
    
link_file.close()