# Import Required Library
from tkinter import *
from tkcalendar import Calendar
from datetime import date
from tkinter import filedialog
#import gerenciador_de_download_para_estações_RENEP
from datetime import datetime
from tkinter.tix import * #lib para texto flutuante

#  -------- CONFIGURACAO DA PAGINA -------------------

root = Tk()
root.title("Gerenciador de Downloads para Arquivos RINEX - RENEP")

# DIMENSOES DA PAGINA
dimx_pg = 700
dimy_pg = 700

# DIMENSOES DA SCREEN
dimx_screen = root.winfo_screenwidth()
dimy_screen = root.winfo_screenheight()

# POSICAO PAGINA
posx_pg = (dimx_screen/2) - (dimx_pg/2)
posy_pg = 0 #(dimy_screen/2) - (dimy_pg/2)



root.iconbitmap("gerenciador_de_download_para_estações_RENEP/icon/icon_download.ico")
root["bg"] = "#DEDEDE" # cor baseada no sistema de cores hexadecimal
root.geometry("%dx%d+%d+%d" %(dimx_pg, dimy_pg, posx_pg, posy_pg)) # tamanho da pag + posicionamento
root.resizable(FALSE,TRUE) # possibilita redimensionar a janelas em ambos eixos.
root.minsize(dimy_pg, dimx_pg) # dimensoes minimas da pg


#--------------- CONSTRUCAO DO PAGINA ---------------

texto_desc = Label(root,
text = "Este programa destina-se a realizar o download dos\n"
"arquivos RINEX da rede RENEP de forma automatizada e\n"
"direcionada de acordo com as bases mais próxima do  \n"
"trabalho executado.",
bg = "yellow",
fg = "black",
font = "Arial 10 bold ",
width= 60,
height= 8,
padx= 20,
pady= 1,
justify= LEFT,
anchor= CENTER, # posicionar txt: N S E W NE CENTER (norte, sul, leste, oeste, nordeste)
bd= 1,
relief= "solid" # bordas possiveis: solid, groove, flat, raised, sunken, ridge
).place(x=100, y=20)

#INPUT DAS INFORMACOES
texto_desc = Label(root,
text= "Selecione data do trabalho: ",
bg = "#DEDEDE" ,
fg = "black",
font = "Arial 8 bold",
width= 25,
height= 1,
padx= 2,
pady= 2,
justify= CENTER,
anchor= N, # posicionar txt: N S E W NE CENTER (norte, sul, leste, oeste, nordeste)
bd= 1,
relief= "flat" # bordas possiveis: solid, groove, flat, raised, sunken, ridge
).place(x=10, y=200)



# Add Calendar
cal = Calendar(root, selectmode = "day",
			year = date.today().year, month = date.today().month,
			day = date.today().day)

cal.place(x=200, y=200)

def grad_date():
	date.config(text =  cal.get_date())

"""# Add Button and Label
cmd = Button(root, text = "Selecione a data ",
	command = grad_date)

cmd.place(x=275, y=390)"""

date = Label(root, text = "", bg= "#DEDEDE" , font= "arial 8 ")
date.place(x=380, y=395)

def get_date():
    global data_lev

    data_lev = cal.get_date()
    data_lev = datetime.strptime(data_lev.split("/")[0] + "/" + data_lev.split("/")[1] + "/20" + data_lev.split("/")[2], "%m/%d/%Y")

    print(data_lev)

Button(root, text="Gravar data", command= lambda: get_date()).place(x=300, y=390)


#ENTRADA LATITUDE
Label(root,
text= 'Informe a Latitude (°): ',
bg = "#DEDEDE" ,
fg = "black",
font = "Arial 8 bold",
width= 25,
height= 1,
padx= 2,
pady= 2,
justify= LEFT,
anchor= N, # posicionar txt: N S E W NE CENTER (norte, sul, leste, oeste, nordeste)
bd= 1,
relief= "flat" # bordas possiveis: solid, groove, flat, raised, sunken, ridge
).place(x=10, y=440)



input_latitude = Entry(root, justify=LEFT)
input_latitude.place(x=180, y=440)


#ENTRADA LONGITUDE
Label(root,
text= 'Informe a Longitude (°): ',
bg = "#DEDEDE" ,
fg = "black",
font = "Arial 8 bold",
width= 25,
height= 1,
padx= 2,
pady= 2,
justify= LEFT,
anchor= N, # posicionar txt: N S E W NE CENTER (norte, sul, leste, oeste, nordeste)
bd= 1,
relief= "flat" # bordas possiveis: solid, groove, flat, raised, sunken, ridge
).place(x=350, y=440)

input_longitude = Entry(root, justify=LEFT)
input_longitude.place(x=520, y=440)


Button(root, text="Gravar coordenadas", command= lambda: get_coord()).place(x=285, y=470)

#Button(root, text="ok", command= lambda: input_longitude.get()).place(x=655, y=445)

#ENTRADA HORA INICIAL
Label(root,
text= "Informe a hora inicial do\n"
      "intervalo de rastreio\n"
      "desejado:",
bg = "#DEDEDE" ,
fg = "black",
font = "Arial 8 bold",
width= 25,
height= 15,
padx= 2,
pady= 2,
justify= LEFT,
anchor= N, # posicionar txt: N S E W NE CENTER (norte, sul, leste, oeste, nordeste)
bd= 1,
relief= "flat" # bordas possiveis: solid, groove, flat, raised, sunken, ridge
).place(x=10, y=500)

hora_inicio = Scale(root, from_= 0, to= 24, orient= HORIZONTAL)
hora_inicio.place(x=180, y=505)


# ENTRADA HORA FINAL
Label(root,
text= "Informe a hora final do\n"
      "intervalo de rastreio\n"
      "desejado:",
bg = "#DEDEDE" ,
fg = "black",
font = "Arial 8 bold",
width= 25,
height= 15,
padx= 2,
pady= 2,
justify= LEFT,
anchor= N, # posicionar txt: N S E W NE CENTER (norte, sul, leste, oeste, nordeste)
bd= 1,
relief= "flat" # bordas possiveis: solid, groove, flat, raised, sunken, ridge
).place(x=350, y=500)


hora_fim = Scale(root, from_= 0, to= 24, orient= HORIZONTAL)
hora_fim.place(x=520, y=505)

#Create a tooltip
tip= Balloon(root)
#Bind the tooltip with button
tip.bind_widget(hora_fim,balloonmsg="Certifique-se de que a hora FINAL seja superior a hora INICIAL.")


#data = datetime.strptime(cal.get_date()[0:5]+"20"+data_cal[5:], "%d/%m/%Y")


# EXTRAIR OS DADOS DE ENTRADA

def get_coord():
    global ilat
    global ilng

    ilat = input_latitude.get()
    ilng = input_longitude.get()

    if "," in str(ilat):
        ilat = ilat.replace(",", ".")
        ilat = float(ilat)
    if "," in str(ilng):
        ilng = ilng.replace(",", ".")
        ilng = float(ilng)

    print(ilat,ilng)

def get_hora_inicial():

    global hi

    hi = hora_inicio.get()

    if int(hi) < 10:
        hi = "0" + str(hi)
    print(hi)

def get_hora_final():

    global hf

    hf = hora_fim.get()

    if int(hf) < 10:
        hf = "0" + str(hf)
    print(hf)


Button(root, text="Gravar hora inicial", command= lambda: get_hora_inicial()).place(x=180, y=555)

Button(root, text="Gravar hora final", command= lambda: get_hora_final()).place(x=525, y=555)

# SELECIONAR O NÚMERO DE ESTAÇÕES

def get_quant_estacao():

    global quant_estacao

    quant_estacao = quantidade_estacao.get()
    print(quant_estacao)

Label(root,
text= "Informe a quantidade de\n"
      "estações mais prox.\n"
      "que deseja salvar:",
bg = "#DEDEDE" ,
fg = "black",
font = "Arial 8 bold",
width= 25,
height= 15,
padx= 2,
pady= 2,
justify= LEFT,
anchor= N, # posicionar txt: N S E W NE CENTER (norte, sul, leste, oeste, nordeste)
bd= 1,
relief= "flat" # bordas possiveis: solid, groove, flat, raised, sunken, ridge
).place(x=10, y=600)

quantidade_estacao = Scale(root, from_= 1, to= 48, orient= HORIZONTAL)
quantidade_estacao.place(x=180, y=600)


Button(root, text="Gravar quant.\nestações", command= lambda: get_quant_estacao()).place(x=300, y=600)

#EXPORTACAO DOS DADOS

# A funcao Lambda fara com que filedialog.askdirectory() nao seja executado automaticamente

def get_path():
    global path
    path = filedialog.askdirectory()
    print(path)


Button(root, text = "Selecionar diretório onde os arquivos serão salvos", command= lambda: get_path()).place(x=410, y=600)

"""
Label(root,
text = "Base Selecionada:",
bg = "#C8C8C8",
fg = "black",
font = "Arial 9 bold ",
width= 50,
height= 6,
padx= 20,
pady= 1,
justify= LEFT,
anchor= NW, # posicionar txt: N S E W NE CENTER (norte, sul, leste, oeste, nordeste)
bd= 1,
relief= "solid" # bordas possiveis: solid, groove, flat, raised, sunken, ridge
).place(x=10, y=650)


base = "MIRA"

dist = 15

Label(root,
text= "» " + base + " dist. " + str(dist) + " Km",
bg = "#C8C8C8" ,
fg = "black",
font = "Arial 8 bold",
width= 15,
height= 1,
padx= 1,
pady= 1,
justify= LEFT,
anchor= N, # posicionar txt: N S E W NE CENTER (norte, sul, leste, oeste, nordeste)
bd= 1,
relief= "flat" # bordas possiveis: solid, groove, flat, raised, sunken, ridge
).place(x=20, y=680)

"""


Button(root, text="Baixar arquivos Rinex", command=root.destroy).place(x=280, y=660)

# Execute Tkinter
root.mainloop()

### SCRIPT


"""
data_lev = datetime.strptime(str("10/09/2022"), "%d/%m/%Y")
ilat = 31.4545
ilng = 51.4545
hi = "04"
hf = "05"
path = "C:/Users/GEOME188/PycharmProjects/pythonProject/gerenciador_de_download_para_estações_RENEP/rinex/paste3"
"""

from numpy import sqrt
from tkinter import *
from tkinter import filedialog
from urllib import request
#!pip install geopandas
import math

import pandas as pd


df = pd.read_csv("gerenciador_de_download_para_estações_RENEP/estacoes_RENEP.csv", encoding = 'utf-8', delimiter = ';')
df.head(20)

# CALCULO PARA CONVERTER COORDENADAS GEODESICAS EM CARTESIANAS TRIDIMENSIONAIS

from numpy import radians

def geo_to_cart3d(lat,lng,h):

#FORMULAÇÃO GEODESICA (PARÂMETROS DO ELIPSOIDE GRS80)

  a = 6378137 #semi eixo maior
  b = 6356752.3141 #semi eixo menor
  e1 = 0.00669438002290 #1º excentricidade
  e2 = 0.00673949677548 #2º excentricidade
  f = 0.00335281068118 #achatamento

  PN = a*(1 - e1)/(1 - e1 * (math.sin(radians(lat)))**2)**0.5 # Pequena Normal
  GN = a/(1 - e1 * (math.sin(radians(lat)))**2)**0.5 # Grande Normal
  X = (GN + h) * math.cos(radians(lat)) * math.cos(radians(lng))
  Y = (GN + h) * math.cos(radians(lat)) * math.sin(radians(lng))
  Z = (PN + h) * math.sin(radians(lat))
  return (X,Y,Z)


# FUNCAO PARA CALCULAR A DISTANCIA ENTRE COORDENADAS CARTESIANAS 3D
def calc_dist(x2,x1,y2,y1,z2,z1):
  return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

# SCRIPT PARA IDENTIFICAR O DIA DO RASTREIO
from datetime import datetime

data = data_lev #data do rastreio que deseja-se fazer download
data_zero = datetime.strptime("01/01/" + str(data)[:4], "%d/%m/%Y") #data zero para contagem

calc_data_preliminar = data - data_zero #calculo preliminar para definir os dias corridos da data
calc_data = int(str(calc_data_preliminar)[:3]) + 1 #calculo para definir os dias corridos da data
print(calc_data)



lat = float(ilat)
lng = float(ilng)
#h = float(input('Digite as coordenadas geodésicas - Altitude elipsoidal(m ex: 20.316): '))
h = 0




# CRIA DICT COM KEY= NOME DAS ESTAÇÕES E VALUE = DIST. ENTRE COORDENADA DE ENTRADA

i=0
st = {}
while i < len(df.index):

  st[df.iloc[i]['Nome_est']] = round(calc_dist(geo_to_cart3d(lat,lng,h)[0],geo_to_cart3d(df.iloc[i]['lat_aprox'],df.iloc[i]['lng_aprox'],0)[0],
          geo_to_cart3d(lat,lng,h)[1],geo_to_cart3d(df.iloc[i]['lat_aprox'],df.iloc[i]['lng_aprox'],0)[1],
          geo_to_cart3d(lat,lng,h)[2],geo_to_cart3d(df.iloc[i]['lat_aprox'],df.iloc[i]['lng_aprox'],0)[2]),3)
  i = i+1


# CRIA NOVO DICIONARIO REORDENANDO COM AS X ESTAÇÕES MAIS PROXIMAS DO PONTO DE ANÁLISE. A DISTANCIA ESTÁ EM KM

st_ordem = {}
for i in sorted(st, key = st.get):
    st_ordem[i] = round(st[i]/1000,3)
    if len(st_ordem) == quant_estacao:
      break


inicio = str(hi)
fim = str(hf)



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

# FUNCAO PARA PEGAR A CHAFE A PARTIR DE CADA ITEM PELO SEU VALOR (PARA O INICIO DO INTERVALO)
def get_key_inicio(val):
  for key, value in intervalo_inicio.items():
    if val == value:
      return key

# FUNCAO PARA PEGAR A CHAFE A PARTIR DE CADA ITEM PELO SEU VALOR (PARA O FIM DO INTERVALO)
def get_key_fim(val):
  for key, value in intervalo_fim.items():
    if val == value:
      return key

#ftp://ftp.dgterritorio.pt/ReNEP/AGUE/2022/07/20/ague201x.zip   MODELO DE LINK

print('\n\n' + str(quant_estacao) + ' ESTAÇÕES RENEP MAIS PRÓXIMAS PARA O RASTREIO DO DIA ' + str(data)[:10] + '\n')
for letra in faixa_hora[id_inicio:id_fim]:
  for i in list(st_ordem.keys()):
    print(i, ': Dist.', st_ordem[i], 'Km | Hora:', get_key_inicio(letra), 'às', get_key_fim(letra) )
    print('Link para download dos arquivos RINEX:')
    print("ftp://ftp.dgterritorio.pt/ReNEP/"+i+"/"+str(data)[:4]+"/"+str(data)[5:7]+"/"+str(data)[8:10]+"/"+i.lower()+str(calc_data)+letra+".zip"+'\n') # linha para baixar os arquivos Rinex.
  print('___________________________________________________________________\n')
    #print('Link para download do Relatório de Informação de Estação:')
    #print("https://geoftp.ibge.gov.br/informacoes_sobre_posicionamento_geodesico/rbmc/relatorio/Descritivo_"+i+'\n')



baixar_arquivos = 'y'
print('\n')

#SCRIPT PARA REALIZAR O DOWNLOAD DOS ARQUIVOS ZIP.

if baixar_arquivos == 'y':
  path_local = path
  for letra in faixa_hora[id_inicio:id_fim]:
    for i in list(st_ordem.keys()):
      link_url = "ftp://ftp.dgterritorio.pt/ReNEP/" + i + "/" + str(data)[:4] + "/" + str(data)[5:7] + "/" + str(data)[8:10] + "/" + i.lower() + str(calc_data) + letra + ".zip"  # linha para baixar os arquivos Rinex.
      file = i.lower() + str(calc_data) + letra + ".zip"
      path_file = path_local + "/" + file
      request.urlretrieve(link_url, path_file)
      print(file + " .... OK")



#SCRIPT PARA GERAR O ARQUIVO TXT COM OS LINKS DE DOWNLOAD + RALATÓRIO DE INFO PARA CADA BASE.
"""
with open(path_local + "/" + 'links_estacoes_RENEP.txt', 'w') as arquivo:
  arquivo.write(str(quantidade_estacao) +' ESTAÇÕES MAIS PRÓXIMAS PARA O RASTREIO DO DIA ' + str(data) + '\n\n')
  for i in list(st_ordem.keys()):
    arquivo.write(i + ': Dist.'+ str(st_ordem[i]) + 'Km'+ '\n')
    arquivo.write('Link para download dos arquivos RINEX:'+ '\n')
    arquivo.write("ftp://ftp.dgterritorio.pt/ReNEP/"+i+"/"+str(data)[:4]+"/"+str(data)[5:7]+"/"+str(data)[8:10]+"/"+i.lower()+str(calc_data)+letra+".zip"+'\n\n')
    arquivo.write('Link para download do Relatório de Informação de Estação:'+ '\n')
    arquivo.write(df.iloc[df.index[df['Nome_est'] == i].tolist()[0]]['link_descritivo'] + '\n\n')
    arquivo.write('_________________________________________________________________________________________________________________' + '\n\n')
  arquivo.write('\n\n' + 'Desenvolvido por, Guilherme Torres.'+ '\n')
  arquivo.write('Contato: guilhervieto@gmail.com')

"""

print("\n\nDownload finalizado!")

"""# PÁGINA 2

root2 = Tk()
root2.title("RESULTADOS - Gerenciador de Downloads para Arquivos RINEX - RENEP")



root2.mainloop()"""