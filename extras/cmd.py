import os
import pyautogui
import time
# Comprueba si el sistema operativo es Windows o no
def apagar( time):
    if os.name == 'nt':
    # Si es Windows, utiliza el comando 'shutdown'
        print("hola")
        os.system('shutdown /s /t '+time)
        print("hola")
    else:

    # Si es Linux o macOS, utiliza el comando 'shutdown'
        os.system('shutdown -h now')


def cancelar():
# Cancelar un apagado programado en Windows
    os.system('shutdown /a')




def cerrarNavegador():
    time.sleep(5)
    for _ in range(10): 
        time.sleep(1) 
        pyautogui.hotkey('ctrl', 'w')

# Espera unos segundos para que tengas tiempo de cambiar a la ventana del navegador
