class wheel:
    def __init__(self,ancho, diametro, rodadura):
        self.ancho = ancho
        self.diametro = diametro
        self.rodadura = rodadura
        self.presion = 0

    def set_presure(self, presion):
        self.presion = presion

    def print_info(self):
        print("dimensiones de la rueda :", self.ancho, "mm/", self.diametro, "R", self.rodadura)
        print("preson deseada :" ,self.presion, "bar")