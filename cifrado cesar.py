def cifrado(palabra, desplazamiento):
    resultado = ""
    for letra in palabra:
        if letra.isalpha():
            nueva_letra = chr((ord(letra) - ord('a' if letra.islower() else 'A') + desplazamiento) %26 + ord('a' if letra.islower() else 'A'))
            resultado += nueva_letra
        else:
            resultado += letra
    return resultado

palabra_original = input("ingrese una palabra para cifrar: ")
desplazamiento = int(input("ingrese el desplazamiento: "))

palabra_cifrada = cifrado(palabra_original,desplazamiento)

print ("palabra original: " +palabra_original)
print ("palabra_cifrada: " +palabra_cifrada)