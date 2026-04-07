from datetime import datetime
import ModuRegistroIngreso
import requests

def obtener_tasa(moneda_origen, moneda_destino):
    url = f"https://api.frankfurter.app/latest?from={moneda_origen}&to={moneda_destino}"
    response = requests.get(url)
    if response.status_code != 200: 
        print("Moneda no reconocida, intentá de nuevo.")
        return None
    data = response.json()
    return data["rates"][moneda_destino]

def convertir():
    origen = input("¿De qué moneda? ").upper()
    destino = input("¿A qué moneda? ").upper()
    monto = float(input("¿Cuánto quieres convertir? "))
    
    tasa = obtener_tasa(origen, destino)
    if tasa is None:
        return
    resultado = monto * tasa
    
    print(f"\n{monto} {origen} = {resultado:.2f} {destino}")
    print(f"Tasa usada: 1 {origen} = {tasa} {destino}")

usuarios = []

while True:
    print("1. Registrar usuario")
    print("2. Iniciar sesión")
    print("3. Salir")
    opcion = input("\nElegí una opción: ").strip()
    if opcion == "1":
        persona = {"Nombre": None, "Correo": None, "Contrasena": None}
        ModuRegistroIngreso.registro(persona)
        usuarios.append(persona)
        print(f"Usuario '{persona['Nombre']}' registrado exitosamente.\n")
    elif opcion == "2":
        if not usuarios:
            print("No hay usuarios registrados aún.\n")
        else:
            usuario = ModuRegistroIngreso.login(usuarios)
            fecha = datetime.now().date()
            hora = datetime.now().hour
            if hora < 12:
              saludo = "buenos días"
            elif 12 <= hora < 18:
              saludo = "buenas tardes"
            else:
              saludo = "buenas noches"
            print(f"Hola {usuario['Nombre']}, {saludo}! Hoy es {fecha}.")
            print("Ingresaste al sistema de cambio de divisas.\n")
            convertir()
    elif opcion == "3":
        print("Hasta luego!")
        break
    else:
        print("Opción inválida, intentá de nuevo.\n")
