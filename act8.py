# Hacer un algoritmo que al ingresar N números por la pantalla y se calcule la suma, resta,
# multiplicación y división. El proceso debe terminar cuando se hallan realizado 10 procesos
# (Hacer uso de contadores).


#Se inicia contador for 
for i in range (10):
#se imprime el numero de veces  
    print ("PROCESO :  ", i + 1 )
       # se plantean dos variables para introducir cifras
    num1 = int(input("ingresar primero numero : "))
    num2 = int(input("ingresar segundo numero : "))
    print ("")

    #se imprimen resultados 
    print("....SUMA....")
    print (num1, "+", num2, "=", num1+num2 )
    print("....RESTA....")
    print (num1, "-", num2, "=", num1-num2)
    print("....MULTIPLICACION.... ")
    print (num1, "*", num2, "=", num1*num2)
    print ("....DIVISION....")
    print (num1, "/", num2, "=", num1/num2)
    print ("")

