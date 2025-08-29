#Clase padre

class Sandwich:
    def __init__(self, pan, precio):
        self.pan = pan
        self.__precio = precio
        
        
    #getter
    
    def get_precio(self):
        return self.__precio

    #setter
    def set_precio(self,nuevo_precio ):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("El precio debe ser mayor a 0")
      
    #metodo que sera sobreescrito con polimorfismo        
    def descripcion(self):
        return f"Sandwich con {self.pan}"
        