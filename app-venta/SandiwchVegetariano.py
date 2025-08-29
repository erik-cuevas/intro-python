
from Sandwich import Sandwich

class SandwichVegetariano(Sandwich):
    
    def __init__ (self, pan, precio, verduras):
        super().__init__(pan, precio)
        self.verduras = verduras
        
    def descripcion(self):
        return f"Sandwich Vegetariano con {self.pan} y verduras {self.verduras}"