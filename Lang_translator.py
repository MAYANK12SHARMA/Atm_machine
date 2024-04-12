 #?                                     Topic :- Language Tranlator and speaker 

import googletrans as translator
from prettytable import PrettyTable
from gtts import gTTS
import os


class LanguageTranslator:
    def __init__(self, source_language, target_language, text_to_translate):
        self.translator_instance = translator.Translator()
        self.source_language = source_language
        self.target_language = target_language
        self.text_to_translate = text_to_translate
        self.translated_text = ''

    def translate_text(self):
        translated_text = self.translator_instance.translate(self.text_to_translate, dest=self.target_language)
        self.translated_text = translated_text.text
        return self.translated_text

    def get_translation_details(self):
        print('------------------------------------------------------------------------------')
        print(f'Original text({self.source_language}): {self.text_to_translate}')
        print('------------------------------------------------------------------------------')
        print(f'Translated text({self.target_language}): {self.translated_text}')
        print()
        print()

table = PrettyTable()
table.field_names = ["Language", "Codes"]

languages = [['English', 'en'], ['Spanish', 'es'], ['French', 'fr'], ['German', 'de'],['Italian','it'],
             ['Portuguese', 'pt'], ['Russian', 'ru'], ['Chinese (Simplified)', 'zh'],['Japanese', 'ja'],
             ['Korean', 'ko'], ['Arabic', 'ar'], ['Hindi', 'hi'],['Bengali', 'bn'], 
             ['Urdu', 'ur'], ['Swahili', 'sw'], ['Turkish', 'tr']]
table.add_rows(languages)

print(table)

s_language = input('Write the language code in which you want to write: ')
print()
text = input('Enter your text: ')
print()
c_language = input('Write the language code in which you want to convert the text: ')
print()

data = LanguageTranslator(s_language, c_language, text)

data.translate_text()
data.get_translation_details()

def text_to_speech(text, language=c_language, filename='output.mp3'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(filename)
    os.system(f'start {filename}')  # This will open the generated file with the default audio player

print('1. to listen the translated text.')
print('2. exit')
while True:
    cho = int(input('Enter your choice : '))
    if cho == 1:
        text_to_speech(data.translate_text())
    else:
        os.remove('output.mp3')
        break
