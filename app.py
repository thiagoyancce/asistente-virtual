

import os

import openai
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
import json
from transcriber import Transcriber,Avatar
from llm import LLM
from weather import Weather
from tts import TTS
from pc_command import PcCommand
from extras import dowload,cmd,clean,OrdenarFile
import recorder
import time

conversacion = []

#Cargar llaves del archivo .env
load_dotenv()
Prompt="Eres un asistente"
directorio=""
openai.api_key = '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'
elevenlabs_key = 'ecb3d600d5c13d936474e615e9386dce'

app = Flask(__name__)

@app.route('/procesar_numero', methods=['POST'])
def procesar_numero():
    data = request.get_json()  # Obtiene los datos JSON enviados desde la página HTML
    selection = data.get('numero', 0)  # Obtiene el número del objeto JSON

    # Realiza cualquier procesamiento necesario con el número aquí
    # Por ejemplo, puedes duplicar el número y devolverlo como resultado
    global Prompt 
    Prompt=Avatar().prompt(selection)
    print (Avatar().prompt(selection))

    return jsonify({'resultado': selection})  # Devuelve el resultado como JSON

@app.route('/procesar_cadena', methods=['POST'])
def procesar_cadena():
    data = request.get_json()
    global directorio
    directorio = data.get('cadena', '')
    print (directorio)
    return jsonify({'resultado': ""})



@app.route("/")
def index():
    return render_template("recorder.html")

@app.route("/audio", methods=["POST"])
def audio():
  


  
    audio = request.files.get("audio")
    
    text = Transcriber().transcribe(audio)
    print("texto"+text)
    global conversacion
    conversacion.append({"role": "system", "content":Prompt})
    conversacion.append({"role": "user", "content": text})
    #Utilizar el LLM para ver si llamar una funcion
    llm = LLM()
    function_name, args, message = llm.process_functions(text)
    if function_name is not None:
        #Si se desea llamar una funcion de las que tenemos
        if function_name == "get_weather":
            #Llamar a la funcion del clima
            function_response = Weather().get(args["ubicacion"])
            function_response = json.dumps(function_response)
            print(f"Respuesta de la funcion: {function_response}")
            
            final_response = llm.process_response(text, message, function_name, function_response)
            tts_file = TTS().process(final_response)
            return {"result": "ok", "text": final_response, "file": tts_file}
        
        elif function_name == "send_email":
            #Llamar a la funcion para enviar un correo
            final_response = "Tu que estas leyendo el codigo, implementame y envia correos muahaha"
            tts_file = TTS().process(final_response)
            return {"result": "ok", "text": final_response, "file": tts_file}
        
        elif function_name == "open_chrome":
            PcCommand().open_chrome(args["website"])
            final_response = "Listo, ya abrí chrome en el sitio " + args["website"]
            tts_file = TTS().process(final_response)
            return {"result": "ok", "text": final_response, "file": tts_file}
        
        elif function_name == "dominate_human_race":
            final_response = "No te creas. Suscríbete al canal!"
            tts_file = TTS().process(final_response)
            return {"result": "ok", "text": final_response, "file": tts_file}
        elif function_name == "download_youtube_video":
          
            youtube_name = args["nombre"]
            try:
                dowload.dowloadVideo(youtube_name)
                final_response = f"Video de YouTube [{youtube_name}] descargado exitosamente."
            except Exception as e:
                final_response = f"No se pudo descargar el video de YouTube [{youtube_name}]. Error: {str(e)}"

            tts_file = TTS().process(final_response)
            return {"result": "ok", "text": final_response, "file": tts_file}

        elif function_name == "download_youtube_music":
            youtube_name = args["nombre"]
            
            try:
                dowload.dowloadMp3(youtube_name)
                
                final_response = f"Música de YouTube [{youtube_name}] descargada exitosamente."
            except Exception as e:
                final_response = f"No se pudo descargar la música de YouTube [{youtube_name}]. Error: {str(e)}"

            tts_file = TTS().process(final_response)
            return {"result": "ok", "text": final_response, "file": tts_file}
        elif function_name == "shutdown_computer":
            segundos =args["segundos"]
            try:
                cmd.apagar(segundos)
                final_response = "La computadora se está apagando. Hasta luego."
            except Exception as e:
                final_response = f"No se pudo apagar la computadora.  Error: {str(e)} "

            tts_file = TTS().process(final_response)
            return {"result": "ok", "text": final_response, "file": tts_file}

        elif function_name == "cancel_shutdown":
            
            try:
                cmd.cancelar()

                final_response = "El apagado programado ha sido cancelado."
            except Exception as e:
                final_response = f"No se pudo cancelar el apagado programado.  Error: {str(e)}"

            tts_file = TTS().process(final_response)
            return {"result": "ok", "text": final_response, "file": tts_file}
        elif function_name == "clean_system":
          
            try:
                clean.limpiarTemporales()

                final_response = "Se ha realizado una limpieza del sistema satisfactoriamente."
            except Exception as e:
                final_response = f"No se pudo realizar la limpieza del sistema. Error: {str(e)}"

            tts_file = TTS().process(final_response)
            return {"result": "ok", "text": final_response, "file": tts_file}
        elif function_name == "close_browser":
           
            try:
                cmd.cerrarNavegador()
                final_response = "Se ha cerrado el navegador satisfactoriamente."
            except Exception as e:
                final_response = f"No se pudo cerrar el navegador. Error: {str(e)}"

            tts_file = TTS().process(final_response)
            return {"result": "ok", "text": final_response, "file": tts_file}
        elif function_name == "organize_folders":
            if(directorio!=""):
                OrdenarFile.organizar_archivos(directorio,directorio)
            try:
                
                final_response = f"Las carpetas en el directorio han sido organizadas."
            except Exception as e:
                final_response = f"No se pudo organizar las carpetas en el directorio. Error: {str(e)}"

            tts_file = TTS().process(final_response)
            return {"result": "ok", "text": final_response, "file": tts_file}
    else:
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",messages=conversacion,
            max_tokens=50)
        result=""
        for choice in response.choices:
            result+=choice.message.content
        
        conversacion.append({"role": "assistant", "content": result})
       
        tts_file = TTS().process(result)
        return{"result":"ok","text":result, "file": tts_file}