import nltk
import pyttsx3
from pocketsphinx import LiveSpeech

def main():
    start_phrase = "hey, speech"
    for start_phrase in LiveSpeech(): 
        print(start_phrase)

if __name__ == "__main__":
    main()