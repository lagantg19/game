import random
from words import word_list
from gtts import gTTS
import os
def voice(given_word):
    my = given_word
    langg = "en"
    output = gTTS(text=my, lang=langg, slow=False)
    output.save("output.mp3")
    os.system("start output.mp3")

print("wel come to the game ")

lives = 6
correct = 6
while (lives > 0):
     given_word = random.choice(word_list)
     voice(given_word)
     taken_word = input("enter the word")
     if given_word == taken_word:
         correct = correct-1
         print(f"you said it correctly and you have to say {correct} words to win the game")
         if correct == 6:
             lives = 0
     else:
         lives = lives - 1
         print(f"you spelled wrong and you have {lives} chance to say ")





