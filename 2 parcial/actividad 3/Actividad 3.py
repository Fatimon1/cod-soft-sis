# Escribe un mensaje en un fichero
def escribe_fichero(mensaje):
    with open('fichero_comunicacion.txt', 'a') as fichero:
        fichero.write(mensaje)

# Leer el mensaje del fichero        
def lee_fichero():
    mensaje = ""
    with open('fichero_comunicacion.txt', 'r') as fichero:
        mensaje = fichero.read()
    return mensaje
nombre=input("Ingresa tu nombre ")
ciudad=input("Ingresa tu ciudad ")
comida_favorita = input("Ingresa tu comida favorita. ")
edad = input("Ingresa tu edad. ")
escribe_fichero(nombre + "\n")
escribe_fichero(ciudad + "\n")
escribe_fichero(comida_favorita + "\n")
escribe_fichero(edad + "\n")
                
print(lee_fichero())