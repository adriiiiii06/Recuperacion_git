# Clases para representar dispositivos
from abc import ABC, abstractmethod

class Dispositivo(ABC):
    def __init__(self, marca, procesador, ram):
        self.marca = marca  # marca
        self.procesador = procesador  # procesador
        self.ram = ram

    @abstractmethod    
    def mostrar_info():
        pass

class portatil(Dispositivo):

    def mostrar_info(self):
        print("Dispositivo: Portátil")
        print(f"Marca: {self.marca}")
        print(f"Procesador: {self.procesador}")
        print(f"RAM: {self.ram} GB")


class movil(Dispositivo):

    def mostrar_info(self):
        print("Dispositivo: Móvil")
        print(f"Marca: {self.marca}")
        print(f"Procesador: {self.procesador}")
        print(f"RAM: {self.ram} GB")


# Función principal
def main():
    dispositivo_1 = portatil("Dell", "i7", 16)
    dispositivo_2 = movil("Samsung", "Snapdragon", 8)

    print("== Información de dispositivos ==")
    dispositivo_1.mostrar_info()
    print("------------------------")
    dispositivo_2.mostrar_info()


if __name__ == "__main__":
    main()
