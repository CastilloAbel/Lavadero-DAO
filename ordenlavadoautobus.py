from ordenlavado import OrdenLavado

class OrdenLavadoAutobus(OrdenLavado):
    def __init__(self, numeroOrden:int, importeLavadoBase:float, cantidadAsientos:int, importeLavadoPorAsiento:float) -> None:
        super().__init__(numeroOrden, importeLavadoBase)
        self._cantidadAsientos = cantidadAsientos
        self._importeLavadoPorAsiento = importeLavadoPorAsiento

    @property
    def cantidadAsientos(self):
        return self._cantidadAsientos
    
    @property
    def importeLavadoPorAsiento(self):
        return self._importeLavadoPorAsiento
    
    def importeFinal(self)->float:
        return super().importeFinal() + (self.cantidadAsientos * self.importeLavadoPorAsiento)
    
    def __str__(self) -> str:
        return super().__str__() + f" Cantidad de asientos: {self.cantidadAsientos}, Importe de lavado por Asiento: {self.importeLavadoPorAsiento}, Importe Final: {self.importeFinal()}"
    