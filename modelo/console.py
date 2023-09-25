from dataclasses import dataclass
from modelo import bicicleta



@dataclass
class usuario:
     nombre:str
     correo:str
     n_telefono:int
     DNI:int
def registro_usuario(self):
        print("Bienvenid@ a esta app para alquilar bicicletas")
        nombre:str=input("ingresa tu nombre")
        DNI:int=input("ingresa tu cedeula")
        correo:str=input("ingrese su correo electronico")
        if "@" in correo:
            print("Se puede")
        else:
            print("No se puede")
        
        n_telefono:int=input("ingrese su celular")


