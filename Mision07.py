# Autor: David Isaí López Jaimes      A01748363
# Programa que tiene un menú que dependiendo la opción hace divisiones con unmetodo de resta o encuentra el numero mayor entre todos los numeros que teclee el usuario


def dividir(dividendo, divisor):  # Función que divide con un metodo de resta para saber el cociente y el residuo
    cociente = 0
    resto = dividendo
    while resto >= divisor:
        resto -= divisor
        cociente += 1
    print("%d / %d = %d, sobra %d" % (dividendo, divisor, cociente, resto))


def encontrarMayor():    # Función que encuentra el mayor de n numeros tecleados por el usuario
    numero = int(input("Teclea un numero [-1 para salir]: "))
    mayor = 0
    if numero == -1:   # Condicional para salir
        print("No hay valor mayor")
    else:
        while numero != -1:    # Ciclo que pide numeros
            numero = int(input("Teclea un numero [-1 para salir]: "))
            if numero > mayor:
                mayor = numero
        print("El mayor es: ", mayor)


def main():   # Función principal que contiene el menú con formato
    print("Misión 07. Ciclos While")
    print("Autor: David Isaí López Jaimes")
    print("Matrícula: A01748363")
    print("1. Calcular divisiones")
    print("2. Encontrar el mayor")
    print("3. Salir")
    opcion = int(input("Teclea tu opción: "))
    while opcion != 3:
        if opcion == 1:
            print("\nCalculando divisiones")
            dividendo = int(input("Dividendo: "))
            divisor = int(input("Divisor: "))
            dividir(dividendo, divisor)
        elif opcion == 2:
            print("\nTeclea una serie de numeros para encontrar el mayor.")
            encontrarMayor()
        print("\n\nMisión 07. Ciclos While")
        print("Autor: David Isaí López Jaimes")
        print("Matrícula: A01748363")
        print("1. Calcular divisiones")
        print("2. Encontrar el mayor")
        print("3. Salir")
        opcion = int(input("Teclea tu opción: "))
    print("\nGracias por usar este programa, regresa pronto.")


main()  #Llama a la función