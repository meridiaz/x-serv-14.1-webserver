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

def calcular(func, op1, op2):
	if func not in operations:
	    return "Introduce una operacion: sumar, restar, multiplicar o dividir"
	try:
	    op1 =  float(op1)
	    op2 =  float(op2)
	except ValueError:
	    return "Introduce un operando valido tipo decimal"
	try:
	    result = operations[func](op1, op2)
	except ZeroDivisionError:
	    return "Para realizar una division el divisor debe ser distinto de 0"
	return "El resultado es: "+ str(result)

	
