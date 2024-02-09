import os
import shutil
def borrarArchivos(carpeta):
    # Obtén la lista de archivos en la carpeta
    archivos = os.listdir(carpeta)

    # Itera sobre la lista de archivos y elimínalos
    for archivo in archivos:
        ruta_completa = os.path.join(carpeta, archivo)
        if os.path.isfile(ruta_completa):
            try:
        # Intentar eliminar el archivo
                os.remove(ruta_completa)
                print(f"El archivo {ruta_completa} se eliminó con éxito.")
            except OSError as e:
                print(f"No se pudo eliminar el archivo {ruta_completa}: {e}")


def borrarCarpetas(direccion):
    if os.path.exists(direccion) and os.path.isdir(direccion):  
        carpetas = [nombre for nombre in os.listdir(direccion) if os.path.isdir(os.path.join(direccion, nombre))]

            # Eliminar cada carpeta
        for carpeta in carpetas:
            carpeta_completa = os.path.join(direccion, carpeta)
            try:
                    # Eliminar la carpeta
                shutil.rmtree(carpeta_completa)
                print(f"Se eliminó la carpeta: {carpeta_completa}")
            except OSError as e:
                print(f"No se pudo eliminar la carpeta {carpeta_completa}: {e}")
    else:
        print(f"El directorio principal {direccion} no existe o no es un directorio.")


def limpiarTemporales():
    carpeta_a_limpiar = "C:\Windows\Temp"
    carpeta_prefetch="C:\Windows\Prefetch"
    borrarCarpetas(carpeta_a_limpiar)
    borrarArchivos(carpeta_a_limpiar)
    borrarCarpetas(carpeta_prefetch)
    borrarArchivos(carpeta_prefetch)

#limpiarTemporales("C:\Windows\Temp")



