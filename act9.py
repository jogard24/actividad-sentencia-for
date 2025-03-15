# Diseñar un diagrama que permita emitir la factura correspondiente a una compra de un
# artículo del cual se adquiere una o varias unidades y se conoce su precio antes de IVA (iva igual
# al 16%), y si el precio bruto (precio de venta más IVA) es mayor de $500. 000.oo se debe realizar
# un descuento del 15%.

def calcular_total(precio_unitario, cantidad):
  """Calcula el total de una compra, incluyendo IVA y descuento.

  Args:
    precio_unitario: El precio unitario del artículo antes de IVA.
    cantidad: La cantidad de unidades del artículo.

  Returns:
    El total a pagar.
  """

  # Calcular el precio antes de IVA
  precio_sin_iva = precio_unitario * cantidad

  # Calcular el IVA
  iva = precio_sin_iva * 0.16

  # Calcular el precio bruto
  precio_bruto = precio_sin_iva + iva

  # Aplicar descuento si corresponde
  descuento = 0
  if precio_bruto > 500000:
    descuento = precio_bruto * 0.15

  # Calcular el total a pagar
  total = precio_bruto - descuento

  return total

# Ejemplo de uso
precio_unitario = float(input("Ingrese el precio unitario antes de IVA: "))
cantidad = int(input("Ingrese la cantidad de unidades: "))

total_a_pagar = calcular_total(precio_unitario, cantidad)

print(f"El total a pagar es: ${total_a_pagar:.2f}")