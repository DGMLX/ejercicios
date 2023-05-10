'''Se desea competir con el pc en un juego de cara y sello. Tienes 3 oportunidades: El usuario elige su opción y el programa saca al azar una de las dos opciones, si le “achuntas” ganas 50 puntos y si pierdes te descuenta 25. Si al finalizar sus tres oportunidades suma 150 puntos debe decir “IDOLO”, si no, “SIGA PARTICIPANDO”'''

import random

oportunidades=3
puntos = 0
while oportunidades>0:
    print("1) CARA")
    print("2) SELLO")
    while True:
        try:
            valorJugada = int(input("Ingrese una opción: "))
            if valorJugada == 1 or valorJugada == 2:
                break
            else:
                print("Debes ingresar 1 o 2")
        except:
            print("Debe ingresar un valor Numérico.")
    valorAzar = random.randint(1,2)
    if valorJugada == valorAzar:
        print("ACERTASTE")
        puntos += 50
    if valorJugada != valorAzar:
        print("NO ACERTASTE")
        puntos -= 25
    oportunidades -= 1
if puntos == 150:
    print(f"IDOLO, OBTUVISTE {puntos} PUNTOS")
else:
    print(f"PERDEDOR, OBTUVISTE {puntos} PUNTOS")    