import openai

#Convertir audio en texto
class Transcriber:
    def __init__(self):
        pass
        
    #Siempre guarda y lee del archivo audio.mp3
    #Utiliza whisper en la nube :) puedes cambiarlo por una impl local
    def transcribe(self, audio):
        audio.save("audio.mp3")
        audio_file= open("audio.mp3", "rb")
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        return transcript.text
    

class Avatar:
    vector = []
    def __init__(self):
        self.vector.append("Eres un doctor privado especializado en medicina general que respondes brevemente.si alguien te preguntase sobre otra cosa que no sea medicina  o algo que no tenga relacion tu siempre respondes que no estas familiarizado con el tema o algo parecido ")
        self.vector.append("Eres un profesor experto en varias materias respondes amablemente y breve. si alguien te preguntase sobre otra cosa que no sea estudios  o algo relacionado tu siempre respondes que no estas familiarizado con el tema o algo parecido ")
        self.vector.append("eres una persona que conoce todo de Deportes")
        self.vector.append("Eres un amigos  que aconseja  contando anecdotas de otras personas que respondes breve")
        self.vector.append("Eres un asistente que responde con brevedad")
        
        pass
        
    #Siempre guarda y lee del archivo audio.mp3
    #Utiliza whisper en la nube :) puedes cambiarlo por una impl local
    def prompt(self, numAvatar):
        return self.vector[numAvatar]
        