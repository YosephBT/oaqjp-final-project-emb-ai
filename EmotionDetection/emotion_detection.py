import requests 
import json



def emotion_detector(text_to_analyse):
    """
    Module Name: em_detector

    Description:
        A brief description of what this module does. Explain its purpose, 
        functionality, and any important details that users should know.

    Usage:
        Provide examples of how to use the functions or classes in this module.

    Author: Yoseph
    Date: 2025
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } } 
    response = requests.post(url, json = myobj, headers=header)  
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        anger = emotions['anger']
        disgust = emotions['disgust']
        fear = emotions['fear']
        joy = emotions['joy']
        sadness = emotions['sadness']
        dominant_emotion = max(emotions, key=emotions.get)
    elif response.status_code == 400:
        emotions = None
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        dominant_emotion = None


    return {'anger':anger,'disgust':disgust,'fear':fear,'joy':joy,'sadness':sadness,'dominant_emotion':dominant_emotion}