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

class creacion_dispositivos:
    def utilidades(respuesta, marca, procesador, ram):
        if respuesta.lower() == "portatil":
            dispositivo_1 = portatil(marca, procesador, ram)
            return dispositivo_1
        if respuesta.lower() == "movil":  
            dispositivo_2 = movil(marca, procesador, ram)
            return dispositivo_2

# Función principal
def main():
    while True:
        pregunta = input("Deseas registrar un dispositivo: ")
        if pregunta == "si":
            respuesta = input("Que tipo de dispositivo deseas registrar (portatil o movil): ")
            if respuesta.lower() == "portatil":
                marca = input("Que tipo de marca es: ")
                procesador = input("Que tipo de procesador es: ")
                ram = input("Que tipo de ram tiene: ") 
                dispositivo_1 = creacion_dispositivos.utilidades(respuesta, marca, procesador, ram)
            if respuesta.lower() == "movil":  
                marca_1 = input("Que tipo de marca es: ")
                procesador_1 = input("Que tipo de procesador es: ")
                ram_1 = input("Que tipo de ram tiene: ")
                dispositivo_2 = creacion_dispositivos.utilidades(respuesta, marca_1, procesador_1, ram_1)


        elif pregunta == "no":
            print("== Información de dispositivos ==")
            dispositivo_1.mostrar_info()
            print("------------------------")
            dispositivo_2.mostrar_info()
            print("Saliendo del programa...")
            break

if __name__ == "__main__":
    main()
