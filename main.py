import math
from OperacionesAritmeticas import OperacionesAritmeticas

if __name__ == '__main__':
    operacion = OperacionesAritmeticas()
    num1,num2 =operacion.ingresoNumeros()
    print(f"{num1}+ {num2} = {num1+num2}")