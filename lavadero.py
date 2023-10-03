from ordenlavado import OrdenLavado
class Lavadero:
    def __init__(self, razonSocial:str) -> None:
        self._razonSocial = razonSocial
        self._ordenesLavado = dict()

    @property
    def razonSocial(self):
        return self._razonSocial
    
    @property
    def ordenesLavado(self):
        return self._ordenesLavado
    
    def agregarOrden(self, orden:OrdenLavado):
        self.ordenesLavado[orden.numeroOrden] = orden