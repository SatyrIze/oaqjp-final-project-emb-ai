from typing import Dict
import requests, json # type: ignore



def emotion_detector(text_to_analyze: str) -> str:
    url: str = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers: Dict[str, str] = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj: Dict[str, Dict[str, str]] = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers = headers, timeout=5)
    formatted_response = json.loads(response.text)
    
    anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    
    emotions = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score
    }
    
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "scores": emotions,
        "dominant_emotion": dominant_emotion
    }