
import math
import pandas as pd
from numpy import radians
from numpy import sqrt
from datetime import datetime
from Elipsoide import *


file_renep= 'gerenciador_de_download_para_estações_RENEP/estacoes_RENEP.csv'
df = pd.read_csv(file_renep, encoding = 'utf-8', delimiter = ';')
df.head(20)


# FUNCAO PARA CALCULAR A DISTANCIA ENTRE COORDENADAS CARTESIANAS 3D
def calc_dist(x2,x1,y2,y1,z2,z1):
  return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

# SCRIPT PARA IDENTIFICAR O DIA DO RASTREIO

data = datetime.strptime(str(input("Data do rastreio GNSS (dd/mm/aaaa): ")), "%d/%m/%Y") #data do rastreio que deseja-se fazer download
data_zero = datetime.strptime("01/01/" + str(data)[:4], "%d/%m/%Y") #data zero para contagem

calc_data_preliminar = data - data_zero #calculo preliminar para definir os dias corridos da data

if (int(str(calc_data_preliminar)[:3]) + 1) < 99:
  calc_data = '0' + str((int(str(calc_data_preliminar)[:3]) + 1)) #calculo para definir os dias corridos da data
else:
  calc_data = str((int(str(calc_data_preliminar)[:3]) + 1)) #calculo para definir os dias corridos da data
print(calc_data)



lat = float(input('Digite as coordenadas geodésicas - Latitude(g.ggg° ex: 41.047013): '))
lng = float(input('Digite as coordenadas geodésicas - Longitude(g.ggg° ex: -7.04246): '))
h = 0


# CRIA DICT COM KEY= NOME DAS ESTAÇÕES E VALUE = DIST. ENTRE COORDENADA DE ENTRADA

grs80 = Elipsoide()

i=0
st = {}
while i < len(df.index):

  st[df.iloc[i]['Nome_est']] = round(calc_dist(grs80.GeoToCart3d(lat,lng)[0],grs80.GeoToCart3d(df.iloc[i]['lat_aprox'],df.iloc[i]['lng_aprox'],0)[0],
          grs80.GeoToCart3d(lat,lng)[1],grs80.GeoToCart3d(df.iloc[i]['lat_aprox'],df.iloc[i]['lng_aprox'],0)[1],
          grs80.GeoToCart3d(lat,lng)[2],grs80.GeoToCart3d(df.iloc[i]['lat_aprox'],df.iloc[i]['lng_aprox'],0)[2]),3)
  i = i+1


# CRIA NOVO DICIONARIO COM AS 5 ESTAÇÕES MAIS PROXIMAS DO PONTO DE ANÁLISE. A DISTANCIA ESTÁ EM KM

st_ordem = {}
for i in sorted(st, key = st.get):
    st_ordem[i] = round(st[i]/1000,3)
    if len(st_ordem) == 2:
      break


inicio = str(input('Informe a hora inicial do intervalo de rastreio desejado. ex: 02: '))
fim = str(input('Informe a hora final do intervalo de rastreio desejado. ex: 11: '))

# CRIANDO A LOGICA PARA AS LETRAS DAS FIXAS DE HORAS

intervalo_inicio = {
"00":"a",
"01":"b",
"02":"c",
"03":"d",
"04":"e",
"05":"f",
"06":"g",
"07":"h",
"08":"i",
"09":"j",
"10":"k",
"11":"l",
"12":"m",
"13":"n",
"14":"o",
"15":"p",
"16":"q",
"17":"r",
"18":"s",
"19":"t",
"20":"u",
"21":"v",
"22":"w",
"23":"x"
}

intervalo_fim = {
"01":"a",
"02":"b",
"03":"c",
"04":"d",
"05":"e",
"06":"f",
"07":"g",
"08":"h",
"09":"i",
"10":"j",
"11":"k",
"12":"l",
"13":"m",
"14":"n",
"15":"o",
"16":"p",
"17":"q",
"18":"r",
"19":"s",
"20":"t",
"21":"u",
"22":"v",
"23":"w",
"00":"x"
}

faixa_hora = [
"a",
"b",
"c",
"d",
"e",
"f",
"g",
"h",
"i",
"j",
"k",
"l",
"m",
"n",
"o",
"p",
"q",
"r",
"s",
"t",
"u",
"v",
"w",
"x"

]

id_inicio = faixa_hora.index(intervalo_inicio[inicio])
id_fim = faixa_hora.index(intervalo_inicio[fim])

# FUNCAO PARA PEGAR A CHAFE A PARTIR DE CADA ITEM PELO SEU VALOR
def get_key_inicio(val):
  for key, value in intervalo_inicio.items():
    if val == value:
      return key

# FUNCAO PARA PEGAR A CHAFE A PARTIR DE CADA ITEM PELO SEU VALOR
def get_key_fim(val):
  for key, value in intervalo_fim.items():
    if val == value:
      return key

#ftp://ftp.dgterritorio.pt/ReNEP/AGUE/2022/07/20/ague201x.zip   MODELO DE LINK

print('\n\n' + '2 ESTAÇÕES RENEP MAIS PRÓXIMAS PARA O RASTREIO DO DIA ' + str(data)[:10] + '\n')
for letra in faixa_hora[id_inicio:id_fim]:
  for i in list(st_ordem.keys()):
    print(i, ': Dist.', st_ordem[i], 'Km | Hora:', get_key_inicio(letra), 'às', get_key_fim(letra) )
    print('Link para download dos arquivos RINEX:')
    print("ftp://ftp.dgterritorio.pt/ReNEP/"+i+"/"+str(data)[:4]+"/"+str(data)[5:7]+"/"+str(data)[8:10]+"/"+i.lower()+str(calc_data)+letra+".zip"+'\n') # linha para baixar os arquivos Rinex.
    print('___________________________________________________________________\n')
