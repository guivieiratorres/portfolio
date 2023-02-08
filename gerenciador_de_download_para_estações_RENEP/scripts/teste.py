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
    '''kdkdkd'''

    def __init__(self, date_work, lat_work, lng_work, track_start_time, track_end_time, n_station=1):
        self.date_work = datetime.strptime(str(date_work), "%d/%m/%Y") #data do rastreio que deseja-se fazer download
        self.lat_work = lat_work
        self.lng_work = lng_work
        self.track_start_time = track_start_time
        self.track_end_time = track_end_time
        self.n_station = n_station


    def ConsecutiveDays():
        #date_work = datetime.strptime(str(self.date_work), "%d/%m/%Y") #data do rastreio que deseja-se fazer download

        date_zero = datetime.strptime("01/01/" + str(self.date_work)[:4], "%d/%m/%Y")  # data zero para contagem
        calc_date_prep = (date_work - date_zero)  # calculo preliminar para definir os dias corridos da data
        if (int(str(calc_date_prep)[:3]) + 1) < 99:
            calc_date = "0" + str((int(str(calc_date_prep)[:3]) + 1))  # calculo para definir os dias corridos da data
            return(calc_date)
        else:
            calc_date = str((int(str(calc_date_prep)[:3]) + 1))  # calculo para definir os dias corridos da data
            return(calc_date)


    # FUNCAO PARA CALCULAR A DISTANCIA ENTRE COORDENADAS CARTESIANAS 3D
    def CalcDist(lat_renep, lng_renep):
        X1 = lng_renep
        Y1 = lat_renep
        X2 = self.lng_work
        Y2 = self.lat_work

        return X1,X2,Y1,Y2


teste = GdeRenep()