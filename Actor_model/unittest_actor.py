import unittest
from actor_model import recognize_actor

class TestRecognizeActorFunction(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_recognize_actor_Simple_sentence(self): ## Simple sentence
        input_text = '''User can view profile'''
        expected_result = {
            'user': {'view profile'},
        }
        result = recognize_actor(input_text)
        self.assertEqual(result, expected_result)

    def test_recognize_actor_using_pronouns(self): ##Simple sentence
        input_text = '''User can view profile. They can also manage their book''' ##Using pronouns
        expected_result = {
            'user': {'view profile', 'manage their book book'},
        }
        result = recognize_actor(input_text)
        self.assertEqual(result, expected_result)

    def test_recognize_actor_2sentences_withoutactoron2nd(self): #2 sentences. 1 sentece with actor second without actor
        input_text = '''User can view profile. They can also manage their book'''
        expected_result = {
            'user': {'view profile', 'manage their book book'},
        }
        result = recognize_actor(input_text)
        self.assertEqual(result, expected_result)

    def test_recognize_actor_with_exception(self): # 1 sentence with exception
        input_text = '''User can view profile but user cannot view other profile'''
        expected_result = {
            'user': {'view profile'},
        }
        result = recognize_actor(input_text)
        self.assertEqual(result, expected_result)

    def test_recognize_actor_on_paragraph_with_each_actor(self): #paragraph with actor in each sentence
        input_text = '''Users must register first before using the telemedicine application. Users are patients who have received treatment at the hospital before and patients who are using the hospital's health services for the first time. Users can search for doctors based on the doctor's name or the name of the clinic / specialist. Next, the user sees the available telemedicine consultation schedule. Users can make a consultation if it coincides with an online doctor's practice or come back later according to the target doctor's schedule'''
        expected_result = {
            'user': {'view profile', 'manage their book book'},
        }
        result = recognize_actor(input_text)
        self.assertEqual(result, expected_result)

    def test_recognize_actor_multiple_actor(self): #2 actor in 1 sentence
        input_text = '''User and administrator can view profile'''
        expected_result = {
            'user': {'view profile'},
            'administrator': {'view profile'},
        }
        result = recognize_actor(input_text)
        self.assertEqual(result, expected_result)

    def test_recognize_actor_simple_2actor(self): # 1 sentence, 2 actor with exception
        input_text = '''User can view profile but user cannot view other profile'''
        expected_result = {
            'user': {'view profile'},
        }
        result = recognize_actor(input_text)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()