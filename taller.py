# 1. Qué operadores utiliza Python :

print(f'.Division Modular= a//b') 

a=7
B=2

print(f'exponenciacion')

num1 = 2
num2 = -5
num3 = 0
num4 = 1.025
num5 = 0.5

print(num1,'^12=', num1**12)
print(num2,'^4=', num2**4)
print(num3,'^9999=', num3**9999)
print(num4,'^-3=', num4**-3)
print(num5,'^8=', num5**8)

print(f'Division Que Retorne en entero')

num1 = 12
num2 = 5
num3 = num1 // num2

print("División entera de", num1, "en", num2, "=", num3)
# Salida: División entera de 12 en 5 = 2

#2 En la jerarquía de operadores, cuáles son los que más
   #prioridad tienen cuando el intérprete de Python los evalúa?

print(f"primero:operaciones entre parentesis = ()\n" "segundo :Potencia = **\n" "tercero multiplicaion y division, modulo o residuo ,division entera = *,/,% // \n" "cuart suma y resta = \n" "Quinta:Operadores relaciones = <, <=, >= ,!=, == \n" "Sexta:Operador logico AND = And\n" " Septima:Operador logico OR = Or")

#3. Si hay operadores de igual precedencia, en qué orden se
#ejecutan?

#A. De izquierda a derecha
#B. De derecha a izquierda

print(f"A.De Izquierda a derecha {8}//{7}*{5} = {8//7*5}")
print(f"B.De derecha a izquierda {5}*{7}//{8} = {5*7//8}")

#4. Que son las expresiones regulares en Python?

print("Las expresiones son combinaciones de constantes, variables, simbolos y parentesis, que arrojan un valor tal y como se conoces en la notacion tradicional del las matematicas. \n como las siguientes:re.search, re.findall,^,$,\s,*,+,?,[], [^],[a-z],()")

#5. Enumere 5 tipos de datos en Python y suministre un valor de
    #ejemplo de cada uno.
num=1
num2=2.1
string = "hola mundo"
pequeño = False
lista = [1,2,3]

print(f"Tipos de Datos: \n Numero Entero: {num1}\n Float: {num2}\n string: {string}\n lista:{lista}\n Booleano: {pequeño}")

#6. En sus propias palabras, qué son las funciones
#preconstruidas y proporcione 2 ejemplos.

mayor=max(55,35,25,43)
texto=len("Hola Mundo")

print(f"las funciones pre construidas son incluidas en las librerias pyhton nativamente. \n Ejemplos: \n la funcion max, revisa cual es el numero mayor dado en una lista: {mayor}\n la funcion len, revisa los caracteres de un texto: {texto}")

#7. Cuál es la diferencia entre un condicional simple y un
#condicional compuesto?

print(f"una estructura de control que ejecuta un conjunto de líneas de código si es cierta una expresión booleana, condicional compuesta tenemos entradas, salidas, operaciones, tanto por la rama del verdadero como por la rama del falso.")

sueldo=int(input("Ingrese cual es su sueldo:"))
if sueldo>3000:
    print("Esta persona debe abonar impuestos")

num1=int(input("Ingrese primer valor:"))
num2=int(input("ingrese segundo valor:"))
print("El valor mayor es")
if num1>num2:
    print(num1)
else:
    print(num2)

#8.Escriba un bloque cualquiera de código en Python en donde
#utilice 2 condicionales (if) anidados.

nombre = ("Joan Sebastian ") 
apellidos = ("Delgado Ortega")
estatura = ("1.75")

if nombre == ("Joan") :
    print ("Tu nombre es Joan")
    if apellidos == "Delgado Ortega":
        print("Y tus apellidos son Delgado Ortega")
    if estatura == 1.75:
        print ("y tu estatura es 1.75")

#9. Construya un algoritmo en Python, que permita ingresar la
#información de un empleado e imprima el nombre, los
#apellidos y la antigüedad. Los datos que se deben solicitar
#son los siguientes:
#*Nombre * Teléfono *Año de ingreso a la empresa
#*Apellidos *Edad.

empleado =input("dijite su nombre")
apellido =input("dijite sus apellidos")
edad =input ("dijite su edad")
telefono =input("dijite su telefono") 
fecha =input("dijite la fecha de ingreso")

print (f"hola {empleado} {apellido}, tu edad es {edad} , su telefono es {telefono} , fecha {fecha}bienvenido a nuestra empresa de desarrollo de sofware, ahora eres un camper mas.. ")

#10. En su casa le solicitan que realice un algoritmo en Python,
#que permita calcular el valor a pagar por concepto de
#energía eléctrica. Los datos que se conocen son los
#siguientes:
#- Mes de consumo - Valor kw
#-Total kw consumido en el mes - estrato

print('[!] extrato calculator omg\n')
def calcular():
    kw = 0
estrato = int(input('[!] Ingrese su estrato: '))
mes = int(input('[!] Ingrese el mes de consumo: '))
        #kw = int(input('Ingrese el valor de kw por dia: '))
total = int(input('[!] total kw consumidos en el mes: '))
if estrato == 1:
            kw = 297
elif estrato == 2:
            kw = 346
elif estrato == 3:
            kw = 588
elif estrato == 4:
            kw = 719
else:
            kw = 862
if mes == 1:
            h = 'enero'
elif mes == 2:
            h = 'febrero'
elif mes == 3:
            h = 'marzo'
elif mes == 4:
            h = 'abril'
elif mes == 5:
            h = 'mayo'
elif mes == 6:
            h = 'junio'
elif mes == 7:
            h = 'julio'
elif mes == 8:
            h = 'agosto'
elif mes == 9:
            h = 'septiembre'
elif mes == 10:
            h = 'octubre'
elif mes == 11:
            h = 'noviembre'
else: 
            h = 'diciembre'    
    
t = total * kw

print(f'\n[!] El valor total del mes {h.upper()} es :{t}')
    
calcular()


