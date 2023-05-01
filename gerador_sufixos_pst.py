'''
GERAR NOVO EXECUTAVEL

'''


import pandas as pd

'''df = pd.read_csv("20230209-27-JAF_unificado.csv", encoding="utf-8",delimiter=";")
#print(df_base.head(1))"""'''


print("Conversão iniciada...\n") #para mostrar no executavel a evolução do processamento

import os
pasta = './'
for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        if ".csv" in arquivo:
            file = arquivo

df = pd.read_csv(file, encoding="utf-8",delimiter=",")
#print(df.head(10))


# Converter Index para uma coluna no dataframe
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'Id'})


# identifica o nome da coluna que tem os codigos
for i in list(df.loc[0]):
    if type(i) == type(""): #identifica coluna com valores tipo string
        posicao_coluna = list(df.loc[0]).index(i) #identifica a posicao da coluna no df

nome_coluna = df.columns[posicao_coluna] #armazena o nome da coluna

print("...\n")#para mostrar no executavel a evolução do processamento

#criar linha a mais para corrigir erros de codigo (linha será apagada)
colunas = list(df.columns)
i = 0
while i < len(colunas):
    if colunas[i] == nome_coluna:
        colunas[i] = "APAGAR"
    else:
        colunas[i] = 0
    i=i+1

df.loc[len(df.index)] = colunas #adiciona a linha criada a ultima linha do df

#codigos que nao devem sofrer codificacao de sufixo
codigo_ponto = ["arv","cv agua q","cv agua r","cv ap q","cv ap r","cv edp q","cv edp r",
                "cv gas","cv gas q","cv resid q","cv resid r","cv san","cv san q","cv tlf q",
                "cv tlf r","cvelec","cvlixo","cv r","cv q","pc","pt","ptat","ptluz","ptmt",
                "pttlf","semaf","sinal","e","VID","BAC","FAL"]

#logics de criacao das codificacoes de sufixo
LAYER_sufixo = []
for i in df["Id"]:
    if df[nome_coluna][i] not in codigo_ponto:
        if df["Id"][i] == 0:
            #print(df["Id"][i], str(df[nome_coluna][i])+".1")
            LAYER_sufixo.append(str(df[nome_coluna][i])+".1")

        elif df[nome_coluna][i] != df[nome_coluna][i - 1]:
            #print(df["Id"][i], str(df[nome_coluna][i])+".1") #está causando um problema no código
            LAYER_sufixo.append(str(df[nome_coluna][i])+".1")

        elif df[nome_coluna][i] == df[nome_coluna][i+1]: #pesquisar por erros e exceçoes na internet
            #print(df["Id"][i],df[nome_coluna][i])
            LAYER_sufixo.append(str(df[nome_coluna][i]))

        else:
            #print(df["Id"][i],str(df[nome_coluna][i])+".0")
            LAYER_sufixo.append(str(df[nome_coluna][i])+".0")

    else:
        #print(df["Id"][i],str(df[nome_coluna][i]))
        LAYER_sufixo.append(str(df[nome_coluna][i]))


# corrigir codificacao de pontos marcacao inicio e ponto marcacao fim para situacoes com codigo duplo por ponto
for i in LAYER_sufixo:
    if len(i.split(".")) == 3:
        LAYER_sufixo[LAYER_sufixo.index(i)] = i.replace(".", i[-2:]+".", 1)


print("...\n")#para mostrar no executavel a evolução do processamento

ultima_linha = len(df.index) - 1
if df[nome_coluna][ultima_linha] != df[nome_coluna][ultima_linha-1]: #correcao da ultima linha
    LAYER_sufixo[ultima_linha] = df[nome_coluna][ultima_linha]

df.insert(2, nome_coluna+"_sufixo",LAYER_sufixo) # adiciona a lista codificada ao dataframe
#print(df.head(-5))

#preparacao do dados de saida
df = df.drop(len(df.index)-1) #apagar última linha usada de recurso para corrigir o bug
df = df.drop(columns=nome_coluna) #deleta coluna nao mais necessaria (base da codificacao)
df = df.drop(columns="Id") #deleta coluna Index nao mais necessaria

#conversao do df para csv e ajuste do nome de saida
df.to_csv(file.split(".")[0]+"_sufixo."+file.split(".")[1], index=False)

'''#conversao do df para csv e ajuste do nome de saida
df.to_csv('texto', index=False)'''

print("\nProcesso finalizado!")#para mostrar no executavel a evolução do processamento
