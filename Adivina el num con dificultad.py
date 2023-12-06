import random

def adivina_el_numero_con_vidas():
    print( "Bienvenido a 'adivina el numero' con dos niveles de difilcutad." )
    print("1. Facil (numeros del 1 al 10)")
    print ("2. Dificil (numeros del 1 al 20)")
    nivel = input("Elige un nivel (1. para Facil y 2. para Dificil): ")
    if nivel == '1':
        limite_superior = 10
    elif nivel == '2':
        limite_superior = 20
    else:
        print("seleccion no valida.Elige 1 para facil y 2 para dificil.")
        return 
    numero_objetivo= randon.randint(1, limite_superior)
    vidas = 3
    print("piensa un numero del 1 al {limite_superior} e intenta adivinarlo")
    while vidas > 0:
        intento= input("ingresa tu adivinanza: ")
        try:
            intento = int(intento)
            if intento < 1 or intento > limite_superior:
                print("Ingresa un numero entre el 1 al {limite_superior}")
                continue
        except ValueError:
                    print("ingresa un numero valido entre el 1 al {limite_superior}")
                    continue
             if intento == numero_objetivo: 
                 print("Adivinaste el numero {numero_objetivo}.")
                 break
            elif intento < numero_objetivo:
                print("el numero es mayor. Te quedan {} vidas.".format(vidas -1)) 
            else:
                print("el numero es menor. Te quedan {} vidas.".format(vidas -1)) 
            vidas-= 1
            if vidas == 0:
                print("te quedaste sin vidas el numero objetivo era {numero_objetivo}.")
                
adivina_el_numero_con_vidas()

