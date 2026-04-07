nombre = "Santiago"
fecha = "27 de Julio de 2024"
saludo = "buenas tardes"

bienvenida = f"Hola {nombre}, {saludo}! Hoy es {fecha}."
print(bienvenida)

# Solicitar monto al usuario
dolares = float(input("Cantidad de dolares a cambiar: "))

# Tipo de cambio aproximado
tipo_de_cambio = 0.91
euros = dolares * tipo_de_cambio

# Calcular billetes y monedas
billetes_10 = int(euros // 10)
billetes_1 = int(euros % 10)
monedas = round(euros * 100 % 100)

print(f"\nVas a cambiar {dolares} dolares a euros.")
print(f"Eso son {euros:.2f} euros.")
print(f"Recibiras: {billetes_10} billete(s) de 10, {billetes_1} billete(s) de 1 y {monedas} centavo(s).")
