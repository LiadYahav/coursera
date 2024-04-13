"""
    Executing this function initiates the application of emotion detection
     to be executed over the Flask channel and deployed on
    localhost:5000.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# initiate the flask app
app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emo_detector():
    """
        this code receives the text from the HTML interface and
        runs emotion detection over it using emotion_detector()
        function. the output returned shows that emotion values and dominant emotion.
    """
    text_to_analyse = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyse)
    if response['dominant_emotion']:
        return (f"For the given statement, the system response is 'anger':"
                f" {response['anger']}, 'disgust': {response['disgust']},"
                f" 'fear': {response['fear']}, 'joy': {response['joy']},"
                f" 'sadness': {response['sadness']}."
                f" The dominant emotion is {response['dominant_emotion']}")
    return "Invalid text! Please try again!"


@app.route("/")
def render_index_page():
    """
        this function initiates the rendering of the main app page
        over the flask channel
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
