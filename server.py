"""Flask server for Emotion Detection application."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")


@app.route('/emotionDetector')
def emotion_analyzer():
    """Analyze the user's text input and return the detected emotions."""
    text_to_detect = request.args.get("textToAnalyze")
    emotion_result = emotion_detector(text_to_detect)

    anger = emotion_result["anger"]
    disgust = emotion_result["disgust"]
    fear = emotion_result["fear"]
    joy = emotion_result["joy"]
    sadness = emotion_result["sadness"]
    dominant_emotion = emotion_result["dominant_emotion"]

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy}, and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """Render the main index page."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
