
#Un empleado de la tienda “Tiki Taka” realiza N ventas durante el día, se requiere saber cuántas
#de ellas fueron mayores a $1000, cuántas fueron mayores a $500 pero menores o iguales a
#$1000, y cuántas fueron menores o iguales a $500. Además, se requiere saber el monto de lo
#vendido en cada categoría y de forma global. Realice un algoritmo que permita determinar lo
#anterior.

print ("actividad 5")

vmayora1000 = 0
vmayora500 = 0



l = []

for i in range (5):
    n = int(input(f" ventas {i+1} : "))

    if n >= 1000 and n <= 500:
        print ("la venta es mayor o igual a 1000 / 500 : " )

        
    elif n > 1000:
        print ("venta mayor a 1000 :")

    elif n > 500:
        print ("venta mayor a 500 :")

    elif n <= 1000:
        print ("venta menor o igual a 1000 :")

    elif n <= 500:
        print ("venta menor o igual a 500 : ")

    total = i + n 
    print (f"total global es de {total} : ")


       





