#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse, time, os, random, hashlib
from heapq import nlargest

parser = argparse.ArgumentParser()
parser.add_argument("-ka", "--kasiski", help="Algoritmo de Criptoanalisis Kasiski", action="store_true")
parser.add_argument("-en", "--enigma", help="Maquina Enigma", action="store_true")
parser.add_argument("-a", "--ayuda", help="ayuda", action="store_true")
parser.add_argument("-f", "--file", help="Nombre del archivo a cifrar", default=os.getcwd(), required=False)
parser.add_argument("-k", "--key", help="archivo que contiene la clave para cifrar")
parser.add_argument("-c", "--cifrado", help="cifrar ", action="store_true")
parser.add_argument("-d", "--descifrado", help="Descifrar", action="store_true")
parser.add_argument("-p", "--parametros", help="parametros", default=os.getcwd(), required=False)
args = parser.parse_args()

alfabetoEspañol = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S",
                   "T", "U", "V", "W", "X", "Y", "Z"]  # , 'Ü', '«', 'Ï', ']', 'À', '3', 'Ù']
alfabetoIngles = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                  "U", "V", "W", "X", "Y", "Z"]  # ,'[', '%', '_', ']']#, 'Ü', '«', 'Ï', ']', 'À', '3', 'Ù']
estadisticaEspañol = ["E", "A", "O", "S", "I", "N", "R", "D", "T", "C", "L", "U", "M", "P", "G", "B", "F", "V", "Y",
                      "Q", "H", "Z", "J", "X", "W", "K", "Ñ"]
estadisticaIngles = ["E", "T", "A", "O", "S", "I", "N", "R", "D", "C", "L", "U", "M", "P", "G", "B", "F", "V", "Y", "Q",
                     "H", "Z", "J", "X", "W", "K"]

def conteo(abc, msg):
    conteo = {}
    for i in range(len(abc)):
        conteo[abc[i]] = msg.count(abc[i])
    most_rep = nlargest(len(abc), conteo, key=conteo.get)
    # print("Las letras que mas se repiten son:")
    #  for v in most_rep:
    #     print(v, '>', conteo.get(v), "veces")
    return most_rep


def mcd(numeros):
    # Calcula el maximo común divisor
    # * Numeros: es una lista de enteros
    mcd = 1
    numeros.sort()  # ordena la lista de menor a mayor
    for i in range(2, numeros[-1] + 1):  # recorre hasta el numero mayor de la lista (el último)
        if esDivisible(i, numeros):
            mcd = i
    return mcd


def esDivisible(numero, lista):
    # Return True:
    #	si el numero no deja resto
    # con todos los números de la lista
    divisible = True
    for i in lista:
        if not i % numero == 0:
            divisible = False
            break;
    return divisible


if args.kasiski == False and args.enigma == False:
    print("""
            -----------------UNIVERSIDAD DE AUTONOMA DE OCCIDENTE----------------------
            ------------------------Algoritmos Criptograficos--------------------------
            |                                                                         |
    	    |                							      |
            |     Sintaxis: ./proyectoFinal <algoritmo>                               |
            |                                                                         |
            |     -ka      :Criptoanalisis Kasiski                                    |
            |     -en    :Algoritmo de Codigo Enigma                                  |
    	    |                     						      |
    	    |       consultar ayuda de un algoritmo determinado:                      |
    	    |       sintaxis: ./proyectoFinal.py < algoritmo > 	-a                    |
    	    |									      |
    	    |   Firmas Digitales.		                                      |
    	    |   Profesor: Msc.Siler Amador Donado.			              |
    	    |   Semestre 2019-1.	                                              |
    	    |   Elaborado por: Andres F Flor     andres.flor@uao.edu.co	              |
    	    |		   Juan Diego Escobar        juan_die.escobar@uao.edu.co      |
    	    |									      |   
    	    |   El codigo fuente,El Documento de Word, los archivos de texto          |
    	    |   utilizados ,el video y las claves de  cada algoritmo se encuentra     |
    	    |	en el siguiente repositorio:		                              |
    	    |   https://drive.google.com/open?id=1gWgExnQ-7p3S5gWOPlx7BGHh601NkXyt    |
    	    |									      |
    	    |   El video De Youtube lo encontratas en el siguiente enlace:	      |
    	    |   https://drive.google.com/open?id=1gWgExnQ-7p3S5gWOPlx7BGHh601NkXyt    |
    	    |									      |
    	    |-------------------------------------------------------------------------|
            """)

if args.kasiski == True and args.ayuda == True:
    print("""
            ----------------------------UNIVERSIDAD AUTONOMA DE OCCIDENTE------------------------
            ---------------------------Algortirmo de CriptoAnalisis Kasiski----------------------
            |                                                                         		|
    	    |                							  		|
            |    Sintaxis: ./proyectoFinal.py -ka <opcion> -f <ArchivoEntrada>                  |                                                                     		
            |      <opcion> :                                                                   |
            |                                                                                   |
            |        -f para indicar el nombre del Archivo de Entrada                           |
            |                                                                                   |
    	    |	  -d para descifrar el archivo <ArchivoEntrada>            		        |
    	    |                                                                                   
            |	  -c para cifrar el archivo <ArchivoEntrada>                                    |								  		
            |	  -k para indicar el nombre del archivo que contiene la Clave para Cifrar       |
            |      <ArchivoEntrada>: nombre del archivo de entrada                     	        |
            |                                                                                   |
    	    |  <ArchivoClave>  : nombre del archivo que contiene la clave          	        |
          									                |
      	    | 											|
    	    |									  		|
    	    |Ejemplo:								  		|
    	    |        Cifrar: ./proyectoFinal -ka -c -f quijote.txt  -k clave.txt|		|

    	    |               CriptoAnalizar: ./proyectoFinal -ka -d -f -quijote.cif  

    	    |  									  		|
    	    |  Elaborado por: Andres Flor          andres.flor@uao.edu.co	  		|
    	    |	          Juan Diego Escobar   juan_die.escobar@uao.edu.co	  		|
	    |   Profesor: Msc.Siler Amador Donado.						|
    	    |-----------------------------------------------------------------------------------|
    	    |-----------------------------------------------------------------------------------|
            """)
if args.kasiski == True and args.cifrado == True:
    # texto
    ti = time.time()

    print("Nombre del archivo a Cifrar  es: ", args.file)
    f = open(args.file, "r", encoding="ISO-8859-1")
    # print("Texto del Documento Cifrado:")
    texto = f.readline()
    texto = texto.upper().strip()
    # print(dato)
    f.close()


    salida = str (args.file)
    salida = salida.replace("txt","cif")
    #print(salida)

    f = open(args.key, "r", encoding="ISO-8859-1")
    clave = f.readline()
    clave = clave.upper().strip()
    f.close()

    J_TXT = []
    for i in range(len(texto)):
        if ord(texto[i].upper()) not in J_TXT:
            J_TXT.append(ord(texto[i].upper()))

    #para incluir las letras de la clave en el alfabeto
    for i in range(len(clave)):
        if ord(clave[i].upper()) not in J_TXT:
            J_TXT.append(ord(clave[i].upper()))

    #Ordernar
    J_TXT.sort()


    alfabeto = []
    for i in J_TXT:
        alfabeto.append(chr(i))


    # texto = ''.join(J_TXT)
    # abc = "".join(alfabeto)
    # d = open("alfabeto.txt", "w")
    # d.write(abc)
    # d.close()
    #

    # print(texto)
    print("La clave con la que vamos a Cifrar es Texto es: ", clave)
    #print(alfabeto)
    #print(len(alfabeto))
    cont = 0

    re = ""
    for i in texto:
        if cont >= len(clave):
            cont = 0
            cont += 1
        else:
            cont += 1
        # C = (m + k) mod alfabeto
        k = alfabeto.index(clave[cont - 1])
        m = alfabeto.index(i)  # texto.index(i)
        # m = (c - k) % len(alfabeto)
        c = (m + k) % len(alfabeto)
        re = re + alfabeto[c]

    # print("m: ", m, "+", "k: ", k, "c: " , c )
    re ="".join(re)
    print("El Archivo cifrado Tiene como Nombre: ", salida)
    d = open(salida, "w",encoding="ISO-8859-1")
    d.write(re)
    d.close()

    tf = time.time()
    tff = tf - ti
    print("el tiempo de ejecucion de Vigenere fue de: " , tff)

# INICIA KASISKI
if args.kasiski == True and args.descifrado == True:

    flagHash = 0
    salida1 = ""
    salida2 = ""

    # tomamos el tiempo inicial desde que se ejecuta el Algoritmo de Cripto Analisis Kasiski
    # para poder saber cuanto tiempo tardo el algoritmo en Descifrar la clave
    ti = time.time()

    print("Nombre del archivo a Descifrar es: ", args.file)
    f = open(args.file, "r", encoding="ISO-8859-1")
    texto = f.readline()
    texto = texto.upper().replace(" ", "")
    f.close()

    archivo = str(args.file).replace('cif',"txt")

    try:
        # print("Nombre del archivo a Descifrar es: ", args.file)
        f = open(archivo, "r", encoding="ISO-8859-1")
        plano = f.readline()
        plano = plano.upper()
        f.close()
    except OSError as e:
        flagHash = 1
        #print(flagHash)


    # obtener hash del texto Original
    if flagHash == 0:
        hash1 = hashlib.md5(plano.encode("utf-8")).hexdigest()
        #print(hash1)

    # obtener diccionario base a usar(ESPAÑOL o INGLES)
    if texto.upper().find("Ñ") != -1:
        estadistica = estadisticaEspañol
    else:
        estadistica = estadisticaIngles

    # obtener alfabeto base a usar
    J_TXT = []
    for i in range(len(texto)):
        if ord(texto[i].upper()) not in J_TXT:
            J_TXT.append(ord(texto[i].upper()))
    J_TXT.sort()

    alfabeto = []
    for i in J_TXT:
        alfabeto.append(chr(i))

    if flagHash == 1:
         if alfabeto.index("Ñ") > -1:
             valor = alfabeto.index("N")
             #print(valor)
             alfabeto.remove("Ñ")
             alfabeto.insert(valor + 1, "Ñ")


    for i in estadistica:
        if i not in alfabeto:
            estadistica.remove(i)

    #print(alfabeto)
    subCadenas = []
    cadena = ""
    i = 0
    j = 0
    hash = {}
    posicionInicial = 0
    tamañoPalabra = 4

    # Distancia entre grupos
    for contador in range(tamañoPalabra, 8):
        #print(contador)
        while i < len(texto):
            if j < contador:
                cadena = cadena + texto[i]
                j = j + 1
                i = i + 1
            else:
                if cadena not in hash:
                    hash[cadena] = []
                hash[cadena].append(posicionInicial)
                cadena = ""
                j = 0
                posicionInicial = i
        i = 0  # se debe de poner el contador i en 0 para poder volver a iterar
        # el ciclo while y formas palabras de 4,5,6,7,...15 caracteres de logitud

    # Lista para obttener las distancias entre las palabras repetidas#
    restas = []
    for x in hash:
        # print(x)
        longitudes = hash[x]
        # obtengo una lista con todos los valores que perteneces a la clave x ejemplo {"XLE": 20,68,92,115}
        for i in range(len(longitudes) - 1):
            restas.append(longitudes[i + 1] - longitudes[i])

    # quitar repetidos, ordernar
    restas = list(set(restas))
    restas.sort()

    # print(restas)

    hash2 = 0
    # print(alfabeto.index(estadistica[25]))
    # print(hash1)
    # alfabeto = alfabetoEspañol
    # print(alfabeto)
    flag = 0
    while flag == 0:
        salida2 = ""
        salida2 = salida2 + "**********************************" + "\n"
        salida2 = salida2 + "Resumen Kasiski" + "\n" +"\n"

        # Escoger 4 valores aleatorios para calcular el MCD
        lista = []
        lista.append(random.choice(restas))
        lista.append(random.choice(restas))
        lista.append(random.choice(restas))
        lista.append(random.choice(restas))
        lonKey = mcd(lista)

        lonKey = int(lonKey)

        salida2 = salida2 + "Distancias escogidas para calcular el Maximo Comun Divisor"
        salida2 = salida2 + "\n"
        salida2 = salida2 + str(lista)
        salida2 = salida2 + "\n"
        salida2 = salida2 + "Longitud de la clave:"
        salida2 =  salida2 + str(lonKey)
        salida2 = salida2 + "\n" + "Jotas" + "\n"

        #print(salida2)
        # print(lonKey)

        # Division de texto(Jotas)
        criptogramas = []
        jotas = 0
        while jotas < lonKey:
            criptogramas.append([])
            for corrimiento in range(0, len(texto) - lonKey, lonKey):
                criptogramas[jotas].append(texto[corrimiento + jotas])
               # print("jotas[{}] = {}, {}, {}, ...".format(jotas, criptogramas[jotas][0], criptogramas[jotas][1], criptogramas[jotas][2]))
            jotas += 1
        subcriptogramas = ""

        # Convertir de vector a string
        subcriptogramas = [[]] * lonKey
        for k in range(len(criptogramas)):
            subcriptogramas[k] = ''.join(criptogramas[k])

            salida2 = salida2 + criptogramas[k][0] + criptogramas[k][1] +criptogramas[k][2]+criptogramas[k][3] +" ..."
            salida2 = salida2 + "\n"

        salida2 = salida2 + "\n"+ "Analisis de Frecuencias para cada Jota"
        salida2 = salida2 + "\n"

        # recorrer cada jota y hallar las repeticiones de cada letra para poder calcular las hipotesis
        mas_Repetidos = []
        for i in range(len(subcriptogramas)):
            # print(subcriptogramas[i])
            mas_Repetidos.append([])
            mas_Repetidos[i] = conteo(alfabeto, subcriptogramas[i])
            salida2 = salida2 + mas_Repetidos[i][0] + mas_Repetidos[i][1] + mas_Repetidos[i][2] + mas_Repetidos[i][4] + "..."
            salida2 = salida2 + "\n"

        salida2 = salida2 + "\n" + "Hipotesis" + "\n"
        key = ""
        try:
            # HIPOTESIS
            # b = (c - m) mod
            for x in mas_Repetidos:
                # print(x)
                for y in range(0, len(alfabeto)):
                    #print(y)
                    if y >= len(alfabeto) - 1:
                        y = y - 1
                    if y >= len(estadistica) - 1:
                        y = y - 1

                    c1 = alfabeto.index(x[y])
                    m1 = alfabeto.index(estadistica[y])
                    b1 = (c1 - m1) % len(alfabeto)
                    # print(y)
                    # print(len(alfabeto))
                    c2 = alfabeto.index(x[y + 1])
                    m2 = alfabeto.index(estadistica[y + 1])
                    b2 = (c2 - m2) % len(alfabeto)
                    if b1 == b2:
                        salida2 = salida2  + "K = (" + str(c1) + " - " + str(m1) + ") Mod" + str(len(alfabeto)) + " = " + str(b1) + "\n"
                        # print("Primera Condicion")
                        key = key + alfabeto[b1]
                        salida2 = salida2 + key + "\n"
                        break
                    else:
                        if y >= len(alfabeto) - 1:
                            y = y - 1

                        if y >= len(estadistica) - 1:
                            y = y - 1

                        c1 = alfabeto.index(x[y + 1])
                        m1 = alfabeto.index(estadistica[y])
                        b1 = (c1 - m1) % len(alfabeto)

                        #print(y)
                        c2 = alfabeto.index(x[y])
                        m2 = alfabeto.index(estadistica[y + 1])
                        b2 = (c2 - m2) % len(alfabeto)
                        if b1 == b2:
                            salida2 = salida2  + "K = (" + str(c1) + " - " + str(m1) + ") Mod" + str(len(alfabeto)) + " = " + str(b1) + "\n"
                            key = key + alfabeto[b1]
                            salida2 = salida2 + key + "\n"
                            break
        except IndexError:
            flag =0
        # print(key)
        # print(alfabeto)
        # DESCIFRAR
        try:
            cont = 0
            re = ""
            for i in texto:
                if cont >= lonKey:
                    cont = 0
                    cont += 1
                else:
                    cont += 1
                c = alfabeto.index(i)
                k = alfabeto.index(key[cont - 1])
                m = (c - k) % len(alfabeto)
                re = re + alfabeto[m]
        except IndexError:
            flag  = 0
        archivo = archivo.replace("txt","dec")

        re = "".join(re)
        hash2 = hashlib.md5(re.encode("utf-8")).hexdigest()

        if flagHash == 0:
            if hash1 == hash2:
                flag = 1
            else:
                flag = 0
        else:
            flag = 1
        # flag =1 # salir del ciclo

        salida2 =  salida2+ "\n" + "La clave es: "
        salida2 =salida2 + key

    print("El Archivo Descifrado tiene como Nombre:", archivo.lower())
    d = open(archivo, "w", encoding="ISO-8859-1")
    d.write(re)
    d.close()

    print("La contraseña con la que fue cifrado el texto es: " + key)
    tf = time.time()
    tff = tf - ti
    print("El tiempo de Ejecucion de Kasiski Fue de: ", tff)


    print("El Archivo Resumen tiene como nombre:", "Resumen.txt")
    d = open("Resumen.txt", "w", encoding="ISO-8859-1")
    d.write(salida2)
    d.close()

    #print(salida2)

if args.enigma == True and args.ayuda == True:
    print("""
            ----------------------------UNIVERSIDAD AUTONOMA DE OCCIDENTE------------------------
            -------------------------------Algortirmo de Maquina Enigma--------------------------
            |                                                                         		|
    	    |                							  		|
            |    Sintaxis: ./proyectoFinal.py -en <opcion> -f <ArchivoEntrada>                  |                                                                     		
            |      <opcion> :                                                                   |
            |                                                                                   |
            |        -f para indicar el nombre del Archivo de Entrada                           |
    	    |                                                                                   
            |	     -p para indicar el archivo de parametros                                   |
      	    | 											|
    	    |									  		|
    	    |Ejemplo:								  		|
    	    |        Cifrar: ./proyectoFinal -en -f quijote.txt  -p parametros.txt              |  		
            |                                                                                   | 
            |                                                                                   |
    	    |  									  		|
    	    |  Elaborado por: Andres Flor          andres.flor@uao.edu.co	  		|
    	    |	          Juan Diego Escobar   juan_die.escobar@uao.edu.co	  		|
	    |  Profesor: Msc.Siler Amador Donado.				                |
            |                                                                                   |
            |    para modificar el archivo parametros tener en cuenta la sintaxys:              | 
            |    1, 3, 16, 22 ....... , 20-5, 9, 2, .......,25,22-19, 3, 7, 8 ..., 21           |
            |                                                                                   |
	    |	separando cada rotor con el caracter - y despues de cada , un espacio           |
	    |                                                                                   |
    	    |-----------------------------------------------------------------------------------|
    	    |-----------------------------------------------------------------------------------|
            """)

if args.enigma == True  and args.ayuda == False:

        print("Bienvenido a Enigma!!!")
        print("************************************************")
        # texto
        ti = time.time()

        print("Nombre del archivo a Cifrar  es: ", args.file)
        f = open(args.file, "r", encoding="ISO-8859-1")
        f1 = open(((args.parametros)), "r", encoding="ISO-8859-1")
        texto = f.readline()
        textoP = f1.read()
        texto = texto.upper().strip()
        textoP = textoP.upper().strip()
        f.close()
        f1.close()

        # obtener hash del texto Original
        hash1 = hashlib.md5(texto.encode("utf-8")).hexdigest()

        # procesamiento del archivo parametros

        N = textoP.split("-")  # distibuye los valores que seran las listas que contengan los valores de los rotores
        NAX1 = N[0].split(',')  # asigna los valores en str del rotor 1 a una lista auxiliar
        NAX2 = N[1].split(',')  # asigna los valores en str del rotor 2 a una lista auxiliar
        NAX3 = N[2].split(',')  # asigna los valores en str del rotor 3 a una lista auxiliar

        I = []
        II = []
        III = []
        N1 = list(range(0, 26))
        i = 0
        for i in N1:
            I.append(int(NAX1[i]))  # asigna los valores convertidos en int de una lista auxiliar al rotor I
            II.append(int(NAX2[i]))  # asigna los valores convertidos en int de una lista auxiliar al rotor II
            III.append(int(NAX3[i]))  # asigna los valores convertidos en int de una lista auxiliar al rotor III


        # definicion de los rotores
        def rotor(letra, numero, inverso=False):

            # lista que contiene los rotores
            tipo = [I, II, III]

            # condicinal caso false de inverso,
            if inverso == False:
                return tipo[numero - 1][(letra) % 26]
                # Devolvemos la letra cifrada con el rotor escogido.
            else:
                return tipo[numero - 1].index((letra) % 26)


        # deficion de funcion enigma, la cual recibe los parametros texto que es la cadena a cifrar, los rotores y sus posiciones de inicio  y los cambios que simuelan el pluh
        def enigma(texto, numeros, posiciones, cambios=list(range(26))):
            girador = [16, 4, 21]  # estos valores indican en que posicion del rotor X va a dar paso al rotor Y

            lista = list(
                texto)  # Convertimos el texto en una lista de caracteres. Ejemplo: 'hola' pasa a ser ('h','o','l','a')

            listacif = []  # Inicializamos la lista donde almacenaremos las letras que han sido cifradas

            letras = [ord(letra) - 65 for letra in
                      lista]  # la funcion ord nos da un numero asociado al caracter en la tabla de ascci ejemplo.. a la letra A le corresponde el 65, a la B el 66,... en la tabla de ascci, por eso, restamos 65 a todos los elementos de la lista.

            for letra in letras:  # Bucle para codificar letra por letra
                # Lo primero que hace la letra es pasar por el plugboard o cambiador

                letra = cambios[letra]

                posiciones[2] = (posiciones[
                                     2] + 1) % 26  # Hacemos girar al rotor derecho, asegurándonos de que si sobrepasa 25 vuelva al 0 (pasar de la A a la Z) con el modulo 26

                # Comprobamos si puede girar  otro rotor
                if posiciones[2] == girador[
                    numeros[2] - 1] + 1:  # condicional que verifica si deber girar el rotor del medio
                    posiciones[1] = (posiciones[1] + 1) % 26

                if posiciones[1] == girador[
                    numeros[1] - 1]:  # condicional que verifica si deber girar el rotor de la derecha
                    posiciones[0] = (posiciones[0] + 1) % 26
                    posiciones[1] += 1

                # Hacemos pasar la letra por los tres rotores y el reflector
                rotor1 = rotor((letra + posiciones[2]) % 26,
                               numeros[2])  # Vamos a hacer pasar el resultado de cada rotor al siguiente.

                rotor2 = rotor((rotor1 - (posiciones[2] - posiciones[1])) % 26, numeros[1])

                rotor3 = rotor(rotor2 - (posiciones[1] - posiciones[0]) % 26, numeros[0])

                # se define una lista que respresenta a el rotor de reflejo que en este caso es estatico que recibe y devuelve al mismo rotor la reflexion de un caracter
                R = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0,
                     19]
                reflejado = R[rotor3 - posiciones[0]]

                # Aquí se sustituyen los valores de las letras en los rotores, es decir, si queremos cifrar A, cogemos la posición del elemento 0 en I (como 0 es el 21º elemento de I, ciframos la A como V)

                rotor3 = rotor(reflejado + posiciones[0], numeros[0], True)

                rotor2 = rotor(rotor3 + (posiciones[1] - posiciones[0]) % 26, numeros[1], True)

                rotor1 = (rotor(rotor2 + (posiciones[2] - posiciones[1]) % 26, numeros[2], True) - posiciones[2]) % 26

                # Hacemos pasar la letra por el plugboard, por si se le ha asociado un cambio:
                letra = cambios[rotor1]

                listacif.append(letra)  # Añadimos la letra cifrada a la lista

            # Cuando salga del bucle, habrá terminado de cifrar todas las letras. Devolvemos por fin la lista cifrada, unida como cadena:

            listafin = [chr(letra + 65) for letra in
                        listacif]  # chr es el inverso de la funcion ord, pasa de números a las correspondientes letras.

            listafin = ''.join(listafin)  # Unimos los elementos de la lista en una cadena.

            return listafin


        # f = open(args.file, "r", encoding="ISO-8859-1")
        # print("Texto del Documento Cifrado:")
        # textoClaro = f.readline()
        # print(dato)
        # f.close()

        # cifrar = "EUREKA"

        print("procesando...")
        cifrado = (enigma(texto.upper(), [3, 2, 1], [5, 4, 17],
                          [11, 1, 2, 20, 4, 5, 6, 7, 8, 9, 10, 0, 12, 13, 14, 15, 16, 17, 18, 19, 3, 21, 22, 23, 24,
                           25]))

        print("el texto ha sido cifrado por el codigo enigma en el archivo Enigma.cif")

        d = open("Enigma.cif", "w")
        d.write(cifrado)
        d.close()
        print("__________________________________________________________")
        descifrar = cifrado
        descifrado = (enigma(descifrar, [3, 2, 1], [5, 4, 17],
                             [11, 1, 2, 20, 4, 5, 6, 7, 8, 9, 10, 0, 12, 13, 14, 15, 16, 17, 18, 19, 3, 21, 22, 23, 24,
                              25]))
        print("El texto ha sido descifrado por el codigo enigma en el archivo Enigma.des")

        d = open("Enigma.dec", "w", encoding="ISO-8859-1")
        d.write(descifrado)
        d.close()

        hash2 = hashlib.md5(descifrado.encode("utf-8")).hexdigest()

        if hash1 == hash2:
            print("hash es igual")
        tf = time.time()
        tff = tf - ti
        print(tff)
        print("El tiempo de Ejecucion de Enigma es de " + str(tff))
