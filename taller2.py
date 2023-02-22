#1. Campus requiere administrar algunos datos de sus Campers
#como por ejemplo, la creación, eliminación o búsqueda de los
#developers, entre otros, por tal razón, ha solicitado el diseño de
#un programa que cuente con el siguiente menú como panel de
#control:
import os
clear=lambda: os.system("clear")
clear()

artemis =[]
sputnik = []

def crear_A():
    artemis.extend(['golden', 'pirlo', 'ronaldo', 'maradona'])

    print(f'[!] Creado exitosamente. {artemis}')
    print('[1] Si\n[2] No')
    s = int(input('[?] Vuelves al menu? : '))
    if s == 1:
        start()
    else:
        exit()

def listar_A():
    print(f'{artemis}\n')
    print('[1] Si\n[2] No')
    s = int(input('[?] Vuelves al menu? : '))
    if s == 1:
        start()
    else:
        exit()

def agregar_A():
    x = input('[?] Ingrese el nombre del camper que agregaras: ')
    artemis.append(x)
    print(f'[!] Agregado exitosamente. {artemis}')
    print('[1] Si\n[2] No')
    s = int(input('[?] Vuelves al menu? : '))
    if s == 1:
        start()
    else:
        exit()

def eliminar_A():
    x = int(input('[?] Ingrese el id del camper que desease eliminar: '))
    artemis.pop(x)
    print(f'[!] Eliminado exitosamente {artemis}')
    print('[1] Si\n[2] No')
    s = int(input('[?] Vuelves al menu? : '))
    if s == 1:
        start()
    else:
        exit()

def ordenar_A():
    artemis.sort()
    print(f'[!] Lista ordenada {artemis}')
    print('[1] Si\n[2] No')
    s = int(input('[?] Vuelves al menu? : '))
    if s == 1:
        start()
    else:
        exit()

def buscar_A():
    x = int(input('[?] Nombre a buscar por ID: '))
    print('[! Nombre encontrado]',artemis[x])
    print('[1] Si\n[2] No')
    s = int(input('[?] Vuelves al menu? : '))
    if s == 1:
        start()
    else:
        exit()

#sputnik

def crear_S():
    sputnik.extend(['valentina', 'valeria', 'freddy', 'david'])

    print(f'[!] Creado exitosamente. {sputnik}')
    print('[1] Si\n[2] No')
    s = int(input('[?] Vuelves al menu? : '))
    if s == 1:
        start()
    else:
        exit()

def listar_S():
    print(f'{sputnik}\n')
    print('[1] Si\n[2] No')
    s = int(input('[?] Vuelves al menu? : '))
    if s == 1:
        start()
    else:
        exit()

def agregar_S():
    x = input('[?] Ingrese el nombre del camper que agregaras: ')
    sputnik.append(x)
    print(f'[!] Agregado exitosamente. {sputnik}')
    print('[1] Si\n[2] No')
    s = int(input('[?] Vuelves al menu? : '))
    if s == 1:
        start()
    else:
        exit()

def eliminar_S():
    x = int(input('[?] Ingrese el id del camper que desease eliminar: '))
    sputnik.pop(x)
    print(f'[!] Eliminado exitosamente {sputnik}')
    print('[1] Si\n[2] No')
    s = int(input('[?] Vuelves al menu? : '))
    if s == 1:
        start()
    else:
        exit()

def ordenar_S():
    sputnik.sort()
    print(f'[!] Lista ordenada {sputnik}')
    print('[1] Si\n[2] No')
    s = int(input('[?] Vuelves al menu? : '))
    if s == 1:
        start()
    else:
        exit()

def buscar_S():
    x = int(input('[?] Nombre a buscar por ID: '))
    print('[! Nombre encontrado]',sputnik[x])
    print('[1] Si\n[2] No')
    s = int(input('[?] Vuelves al menu? : '))
    if s == 1:
        start()
    else:
        exit()


def start():
    clear()
    print("[!] ----------------- Menu ----------------- ")
    print("[!] 1.CREAR GRUPO ARTEMIS:\n[!] 1.1 LISTAR CAMPERS DE ARTEMIS\n[!] 1.2 AGREGAR CAMPERS A ARTEMIS\n[!] 1.3 ELIMINAR CAMPERS DE ARTEMIS\n[!] 1.4 ORDENAR ALFABETICAMENTE EN LISTA DE ARTEMIS\n[!] 1.5 BUSCAR CAMPER EN LISTA DE ARTEMIS \n[!] 2 CREAR GRUPO SPUTNIK\n[!] 2.1 LISTAR CAMPERS DE SPUTNIK:\n[!] 2.2 AGREGAR CAMPERS A SPUTNIK\n[!] 2.3 ELIMINAR CAMPERS DE SPUTNIK\n[!] 2.4 ORDENAR ALFABETICAMENTE EN LISTA DE SPUTNIK\n[!] 2.5 BUSCAR CAMPER EN LISTA DE SPUTNIK")
    print("[!] ---------------------------------------- ")
    m = float(input('\n[>] Digite su opcion: '))
    menu(m)


def menu(x):
    if x == 1:
        crear_A()

    elif x == 1.1:
        listar_A()

    elif x == 1.2:
        agregar_A()

    elif x == 1.3:
        eliminar_A()

    elif x == 1.4:
        ordenar_A()

    elif x == 1.5:
        buscar_A()

    elif x == 2:
        crear_S()

    elif x == 2.1:
        listar_S()

    elif x == 2.2:
        agregar_S()

    elif x == 2.3:
        eliminar_S()

    elif x == 2.4:
        ordenar_S()

    elif x == 2.5:
        buscar_S()

start()

#2. N atletas han pasado a finales en salto triple en los juegos
#olímpicos de 2022.

#Diseñe un programa que pida por teclado los nombres de cada
#atleta finalista y a su vez, sus marcas del salto en metros.

#Informar el nombre de la atleta campeona que se quede
#con la medalla de oro y si rompió récord, reportar el pago que
#será de 500 millones. El récord esta en 15,50 metros.

print('Campeones')

atleta1 = input('[!] Ingrese su nombre: ')
atleta1_m = float(input('[!] Ingrese su record: '))


atleta2 = input('[!] Ingrese su nombre: ')
atleta2_m = float(input('[!] Ingrese su record: '))


atleta3 = input('[!] Ingrese su nombre: ')
atleta3_m = float(input('[!] Ingrese su record: '))

if atleta1_m == 15.50:
    print(f'[!] Ganaste 500 millones {atleta1}')
elif atleta2_m == 15.50:
    print(f'[!] Ganaste 500 millones {atleta2}')
elif atleta3_m == 15.50:
    print(f'[!] Ganaste 500 millones {atleta3}')

#3. En pocos días comienza la vuelta a España y la federación
#colombiana de ciclismo, como incentivo ha determinado pagar
#un valor adicional. El programa pedirá por teclado el sueldo
#básico por kilometro recorrido, el número de kilómetros
#recorridos durante toda la vuelta, numero de kilómetros
#recorridos con la camiseta de líder.
#Calcular el valor a pagar total, si se sabe que si recorre en la
#bici más de 1800 kilómetros con la camiseta de líder, esos
#kilómetros se consideran especiales y tendrán un recargo de
#25%.
#El total de kilómetros por recorrer durante toda la vuelta serán
#3.277 kilómetros,el ganador de la vuelta a España recibirá 700
#millones de pesos.    

esp=2000
tope=4000
pagoganador=900
pagoesp=0
pago=0


while(c!=1):
    sueldo=float(input("dijite su sueldo basico por kilometro recorrido: "))
    numkm1=float(input("\nDijite el numero de kilometroa recorridos durante tola la vuelta: "))
    numkmlider=float(input("\nDijite el numero de kilometros recooridos con la camisa de lider; "))

    #asignacion= Federacion (sueldo,numkm1,numkmlider)
    if(numkmlider>esp):
        pagoesp=(numkmlider.esp) *1,25
    
    if(numkm1>tope):
        pago=pagoganador
        print(" A ganado la vuelta españa")

    print(f"==== pago total ====\n")    
    f"pago kilometros especiales {pagoesp}\n"
    f"pago kilometros normales {sueldo*numkm1}\n"
    f"pago ganador {pago}\n"
    f"======Total :{pagoesp+(sueldo+numkm1)+pago}"

    c=int (input("1.salir\n 2. continuar\n"))



#4. Una empresa tiene 500 almacenes. Cada almacén debe
#reportar el nombre y 5 registros c/u, contiene el tipo de articulo
#y el número de unidades vendidas de ese artículo.

#Haga un programa en Python para determinar cuál fue el
#almacén que mas vendió, cual fue el articulo más vendido de
#ese almacén y cual el más vendido en general.

import random
import json

Almacen = []
lista= []
articulo = []
for i in range (3):
    lista.__setitem__("tipo", f"pastac {i+1}")
    for x in range (5):
        data= [1,2,3,4,5]
        articulo.append(random.choice(data))
    lista.__setitem__("articulo",articulo)
    Almacen.append({"nombre": f"Almacen{i+1}", "registro":lista})
    print(json.dump(Almacen,ident=4))