class MCD:
    def __init__(self, numero1: int, numero2: int):
        self.numero1 = numero1
        self.numero2 = numero2

    def calcular(self) -> int:
        a = self.numero1
        b = self.numero2

        # Continuar hasta que los números sean iguales
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a

        # Cuando a y b son iguales, ese valor es el MCD
        return a


# Solicitar al usuario que ingrese los números
if __name__ == "__main__":
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))

    mcd_calculadora = MCD(numero1, numero2)
    resultado = mcd_calculadora.calcular()

    print(f"El MCD de {numero1} y {numero2} es: {resultado}")
