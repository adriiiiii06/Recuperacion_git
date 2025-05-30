# Clases para representar dispositivos

class portatil:
    def __init__(self, m, p, ram):
        self.m = m  # marca
        self.p = p  # procesador
        self.ram = ram

    def mostrar(self):
        print("Dispositivo: Portátil")
        print(f"Marca: {self.m}")
        print(f"Procesador: {self.p}")
        print(f"RAM: {self.ram} GB")


class movil:
    def __init__(self, m, p, ram):
        self.m = m  # marca
        self.p = p  # procesador
        self.ram = ram

    def mostrar(self):
        print("Dispositivo: Móvil")
        print(f"Marca: {self.m}")
        print(f"Procesador: {self.p}")
        print(f"RAM: {self.ram} GB")


# Función principal
def main():
    d1 = portatil("Dell", "i7", 16)
    d2 = movil("Samsung", "Snapdragon", 8)

    print("== Información de dispositivos ==")
    d1.mostrar()
    print("------------------------")
    d2.mostrar()


if __name__ == "__main__":
    main()
