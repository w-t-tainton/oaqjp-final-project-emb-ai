""" 
    Emotion Detection executed over the Flask
    channel and deployed on localhost:5000.
"""

# Import Flask, render_template, request
from flask import Flask, render_template, request

# Import the emotion detection function from the package created
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emot_detector():
    """
        Receives the text from the index HTML interface, runs it through
        the emotion_detector() function and returns a fromatted string.
    """
    # Get text to analyze from request arguement
    text_to_analyze = request.args.get('textToAnalyze')
    # Call the emotion detector
    response = emotion_detector(text_to_analyze)
    # Extract emotion strings from response and arrange
    emotion_string = ""
    for key, value in response.items():
        if key != "dominant_emotion":
            value = format(value, 'f')
            emotion_string = emotion_string + "'" + key + "': " + value + ", "
    emotion_string = emotion_string[:-2]
    # Extract dominant emotion
    dominant_emotion = response["dominant_emotion"]
    # Form and return response string
    return_string = f"For the given statement, the system response is {emotion_string}."
    return_string = return_string + " The dominant emotion is {dominant_emotion}."
    return return_string

@app.route("/")
def render_index_page():
    """
        This function initiates the rendering of the index HTML page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
