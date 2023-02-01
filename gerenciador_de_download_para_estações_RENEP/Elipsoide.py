from math import radians
import math


class Elipsoide:
    """Classe que cria objeto do tipo Elipsoide, esse objeto pode ser configurado para
    qualquer sistema de referencia passando os parametros do elipsoide.

    *com essa classe pode-se fazer a conversão de coordenadas geodesicas para cartesianas 3D."""

    def __init__(self, a, b, e1, e2, f):
        self.a = a  # semi eixo maior
        self.b = b  # semi eixo menor
        self.e1 = e1  # 1º excentricidade
        self.e2 = e2  # 2º excentricidade
        self.f = f  # achatamento

    def GeoToCart3d(self, lat, lng, h=0):
        self.lat = lat
        self.lng = lng
        self.h = h

        GN = (self.a / (1 - self.e1 * (math.sin(radians(lat))) ** 2) ** 0.5)  # Grande Normal

        PN = (self.a * (1 - self.e1) / (1 - self.e1 * (math.sin(radians(lat))) ** 2) ** 0.5 )  # Pequena Normal

        X = (GN + h) * math.cos(radians(lat)) * math.cos(radians(lng))
        Y = (GN + h) * math.cos(radians(lat)) * math.sin(radians(lng))
        Z = (PN + h) * math.sin(radians(lat))
        return (X, Y, Z)


a_grs80 = 6378137  # semi eixo maior
b_grs80 = 6356752.3141  # semi eixo menor
e1_grs80 = 0.00669438002290  # 1º excentricidade
e2_grs80 = 0.00673949677548  # 2º excentricidade
f_grs80 = 0.00335281068118  # achatamento
