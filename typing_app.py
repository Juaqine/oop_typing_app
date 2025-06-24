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

        self.show_home_screen()

    def show_home_screen(self):
        self.home_screen_frame = tk.Frame(self.window, bg=self.color_background)
        self.home_screen_frame.pack(fill="both", expand=True)

        tk.Label(
            self.home_screen_frame,
            text="Welcome to the PUP Typing Speed Test!",
            font=("Helvetica", 22, "bold"),
            fg=self.color_text,
            bg=self.color_background
        ).pack(pady=40)

        tk.Label(
            self.home_screen_frame,
            text="Press ENTER to start the game",
            font=("Helvetica", 14),
            fg=self.color_text,
            bg=self.color_background
        ).pack(pady=20)

        self.window.bind("<Return>", self.start_game)

    def start_game(self, event=None):
        self.window.unbind("<Return>")
        self.home_screen_frame.destroy()
        self.setup_typing_ui()

    def setup_typing_ui(self):
        self.typing_frame = tk.Frame(self.window, bg=self.color_background)
        self.typing_frame.pack(fill="both", expand=True)

        tk.Label(
            self.typing_frame,
            text="Typing Speed Test",
            font=("Helvetica", 20, "bold"),
            fg=self.color_text,
            bg=self.color_background
        ).pack(pady=10)

        self.sentence_label = tk.Label(
            self.typing_frame,
            text=self.current_sentence,
            wraplength=700,
            font=("Helvetica", 14),
            fg=self.color_text,
            bg=self.color_background
        )
        self.sentence_label.pack(pady=10)

        self.text_entry = tk.Entry(
            self.typing_frame,
            textvariable=self.input_text,
            font=("Helvetica", 14),
            width=90,
            fg=self.color_background,
            bg=self.color_text
        )
        self.text_entry.pack(pady=10)
        self.text_entry.bind("<Return>", self.process_result)
        self.text_entry.bind("<KeyPress>", self.start_timer_once)

        self.result_display = tk.Label(
            self.typing_frame,
            text="",
            font=("Helvetica", 12),
            fg=self.color_text,
            bg=self.color_background
        )
        self.result_display.pack(pady=10)

        self.instruction_label = tk.Label(
            self.typing_frame,
            text="Click the field, type the sentence, then press ENTER.",
            font=("Helvetica", 12, "italic"),
            fg=self.color_text,
            bg=self.color_background
        )
        self.instruction_label.pack(pady=5)

        self.restart_button = tk.Button(
            self.typing_frame,
            text="Restart",
            command=self.reset_test,
            font=("Helvetica", 12),
            bg=self.color_text,
            fg=self.color_background
        )
        self.restart_button.pack(pady=10)

        self.text_entry.focus()

    def start_timer_once(self, event):
        if self.start_time is None:
            self.start_time = time.time()

    def process_result(self, event):
        if self.start_time is None:
            return

        end_time = time.time()
        user_input = self.input_text.get()
        total_time = end_time - self.start_time

        words_per_minute = self.calculate_wpm(user_input, total_time)
        typing_accuracy = self.calculate_accuracy(user_input)

        result_text = f"Time: {round(total_time, 2)}s | WPM: {words_per_minute} | Accuracy: {typing_accuracy}%"
        self.result_display.config(text=result_text)

        self.text_entry.config(state='disabled')

    def calculate_wpm(self, user_input, total_time_seconds):
        words = user_input.strip().split()
        word_count = len(words)
        wpm = (word_count / total_time_seconds) * 60 if total_time_seconds > 0 else 0
        return round(wpm, 2)

    def calculate_accuracy(self, user_input):
        correct_characters = 0
        for index, character in enumerate(user_input):
            if index < len(self.current_sentence) and character == self.current_sentence[index]:
                correct_characters += 1
        accuracy_percentage = (correct_characters / len(self.current_sentence)) * 100
        return round(accuracy_percentage, 2)

    def reset_test(self):
        self.current_sentence = random.choice(self.get_typing_sentences())
        self.sentence_label.config(text=self.current_sentence)
        self.input_text.set("")
        self.result_display.config(text="")
        self.start_time = None
        self.text_entry.config(state='normal')
        self.text_entry.focus()

    def get_typing_sentences(self):
        return ["Default sentence for typing test."]

class TypingTest(TypingTestBase):
    def get_typing_sentences(self):
        return [
            "Di pinapansin ingay sa tabi magulong kapaligiran sayo lang ang tingin.",
            "Kung mananatili sayo minamahal kong estranghero.",
            "Pasindi na ng ilaw minumulto na ko ng damdamin ko.",
            "Hindi titigil hanggang ako na ang dahilan ng yong ngiting misteryoso."
        ]

if __name__ == "__main__":
    root_window = tk.Tk()
    typing_app = TypingTest(root_window)
    root_window.mainloop()
