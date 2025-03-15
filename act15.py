# Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10.000 pesos,
# el segundo 20. 000 pesos, el tercero 40. 000 pesos y así sucesivamente. Realizar un algoritmo
# para determinar cuánto debe pagar mensualmente y el total de lo que pagó después de los 20
# meses.



def calcular_pagos():
    pago_mensual = 10000  # Pago inicial
    total_pagado = 0

    for mes in range(1, 21):  # 20 meses
        print(f"Mes {mes}: ${pago_mensual}")
        total_pagado += pago_mensual
        pago_mensual *= 2  # Duplica el pago cada mes

    print(f"\nTotal pagado después de 20 meses: ${total_pagado}")

# Llamar a la función
calcular_pagos()
