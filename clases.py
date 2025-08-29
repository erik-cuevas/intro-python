class personaje:
    def __init__(self, nombre, salud, mana):
        self.nombre = nombre
        self.salud = salud
        self.mana = mana

    def atacar(self, enemigo):
        print(f"{self.nombre} ataca a {enemigo.nombre}")
        
    def loot(self, enemigo):
        print(f"{self.nombre} obtiene loot de {enemigo.nombre}")