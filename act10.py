# Construya los algoritmos que permitan calcular las siguientes series con un valor de N
# ingresado desde teclado:
# 1
# 2 + 22 + 32+...N2
# tal que N es positivo
# 1
# 1 + 22 + 33+...Nn
# tal que N es positivo

def calcular_serie1_for(n):
  """Calcula la serie 1^2 + 2^2 + 3^2 + ... + N^2 usando un bucle for."""
  suma = 0
  for i in range(1, n + 1):
    suma += i**2
  return suma

def calcular_serie1_while(n):
  """Calcula la serie 1^2 + 2^2 + 3^2 + ... + N^2 usando un bucle while."""
  suma = 0
  i = 1
  while i <= n:
    suma += i**2
    i += 1
  return suma

# Ejemplo de uso
n = int(input("Ingrese el valor de N: "))

resultado_for = calcular_serie1_for(n)
resultado_while = calcular_serie1_while(n)

print(f"Resultado usando for: {resultado_for}")
print(f"Resultado usando while: {resultado_while}")