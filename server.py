from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analiza el texto recibido y devuelve una frase formateada con las emociones.
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

    # Si el texto es inválido (según la lógica que haremos luego o si viene vacío)
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
    Renderiza la página principal.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)