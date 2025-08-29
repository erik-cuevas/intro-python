from Sandwich import Sandwich

class SandwichCarne(Sandwich):
    
    def __init__ (self, pan, precio, queso):
        super().__init__(pan, precio)
        self.queso = queso
        
    def descripcion(self):
        return f"Sandwich de Carne con {self.pan} y queso {self.queso}"