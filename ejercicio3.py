'''Se desea evaluar que red social están usando con más frecuencia los jóvenes Instagram o TikTok, para esto se tomo una muestra de 100 jóvenes entre 15 y 21 años. Se les preguntaráque red social prefieren, su edad y si tienen pareja o no. Desarrolle un algoritmo que permitasaber:• Red social más utilizada• Promedio de edad de usuarios de Instagram y TikTok• Cuantos jóvenes que usan TikTok están en pareja.o Deberá crear un algoritmo en pseudocódigo que de solución a este problema.'''


personas = 5
personasEncuestadas=5
acumInstagram = 0
acumTiktok = 0
totalEdad = 0
tiktokPareja = 0
while personas > 0:
    print("1) INSTAGRAM")
    print("2) TIKTOK")
    while True:
        try:
            redSocial = int(input("¿Que red social prefieres?: "))
            if redSocial == 1 :
                acumInstagram += 1
                break
            elif redSocial == 2:
                acumTiktok += 1
                break
            else:
                print("Debes elegir 1 o 2")
        except:
            print("Debes ingresar un valor numérico.")
    while True:
        try:
            edad = int(input("¿Que edad tienes?: "))
            if edad > 15 and edad < 21:
                totalEdad += edad
                break
            else:
                print("Ingrese una edad válida entre 15 y 21 años.")
        except:
            print("Debe ingresar un valor numérico.")
    while True:
        print("1) SI TENGO PAREJA")
        print("2) NO TENGO PAREJA")
        try:
            pareja = int(input("¿Tienes pareja?:"))
            if pareja == 1 and redSocial == 2:
                tiktokPareja += 1
                break
            if pareja == 1 or pareja ==2:
                break
            else:
                print("Debes elegir 1 o 2")
        except:
            print("Debe ingresar un valor numérico")
    personas -= 1
if personas == 0:
    if acumInstagram > acumTiktok:
        print("La red social más utilizada es INSTAGRAM")
    elif acumTiktok > acumInstagram:
        print("La red social más utilizada es TIKTOK")
    else:
        print("Los usuarios prefiere ambas redes sociales como las más utilizadas")
    
    print(f"El promedio de las edaddes de las personas encuestadas: {totalEdad/personasEncuestadas}")
    print(f"Hay {tiktokPareja} personas que utilizan tiktok y tienen pareja")