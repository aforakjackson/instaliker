import random
from instagrapi import Client
from getpass import getpass
from colorama import Fore, init
from pyfiglet import Figlet
import keyboard
import time  # Importa el módulo time

init()
f = Figlet(font='slant')
print(Fore.GREEN + f.renderText('InstaLiker')+ "                        By Aforak y EsponjiMan")
print("####################################################")
usuario = input(Fore.WHITE + 'Introduce usuario: ')
password = getpass('Introduce clave: ')

#COMIENZA LA CONEXIÓN
client=Client()
client.login(f"{usuario}",f"{password}")
print(Fore.GREEN + "[*]" + Fore.WHITE + "¡Conectado!")
#CONEXIÓN REALIZADA

#MENÚ
def menu():
    print(Fore.WHITE + "############# MENÚ ############")
    print(Fore.WHITE + "Abrir menú - Pulsa " + Fore.GREEN + "M" )
    print(Fore.WHITE + "Dar likes automáticamente por tema - Pulsa " + Fore.GREEN + "L" )
    print(Fore.WHITE + "Salir del menú - Pulsa " + Fore.RED + "CNTRL + C" )
    print(Fore.WHITE + "###############################")

keyboard.add_hotkey("m", menu)  # Asignación de la tecla a la función

def dar_likes():
    print(Fore.GREEN + "INFO: " + Fore.WHITE + "¡Has elegido la opción de Dar Likes por temas!")
    cantidad=int(input("Introduce la cantidad de likes que quieres dar: "))
    hastag=input('Elige sobre que tema serán las publicaciones: ')
    medias= client.hashtag_medias_recent(hastag,cantidad)
    for i,media in enumerate(medias):
        client.media_like(media.id)
        print(Fore.GREEN + "[*]" + Fore.WHITE + f"¡Has dado like a  {i+1} publicaciones sobre #{hastag}!")
    print("¡Acciones realizadas con éxito!")
    print(Fore.GREEN + "INFO: " + Fore.WHITE + "Pulsa 'M' para abrir el menú")
keyboard.add_hotkey("l", dar_likes)  # Asignación de la tecla a la función

while True:  # Bucle infinito
    print(Fore.GREEN + "INFO: " + Fore.WHITE + "Pulsa 'M' para abrir el menú")
    time.sleep(210)  # Pausa de 1 segundo
    if keyboard.is_pressed('q'):  # Si el usuario presiona 'q', se rompe el bucle
        break

print(Fore.RED + "[*]" + Fore.WHITE + "Cerrando sesión de " + Fore.YELLOW + f"{usuario}")
