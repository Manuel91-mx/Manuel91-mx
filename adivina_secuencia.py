import random #con este comando, agregamos la libreria de random, el cual nos arojara numeros aleatorios cada que iniciemos el programa.

print("Vienvenido... VIENVENIDO!!!")
print("Acaso estas tratando de adivinar el numero....????")
print("Jajajajajajajajajaj, intentalo, pero te aseguro que sera dificil...")
print("Estas listo???")
print("Empecemos.")

numero_pe = random.randint(1, 10) # determinamos que el numero pensado, sera el numero random dado por la libreria, que va del rango de 1 a 10...

numero_ad = int(input(
    "¿Que numero estoy pensando?: "))  # De esta foma, estas agregando una entrada a una variable, y a parte, la haces de forma entero.

if numero_ad != numero_pe:
    print("Ja, sigue intentando... te dije que era dificil")
    print("El numero ganador era: {}".format(numero_pe))

if numero_ad == numero_pe:
    print("Pero como es esto posible...???")
    print("Me has destruido...")
    print("NOOOOOOOOO!!!!!")
