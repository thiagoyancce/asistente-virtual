from os import mkdir, listdir
from os.path import exists, isfile
from shutil import move, Error
from argparse import ArgumentParser

def crear_carpetas_si_no_existe(carpetas, ruta="./"):
  
    for carpeta in carpetas:
        if exists(ruta+"/"+carpeta) != True:
            # si la carpeta no existe exists() retorna False lo cual es diferente a True
            #  y esta condicion se llevara a cabo
            mkdir(ruta+"/"+carpeta)
            print("{} Creando la carpeta -> {}"+carpeta)


def asociar_carpetas_con_extensiones(nombre_carpeta, extensiones_de_archivos, ruta=".", ArchivosExcepciones=[]):

    ArchivosParaEstaCarpeta = []
    
    for archivo in listdir(ruta):
        if archivo.endswith(extensiones_de_archivos) == True and archivo not in ArchivosExcepciones and isfile(ruta+"/"+archivo):
           
            ArchivosParaEstaCarpeta.append(ruta+"/"+archivo)

    return ArchivosParaEstaCarpeta

def organizar_archivos(ruta_directorio_archivos, ruta_directorio_salida):


    ArchivosExcepciones = [__file__.split("\\")[-1], "requirements.txt"]
    carpetas = ["documentos", "fotos", "videos", "musica","ejecutables", "otros"]
    crear_carpetas_si_no_existe(carpetas,ruta_directorio_salida)

    extensionesdocumentos = [   
                                (".pdf","PDF", ".doc", ".docx", ".txt", ".odt", ".xlsx", ".ppt", ".pptx"),# documentos
                                (".png", ".PNG",".jpg", ".jpeg", ".gif", ".tiff", ".bmp"),                 # fotos
                                (".mp4", ".mkv", ".avi", ".mov", ".flv", ".divx"),                  # videos
                                (".mp3", ".aac", ".wav", ".aiff", ".wma", ".opus", ".ogg"),   # musica 
                                (".exe",".apk","init",".bat"),      # ejecutables
                                (   
                                    ".py", ".rar", ".zip", ".html", ".tmp", ".dat", ".exe", ".deb", 
                                    ".dmg",".sql", ".psd", ".c", ".asm", ".java", ".rst"
                                ), # otros
                            ]
    
    for carpetaNumero in range(0, len(carpetas)):

        ListaDeArchivos = asociar_carpetas_con_extensiones(carpetaNumero, extensionesdocumentos[carpetaNumero],ruta_directorio_salida , ArchivosExcepciones=ArchivosExcepciones) 
        print("{} Archivos a guardar en la carpeta {}, en total un cantidad de {}:")
        print("\n".join(ListaDeArchivos))
        for archivo in ListaDeArchivos:
            try:
                print("{} Moviendo el archivo ({}) a la carpeta ({})")
                move(archivo, ruta_directorio_salida+"/"+carpetas[carpetaNumero])
            except Error:
                print("{} El archivo {} \t ya existe en el directorio {}")
            

