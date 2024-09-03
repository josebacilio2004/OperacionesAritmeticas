from Operaciones_MCD
from Operaciones_MCD

if __name__ == "__main__":
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))

    mcd_calculadora = MCD(numero1, numero2)
    resultado = mcd_calculadora.calcular()

    print(f"El MCD de {numero1} y {numero2} es: {resultado}")
