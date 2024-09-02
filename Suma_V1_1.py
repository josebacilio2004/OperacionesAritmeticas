def ingresoNumeros():
    numero01=float(input('Ingrese sumando 1: '))
    numero02=float(input('Ingrese sumando 2: '))
    return numero01,numero02

def suma(numero01,numero02):
    return numero01+numero02

num1,num2 = ingresoNumeros()

print(f"{num1}+ {num2} = {num1+num2}")