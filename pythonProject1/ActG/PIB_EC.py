import re
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://datosmacro.expansion.com/pib/ecuador'

fecha_list=list()
pib_eur_list=list()
pib_dol_list=list()
variacion_list=list()

html_doc = requests.get(url)
soup = BeautifulSoup(html_doc.text, 'html.parser')
tabla = soup.find('table', attrs={'class': "table tabledat table-striped table-condensed table-hover"})

filas = tabla.find_all('tr')
for fila in filas:
    celdas = fila.find_all('td')
    if len(celdas) > 0:
        fecha= celdas[0].string
        pib_eur= re.sub(r'[^\d.]', '', str(celdas[1].string))
        pib_dol= re.sub(r'[^\d.]', '', str(celdas[2].string))
        variacion= celdas[3].string
        fecha_list.append(fecha)
        pib_eur_list.append(pib_eur)
        pib_dol_list.append(pib_dol)
        variacion_list.append(variacion)

df = pd.DataFrame({'FECHA': fecha_list, 'PIB ANUAL (EUROS)': pib_eur_list, 'PIB ANUAL (DOLARES)': pib_dol_list, 'VARIACION': variacion_list})
df.to_csv('pib.csv', index=False, encoding='utf-8')


#Integrantes:
#Natasha Almeida
#Mercy Cali
#Ketsi Luca
#María Saldaña
