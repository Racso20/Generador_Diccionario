#!/usr/bin/env python3
import string
from datetime import datetime
import argparse
from pwn import *
import signal
import sys

caracteres_texto= string.ascii_letters + string.digits + string.punctuation

caracteres = []
palabras = []
palabra_ciclica = []

color = {}
color["rojo"] = "\033[1;31m"
color["verde"] = "\033[1;32m"
color["amarillo"] = "\033[1;33m"
color["azul"] = "\033[1;34m"
color["magenta"] = "\033[1;35m"
color["cyan"] = "\033[1;36m"
color["blanco"] = "\033[1;37m"
color["reset"] = "\033[0m"

def def_handler(sig, frame):
    global color
    print(color["rojo"]+"\n\n[x] Saliendo...\n"+color["reset"])
    sys.exit(1)

    
signal.signal(signal.SIGINT, def_handler)
    
    
def mostrar_tiempo():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return "Tiempo = "+current_time

    
def diccionario():

    for puntero in caracteres_texto:
        palabras.append(puntero)
    for i in range(10):
        palabra_ciclica.append("a")
        
    estado = False
    i=0
    for palabra in palabras:
        for caracter in caracteres_texto:
            largo=len(palabra+caracter)
            if int(args.largo)<largo:
                estado = True
                break
            i+=1
            palabra_ciclica[i%10]=palabra+caracter
            palabras.append(palabra+caracter)
            p3.status(f"{palabra_ciclica}")
            p2.status(f"{'{:,.3f}'.format(i*100/cantidad).replace('.', ',')}%")
            p1.status(f"Vamos en {'{:,.0f}'.format(i).replace(',', '.')} palabras que tienen un largo de {largo}")   
            
        if estado:
            break
            
    f = open("diccionario.txt", "w")
    for salida in palabras:
        f.write(salida+"\n")


parser = argparse.ArgumentParser(description='Herramienta de Fuzzing y Crawler', add_help=True)
parser.add_argument('-l', '--largo', help='Largo máximo de la cadena', type =str, required=True)
args = parser.parse_args()

if __name__ == "__main__":
    inicio=mostrar_tiempo()
    
    largo=0
    cantidad=int(1-(len(caracteres_texto)**(int(args.largo)+1))/(1-len(caracteres_texto)))-1
    
    p1 = log.progress(f"Se crearán {'{:,.0f}'.format(cantidad).replace(',', '.')} de palabras")
    p2 = log.progress(f"Porcentaje")
    p3 = log.progress(f"Ultimas Palabras Ingresadas")
    diccionario()
    fin=mostrar_tiempo()
    
    print(inicio)
    print(fin)
