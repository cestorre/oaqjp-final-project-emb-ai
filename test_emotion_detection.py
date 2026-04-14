import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        # Caso 1: Alegría
        res_1 = emotion_detector('I am glad this happened')
        self.assertEqual(res_1['dominant_emotion'], 'joy')
        
        # Caso 2: Rabia
        res_2 = emotion_detector('I am really mad about this')
        self.assertEqual(res_2['dominant_emotion'], 'anger')
        
        # Caso 3: Asco
        res_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(res_3['dominant_emotion'], 'disgust')
        
        # Caso 4: Tristeza
        res_4 = emotion_detector('I am so sad about this')
        self.assertEqual(res_4['dominant_emotion'], 'sadness')
        
        # Caso 5: Miedo
        res_5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(res_5['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()