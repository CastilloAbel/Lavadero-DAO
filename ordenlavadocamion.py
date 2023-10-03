from ordenlavado import OrdenLavado
from lavadocajacamion import LavadoCajaCamion
class OrdenLavadoCamion(OrdenLavado):
    def __init__(self, numeroOrden:int, importeLavadoBase:float, importeLavadoCabina:float, importeLavadoChasis:float) -> None:
        super().__init__(numeroOrden, importeLavadoBase)
        self._importeLavadoCabina = importeLavadoCabina
        self._importeLavadoChasis = importeLavadoChasis
        self._lavadoCaja = None

    @property
    def importeLavadoCabina(self):
        return self._importeLavadoCabina
    
    @property
    def importeLavadoChasis(self):
        return self._importeLavadoChasis
    
    @property
    def lavadoCaja(self):
        return self._lavadoCaja
    
    @lavadoCaja.setter
    def lavadoCaja(self, lavadoCaja):
        self._lavadoCaja = lavadoCaja

    def importeLavado(self)->float:
        return super().importeFinal() + self.importeLavadoCabina + (0 if self.lavadoCaja is None else self.lavadoCaja.calcularImporte())

    def agregarLavadoCaja(self, lavadoCaja:LavadoCajaCamion)->None:
        self.lavadoCaja = lavadoCaja

    def eliminarLavadoCaja(self)->None:
        self.lavadoCaja = None

    def __str__(self) -> str:
        return super().__str__() + f" Importe de lavado de cabina: {self.importeLavadoCabina}, Importe de lavado de chasis: {self.importeLavadoChasis}, Caja: {'' if self.lavadoCaja is None else self.lavadoCaja}, Importe Final: {self.importeFinal()}"