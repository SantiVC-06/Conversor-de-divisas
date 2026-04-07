def registro(persona):
    esigual = False
    persona["Nombre"] = str(input("Ingresar nombre de usuario: "))
    if persona["Nombre"].strip().lower() == "salir":
        return False
    while not esigual:
      persona["Correo"] = str(input("Ingresar correo electrónico: "))
      persona["Contrasena"] = str(input("Ingresar contraseña: "))
      Repeticion = str(input("Repetir contraseña: "))
      if persona["Contrasena"] == Repeticion:
        esigual = True
      else: print("Las contraseñas no coinciden, por favor intentá de nuevo.")
    return True

def login(usuarios):
    correo = str(input("Ingresar correo electrónico: "))
    contrasena = str(input("Ingresar contraseña: "))
    for usuario in usuarios:
        if correo == usuario["Correo"] and contrasena == usuario["Contrasena"]:
            print(f"Inicio de sesión exitoso. Bienvenido, {usuario['Nombre']}!")
            return usuario
    print("Correo electrónico o contraseña incorrectos.")
