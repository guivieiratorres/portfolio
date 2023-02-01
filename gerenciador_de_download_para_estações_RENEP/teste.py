from Elipsoide import *

# from Elipsoide import GeoToCart3d

# FORMULAÇÃO GEODESICA (PARÂMETROS DO ELIPSOIDE GRS80)

a_grs80 = 6378137  # semi eixo maior
b_grs80 = 6356752.3141  # semi eixo menor
e1_grs80 = 0.00669438002290  # 1º excentricidade
e2_grs80 = 0.00673949677548  # 2º excentricidade
f_grs80 = 0.00335281068118  # achatamento


grs80 = Elipsoide()

teste = grs80.GeoToCart3d(41.151,-7)

print(teste)