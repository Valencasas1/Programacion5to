import.random
palabras=["PERRO", "perro", "CASA", "casa"]
palabra= random.choice(palabras)
intentos= 7
letras_adivinadas= []
while intentos > 0:
    palabra_adivinada= ""
    for letra in palabra:
        if letra in letras_adivinadas:
            palabra_adivinada += letra
    else:
            palabra_adivinada += "_"
    if palabra_adivinada == palabra:
        print ("Ganaste la palabra era: ",palabra)
    break
print ("palabra: ", palabra_adivinada)
print ("Intentos restantes: ", intentos)
letra_usuario = input("Ingresa una letra: ").lower()
if len(letra_usuario)==1 and letra_usuario.isalpha():
    if letra_usuario in letras_adivinadas:
        print("ya intentaste esa letra utiliza otra")
    elif letra_usuario in palabra:
        letras_adivinadas.append(letra_usuario)
        print("correcto esa letra esta en la palabra")
    else:
        letras_adivinadas.append(letra_usuario)
        intentos -= 1
        print("incorrecto te quedan ", intentos, "intentos.")
else:
        print("Ingresa una letra valida.")
if intentos == 0:
    print("Perdiste la palabra era: ", palabra)