class LavadoCajaCamion:
    def __init__(self, anchoCaja:float, largoCaja:float, altoCaja:float, importeBaseLavadoCajaM3:float) -> None:
        self._anchoCaja = anchoCaja 
        self._largoCaja = largoCaja
        self._altoCaja = altoCaja
        self._importeBaseLavadoCajaM3 = importeBaseLavadoCajaM3

    @property
    def anchoCaja(self):
        return self._anchoCaja
    
    @property
    def largoCaja(self):
        return self._largoCaja
    
    @property
    def altoCaja(self):
        return self._altoCaja
    
    @property
    def importeBaseLavadoCajaM3(self):
        return self._importeBaseLavadoCajaM3
    
    def volumen(self)->float:
        return self.altoCaja * self.anchoCaja * self.largoCaja
    
    def importeFinalLavadoCajaM3(self)->float:
        return self.importeBaseLavadoCajaM3 * (1 if self.altoCaja <= 0.5 else 1.1 if 0.5 < self.altoCaja <= 2 else 1.25)
        
    def calcularImporte(self)->float:
        return self.volumen() * self.importeFinalLavadoCajaM3()
    
    def __str__(self)->str:
        return f"Ancho de Caja: {self.anchoCaja}, Largo de Caja: {self.largoCaja}, Alto de Caja: {self.altoCaja}, importe base por M3: {self.importeBaseLavadoCajaM3}$"