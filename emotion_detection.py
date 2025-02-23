"""
   Emotion Detection using IBM Watson AI
"""

# Imports
import json
import requests

def emotion_detector(text_to_analyze):
    """
       Make call to IBM Watson AI Emotion Detection.  
       Return response with score for emotions in dictionary format.
       Include dominant emotion.
    """
    # Configure URL, header and text input to send in request
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    text_input = {"raw_document": {"text": text_to_analyze}}
    # Send request to Watson AI
    response = requests.post(url, json=text_input, headers=header, timeout=30)
    # Format response to JSON
    response_formatted = json.loads(response.text)
    # Extract emotions from JSON formatted response
    emotions = response_formatted["emotionPredictions"][0]["emotion"]
    # Extract emotion scores
    anger = emotions["anger"]
    disgust = emotions["disgust"]
    fear = emotions["fear"]
    joy = emotions["joy"]
    sadness = emotions["sadness"]
    # Create new scores dictionary
    scores = {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy, 'sadness': sadness}
    # Determine dominant emotion
    dominant_emotion_score = 0.0
    dominant_emotion = " "
    for k, v in scores.items():
        if v > dominant_emotion_score:
            dominant_emotion_score = v
            dominant_emotion = k
    # Append dominant emotion to scores dictionary        
    scores["dominant_emotion"] = dominant_emotion
    # Return scores dictionary
    return scores
