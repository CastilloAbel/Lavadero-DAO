from ordenlavado import OrdenLavado
from functools import reduce
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
    
    def addOrdenLavado(self, orden:OrdenLavado):
        self.ordenesLavado[orden.numeroOrden] = orden

    def importeFinalPromedioOrdenesLavado(self)->float:
        return sum(list(map(lambda x: x.importeFinal(), self.ordenesLavado.values())))

    def cantidadOrdenesLavadoAutoBusDesdeHasta(self, desde:int, hasta:int)->int:
        return len(list(filter(lambda x: x.__class__.__name__ == "OrdenLavadoAutobus" and desde <= x.cantidadAsientos <= hasta,self.ordenesLavado.values())))

    def existeOrdenLavado(self, nroOrden:int)->bool:
        return True if self.ordenesLavado[nroOrden] else False
    
    def listarImportesFinales(self)->list:
        return list(map(lambda x: f"Numero Orden: {x.nroOrden}, Importe Final: {x.importeFinal()}$", self.ordenesLavado.values())).sort()
    
    def numeroOrdenConImporteFinalMasCaro(self)->int:
        return reduce(lambda x, y: x if x.importeFinal() >= y.importeFinal() else y,self.ordenesLavado.values()).nroOrden