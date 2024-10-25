if __name__ =='__main__':
    #tipos de datos basicos
    entero =42
    decimal = 3.14
    complejo = 2+3j
    booleano = True
    cadena = "hola,Python!"
    binario = bytes ([50,100,150])

    print("tipoa basicos:")
    print("Enteros:", entero)
    print("Decimal:", decimal)
    print("Complejo:", complejo)
    print("Booleano:", booleano)
    print("Cadena:", cadena)
    print("Binario:", binario,"\n")
 #Estrucura de datos  avanzadas
    lista = [1,2,3,"cuatro"]
    tupla = (5,6,7,"ocho")
    conjunto = {9,10,"once","doce"}
    diccionario = {"clave1": "valor1","clave2":20}


    print("ESTRUCTURAS AVANZADAS:")
    print("Lista:",lista)
    print("Tupla:",tupla)
    print("Conjuto:",conjunto)
    print("Diccionario:",diccionario,"\n")
#otro tiposespeciales
    nulo = None                        #nonetype
    rango = range(3)                      #range (equivale  0


    print("Tipos especiales:")
    print("Nulo:", nulo)
    print("Rango:",list(rango))       #convertimos a la lista


    #ejemplo de interacion con el tipo range
    print("\nIterando sobre el rango:")
    #esta es la manera mas corta de reorrer un rango
    for numero in rango:
        print(numero)


