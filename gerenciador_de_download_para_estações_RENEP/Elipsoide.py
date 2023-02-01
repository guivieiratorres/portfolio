from math import radians
import math


class Elipsoide:
    """Classe que cria objeto do tipo Elipsoide, esse objeto pode ser configurado para
    qualquer sistema de referencia passando os parametros do elipsoide.

    OBS: Por default a classe assume a configuração do elipsoide GRS80.

    *com essa classe pode-se fazer a conversão de coordenadas geodesicas para cartesianas 3D.

     a: semi eixo maior
     b: semi eixo menor
    e1: 1º excentricidade
    e2: 2º excentricidade
     f: achatamento
    """

    def __init__(self, a=6378137.0, b=6356752.3141, e1=0.00669438002290, e2=0.00673949677548, f=0.00335281068118):
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

        PN = (self.a * (1 - self.e1) / (1 - self.e1 * (math.sin(radians(lat))) ** 2) ** 0.5)  # Pequena Normal

        X = (GN + h) * math.cos(radians(lat)) * math.cos(radians(lng))
        Y = (GN + h) * math.cos(radians(lat)) * math.sin(radians(lng))
        Z = (PN + h) * math.sin(radians(lat))
        return (X, Y, Z)