usuario_guardado = "usuario"
contrasena_guardada = "1234"

usuario_ingresado = input("ingresa tu nombre de usuario")
contrasena_ingresada = input("Ingresa tu contraseña")

if usuario_guardado == usuario_ingresado and contrasena_guardada == contrasena_ingresada:
    print("Usuario logueado de forma correcta")
else: 
    print("Datos incorrectos")