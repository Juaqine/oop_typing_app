#Imports GUI, timer, and random sentence logic..
#A class wraps everything — the typing test, the UI, the score logic.
#Window shows a title, sentence, entry box, and some gold-and-maroon style PUP colors.
#Picks a random sentence from a list, waits for the user to type.
#Timer starts only when the first key is pressed.
#When Enter is hit, it checks how fast and how accurate the typing was.
#WPM is calculated based on how many words were typed per minute.
#Accuracy checks how many letters match the original sentence character-by-character.
#A reset button lets the user try again with a new sentence.
#Sentences are stored in a separate method.
#Another class inherits the base one just to swap in the Cup of Joe lines.
#Whole app runs inside a single window when the file is executed.

import tkinter as tk
import random
import time

class TypingTestBase:
    def __init__(self, window):
        self.window = window
        self.window.title("Typing Speed Test")
        self.window.geometry("800x400")

        self.color_background = "#800000"
        self.color_text = "#FFD700"
        self.window.config(bg=self.color_background)

        self.input_text = tk.StringVar()
        self.start_time = None
        self.typing_sentences = self.get_typing_sentences()
        self.current_sentence = random.choice(self.typing_sentences)

        self.home_screen_frame = None
        self.typing_frame = None
