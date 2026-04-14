"""
Servidor de Flask para el sistema de detección de emociones.
Este módulo define las rutas para analizar texto y renderizar la página principal.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Recibe un texto desde la interfaz web, lo analiza usando la función
    emotion_detector y devuelve una frase formateada con los resultados.
    """
    # Obtener el texto de los parámetros de la URL
    text_to_analyze = request.args.get('textToAnalyze')

    # Llamar a la función del paquete
    response = emotion_detector(text_to_analyze)

    # Extraer los valores
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Task 7: Manejo de error si la emoción dominante es None
    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    # Retornar la respuesta con el formato exacto del enunciado
    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Renderiza la página de inicio de la aplicación web.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    