from Sandwich import Sandwich
from Venta import Venta
from SandwichCarne import SandwichCarne
from SandiwchVegetariano import SandwichVegetariano

mi_sandwich = Sandwich("integral", 1200)
venta = Venta()
vegetariano = SandwichVegetariano("integral", 2000, "tomate lechuga")
carne = SandwichCarne("frances", 2500, "cheddar")


carne.set_precio(4500)

venta.agregar_sandwich(vegetariano)
venta.agregar_sandwich(carne)