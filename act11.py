# Escribir un programa que le pregunte al usuario una cantidad de pesos, una tasa de interés y
# un número de años y muestre como resultado el monto final a obtener. La fórmula a utilizar
# es:
# Cn = C * (1 + x/100) ^ n
# Donde C es el capital inicial, x es la tasa de interés y n es el número de años a calcular.

def calcular_monto_final(capital_inicial, tasa_interes, numero_anios):
    """Calcula el monto final a obtener."""
    monto_final = capital_inicial * (1 + tasa_interes / 100) ** numero_anios
    return monto_final

# Ejemplo de uso
capital_inicial = float(input("Ingrese el capital inicial: "))  # C (pesos)
tasa_interes = float(input("Ingrese la tasa de interés: "))  # x (%)
numero_anios = int(input("Ingrese el número de años: "))  # n

monto_final = calcular_monto_final(capital_inicial, tasa_interes, numero_anios)

print(f"El monto final a obtener es: {monto_final:.2f} pesos")