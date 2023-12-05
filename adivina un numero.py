import random
def adivina_el_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 0
    intentosM= 5
    
    while intentos < intentosM:
        
        numUsuario = int(input("adivine el numero entre 1 y 20"))
        
             if 1 <= numUsuario <= 20:
                 
                if numUsuario == numero_secreto:
                    print("adivinaste")
                    break
                else:
                    print("incorrecto, intenta de nuevo")
            else:
                print("ingrese un numero entre 1 y 20")
                
    intentos += 1
    
    if intentos == intentosM:
        print("acabaste todos tus intentos, el numero secreto es" +numero_secreto)