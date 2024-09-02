class OperacionesAritmeticas():
    def ingresoNumeros(self):
        numero01=float(input('Ingrese sumando 1: '))
        numero02=float(input('Ingrese sumando 2: '))
        return numero01,numero02

    def suma(self, numero01,numero02):
        return numero01 + numero02

if __name__ == '__main__':
    operacion = OperacionesAritmeticas()
    num1,num2 =operacion.ingresoNumeros()
    print(f"{num1}+ {num2} = {num1+num2}")