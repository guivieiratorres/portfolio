import math
import pandas as pd
from numpy import radians
from numpy import sqrt
from datetime import datetime
from Elipsoide import *


file_renep= 'C:/guilherme.torres/Projetos_VScode/portifolio_github/portfolio/gerenciador_de_download_para_estações_RENEP/estacoes_RENEP.csv'
df = pd.read_csv(file_renep, encoding = 'utf-8', delimiter = ';')
df.head(20)


class GdeRenep:
    

    def __init__(self, date_work, lat_work, lng_work, track_start_time, track_end_time, n_station=1):
        self.date_work = datetime.strptime(str(date_work), "%d/%m/%Y") #data do rastreio que deseja-se fazer download
        self.lat_work = lat_work
        self.lng_work = lng_work
        self.track_start_time = track_start_time
        self.track_end_time = track_end_time
        self.n_station = n_station


    def ConsecutiveDays(self):
        #date_work = datetime.strptime(str(self.date_work), "%d/%m/%Y") #data do rastreio que deseja-se fazer download

        date_zero = datetime.strptime("01/01/" + str(self.date_work)[:4], "%d/%m/%Y")  # data zero para contagem
        calc_date_prep = (self.date_work - date_zero).days  # calculo preliminar para definir os dias corridos da data
        if calc_date_prep + 1 <= 99:  # necessário +1 para o calculo de diferença de dias ficar correta
            calc_date = "0" + str(calc_date_prep + 1)  # adicionar 0 para dias consecutivos <= 99
            return(calc_date)
        else:
            calc_date = str(calc_date_prep + 1)  # calculo para definir os dias corridos da data
            return(calc_date)


    # FUNCAO PARA CALCULAR A DISTANCIA ENTRE COORDENADAS CARTESIANAS 3D
    def CalcDist(self,sgr, lat_renep, lng_renep):
        sgr = Elipsoide()
        #lat_work = self.lat
        #lng_work = self.lng
        X1 = sgr.GeoToCart3d(lat= self.lat_work, lng=self.lng_work)[0]
        X2 = sgr.GeoToCart3d(lat= lat_renep, lng=lng_renep)[0]
        Y1 = sgr.GeoToCart3d(lat= self.lat_work, lng=self.lng_work)[1]
        Y2 = sgr.GeoToCart3d(lat= lat_renep, lng=lng_renep)[1]
        Z1 = sgr.GeoToCart3d(lat= self.lat_work, lng=self.lng_work)[2]
        Z2 = sgr.GeoToCart3d(lat= lat_renep, lng=lng_renep)[2]
        
        return math.sqrt((X1 - X2) ** 2 + (Y1 - Y2) ** 2  + (Z1 - Z2) ** 2)
        
        
p1 = GdeRenep(lat_work=41, lng_work=-7, track_start_time=12, track_end_time=14, n_station=1, date_work='09/04/2022')
sgr_teste = Elipsoide()
#print(type(teste.date_work))

dias = p1.ConsecutiveDays()

print(dias)

#1;AGUE;;40.575580500000;-8.446893330000

ague_lat = 40.575580500000
ague_lng = -8.446893330000

calc_p1 = p1.CalcDist(sgr=sgr_teste, lat_renep=ague_lat,lng_renep=ague_lng)

print(calc_p1)

        
p2 = GdeRenep(lat_work=40.5, lng_work=-8.5, track_start_time=12, track_end_time=14, n_station=1, date_work='09/04/2022')

calc_p2 = p2.CalcDist(sgr=sgr_teste, lat_renep=ague_lat,lng_renep=ague_lng)
print(calc_p2)

print(calc_p1-130901.369)


'''
# SCRIPT PARA IDENTIFICAR O DIA DO RASTREIO

input_date = '05/02/2023'

lat = 41#float(input("Digite as coordenadas geodésicas - Latitude(g.ggg° ex: 41.047013): "))
lng = -7#float(input("Digite as coordenadas geodésicas - Longitude(g.ggg° ex: -7.04246): "))
h = 0


# CRIA DICT COM KEY= NOME DAS ESTAÇÕES E VALUE = DIST. ENTRE COORDENADA DE ENTRADA

grs80 = Elipsoide()

i = 0
st = {}
while i < len(df.index):

    st[df.iloc[i]["Nome_est"]] = round(RGE_RENEP.CalcDist(df.iloc[i]["lat_aprox"], df.iloc[i]["lng_aprox"]), 3)
    i = i + 1


# CRIA NOVO DICIONARIO COM AS n ESTAÇÕES MAIS PROXIMAS DO PONTO DE ANÁLISE. A DISTANCIA ESTÁ EM KM

st_ordem = {}
for i in sorted(st, key=st.get):
    st_ordem[i] = round(st[i] / 1000, 3)
    if len(st_ordem) == n_station:
        break


track_start_time = '02'#str(input("Informe a hora inicial do intervalo de rastreio desejado. ex: 02: "))
track_end_time = '03'#str(input("Informe a hora final do intervalo de rastreio desejado. ex: 11: "))

# CRIANDO A LOGICA PARA AS LETRAS DAS FIXAS DE HORAS

track_start_time_interval = {
    "00": "a",
    "01": "b",
    "02": "c",
    "03": "d",
    "04": "e",
    "05": "f",
    "06": "g",
    "07": "h",
    "08": "i",
    "09": "j",
    "10": "k",
    "11": "l",
    "12": "m",
    "13": "n",
    "14": "o",
    "15": "p",
    "16": "q",
    "17": "r",
    "18": "s",
    "19": "t",
    "20": "u",
    "21": "v",
    "22": "w",
    "23": "x",
}

track_end_time_interval = {
    "01": "a",
    "02": "b",
    "03": "c",
    "04": "d",
    "05": "e",
    "06": "f",
    "07": "g",
    "08": "h",
    "09": "i",
    "10": "j",
    "11": "k",
    "12": "l",
    "13": "m",
    "14": "n",
    "15": "o",
    "16": "p",
    "17": "q",
    "18": "r",
    "19": "s",
    "20": "t",
    "21": "u",
    "22": "v",
    "23": "w",
    "00": "x",
}

hour_range_letter = [
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
    "x",
]

id_track_start_time = hour_range_letter.index(track_start_time_interval[track_start_time])
id_track_end_time = hour_range_letter.index(track_start_time_interval[track_end_time])

# FUNCAO PARA PEGAR A CHAFE A PARTIR DE CADA ITEM PELO SEU VALOR
def get_key_track_start_time(val):
    for key, value in track_start_time_interval.items():
        if val == value:
            return key


# FUNCAO PARA PEGAR A CHAFE A PARTIR DE CADA ITEM PELO SEU VALOR
def get_key_track_end_time(val):
    for key, value in track_end_time_interval.items():
        if val == value:
            return key



def generate_link():
    link_renep = "ftp://ftp.dgterritorio.pt/ReNEP/"+ i+ "/"+ str(input_date)[:4]+ "/"+ str(input_date)[5:7]+ "/"+ str(input_date)[8:10]+ "/"+ i.lower()+ consecutive_days(input_date)+ letra + ".zip"+ "\n"  # linha para baixar os arquivos Rinex.
    return link_renep
# ftp://ftp.dgterritorio.pt/ReNEP/AGUE/2022/07/20/ague201x.zip   MODELO DE LINK

print("\n\n" + "2 ESTAÇÕES RENEP MAIS PRÓXIMAS PARA O RASTREIO DO DIA " + str(input_date)[:10] + "\n")
for letra in hour_range_letter[id_track_start_time:id_track_end_time]:
    for i in list(st_ordem.keys()):
        print(i,": Dist.", st_ordem[i],"Km | Hora:", get_key_track_start_time(letra), "às", get_key_track_end_time(letra), )
        print("Link para download dos arquivos RINEX:")
        print(generate_link())
        print("___________________________________________________________________\n")

'''