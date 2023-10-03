class OrdenLavado:
    def __init__(self, numeroOrden:int, importeLavadoBase:float) -> None:
        self._numeroOrden = numeroOrden
        self._importeLavadoBase = importeLavadoBase
    
    @property
    def numeroOrden(self):
        return self._numeroOrden
    
    @property
    def importeLavadoBase(self):
        return self._importeLavadoBase
    
    def importeFinal(self)->float:
        return self.importeLavadoBase
    
    def __str__(self)->str:
        return f"Numero de Orden: {self.numeroOrden}, Importe de lavado Base: {self.importeLavadoBase}$"