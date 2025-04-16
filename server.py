"""
Emotion detection server
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def em_detector():
    """
    Module Name: em_detector

    Description:
       Gets text input form the user and provide emotion 

    Author: Yoseph
    Date: 2025
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:
        return "Invalid input! Please try again."
    return "For the given statement, the system response is: " + ", ".join([
        f"anger: {anger}",
        f"disgust: {disgust}",
        f"fear: {fear}",
        f"joy: {joy}",
        f"sadness: {sadness}",
        f"dominant_emotion: {dominant_emotion}"
    ])
@app.route("/")
def render_index_page():
    """
    Module Name: em_detector

    Description:
        root route.

    Usage:
        render the index html.

    Author: Yoseph
    Date: 2025
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
