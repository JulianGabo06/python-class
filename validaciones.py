# se importa el modulo os, este nos sirve para poder utilizar la funcion independiente
# del sistema operativo
import os

# creamos una funcion para limpiar la consola
def limpiar_consola():
    # dependiendo de si el sistema operativo es windows(nt) se utiliza
    # el comando de windows, y si es algo diferente a windows se asume 
    # que utiliza el sistema parecido a linux
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# inicializamos las variables del user y del password
user = ''
password = ''

# le pedimos que registre su  usuario y su contraseña
user = input('Ingresa un usuario: ')
password = input('Ingresa una contraseña: ')

# checheamos que sea alfanumerica
if password.isalnum():
    #limpiamos la consola 
    limpiar_consola()

    # le pedimos que ingrese el usuario y contraseña que previamente registro
    userInput = input('Ingresa el usuario: ')
    passwordInput = input('Ingresa la contraseña: ')
    
    # si ocurre un error se le muestra
    while userInput != user or passwordInput != password:
        print(f'\n❌ Usuario o contraseña incorrectos ❌\n')
        userInput = input('Ingresa el usuario: ')
        passwordInput = input('Ingresa la contraseña: ')


    # si ocurre el user y contraseña coinsiden puede ingresar
    while user.casefold() == userInput.casefold() and password.casefold() == passwordInput.casefold():
        # agregamos al mensaje de bienvenida el usuario
        welcomeStrg = f' Bienvenido {user} '
        print('')
        # hacemos que se centre el mensaje, 25 rayitas del lado izquierdo y 25 del derecho
        print(welcomeStrg.center(50, '-'))
        break
else:
    # si la contraseña no es alfanumerica le sale un error al usuario
    print(f'\n❌ La contraseña contiene caracteres invalidos ❌')
    print('👋 intenta mas tarde 👋')

