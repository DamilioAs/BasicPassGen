#GENERAR CONTRASEÑA

import random
import string 
import os

lista = []

def generar_contra():
    
    contra = ""
    n_c = int(input("Ingrese el número de letras: "))
    n_n = int(input("Ingrese el número de numeros: "))
    n_cespe = int(input("Ingrese el número de caracteres especiales: "))

    total = n_c + n_n + n_cespe
    caracteres = string.ascii_letters + string.punctuation + string.digits

    for i in range(total):
        contra += random.choice(caracteres)

    lista.append(contra)
    print(f"La contraseña es:", contra)

    ruta = os.path.join(os.path.dirname(__file__), "resgitro.txt")
    with open(ruta, "a", encoding="utf-8") as file:
        file.write(f"Se registra la contraseña: {contra}\n")
 
def mostrar_contraseñas(lista):

    if len(lista) > 0:
        print("\nCONTRASEÑAS GENERADAS")
        for i in lista:
            print(i)
        
    else: 
        print("\nNo hay elementos")

while True:
    print("\nGENERADOR DE CONTRASEÑAS\n1.- Generar contraseña.\n2.- Mostrar contraseñas\n3.- Salir\n")
    try:
        op = int(input("Ingrese la opción: "))
    except Exception as e:
        print("Valor incorrecto")
        op = int(input("Ingrese la opción de nuevo: "))

    match op:
        case 1:
            generar_contra()
        case 2:
            mostrar_contraseñas(lista)
        case 3:
            print("Programa cerrado")
        case _:
            print("Opcón no valida")