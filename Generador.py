#!/usr/bin/env python3
import string
from datetime import datetime
import argparse

caracteres_texto= string.ascii_letters + string.digits + string.punctuation

caracteres = []
palabra = []


def ingresar(valor):
    global palabra, salida
    estado = True
    for item in palabra:
        if valor == item:
            estado = False
    
    if estado:
        palabra.append(valor)

def mostrar_tiempo():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return "Tiempo = "+current_time


parser = argparse.ArgumentParser(description='Herramienta de Fuzzing y Crawler', add_help=True)
parser.add_argument('-l', '--largo', help='Largo máximo de la cadena', type =str, required=True)
args = parser.parse_args()


inicio=mostrar_tiempo()

f = open("diccionario.txt", "w")
for puntero in caracteres_texto:
    print(puntero)
    caracteres.append(puntero)
    palabra.append(puntero)
    f.write(puntero+"\n")

while True:
    salida=palabra.pop(0)
    
       
    if (len(salida)+1)>int(args.largo):
        break
    
    for caracter in caracteres:
        ingreso = salida+""+caracter
        f.write(ingreso+"\n")
        print(ingreso)
        ingresar(ingreso)
    
fin=mostrar_tiempo()

print(inicio)
print(fin)
