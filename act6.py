# En una empresa de 100 trabajadores, se hará un aumento al salario de acuerdo al tiempo de
# servicio, para este aumento se tomará en cuenta lo siguiente:
# - Tiempo de servicio: de 1 a 5 años Aumento: 100 PESOS
# - Tiempo de servicio: de 5 a 10 años Aumento: 250 PESOS
# - Tiempo de servicio: de 10 a 20 años Aumento: 400 PESOS.
# - Tiempo de servicio: de 20 años a más Aumento: 550 PESOS.

def calcular_aumento(tiempo_servicio):
#   Calcula el aumento de salario según el tiempo de servicio.
#     tiempo_servicio: El tiempo de servicio del empleado en años.

#     El aumento de salario en pesos.
  
  if 1 <= tiempo_servicio <= 5:
    return 100
  elif 5 < tiempo_servicio <= 10:
    return 250
  elif 10 < tiempo_servicio <= 20:
    return 400
  elif tiempo_servicio > 20:
    return 550
  else:
    return 0  # Si el tiempo de servicio es menor a 1 año

# Ejemplo de uso para 100 empleados:
for i in range(100):
  tiempo_servicio = int(input(f"Ingrese el tiempo de servicio del empleado {i + 1}: "))
  aumento = calcular_aumento(tiempo_servicio)
  print(f"El aumento para el empleado {i + 1} es: {aumento} PESOS")