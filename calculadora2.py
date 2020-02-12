#!/usr//bin/python3

import sys
import operator

#check
operations = {
    "sumar": operator.add,
    "restar": operator.sub,
    "multiplicar": operator.mul,
    "dividir": operator.truediv
}

if len(sys.argv) != 4:
    print("Introduce una operacion y dos operandos")
    sys.exit(1)

operation = sys.argv[1]
if operation not in operations:
    print("Introduce una operacion: add, sub, mul o div")
    sys.exit(1)
try:
    op1 =  float(sys.argv[2])
    op2 =  float(sys.argv[3])
except ValueError:
    print("Introduce un operando valido tipo decimal")
    sys.exit(1)

try:
    result = operations[operation](op1, op2)
except ZeroDivisionError:
    print("Para realizar una division el divisor debe ser distinto de 0")
    sys.exit(1)


print("El resultado es: "+ str(result))
