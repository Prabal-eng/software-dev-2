import tkinter as tk
from tkinter import ttk
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        self.master.geometry("400x300")
        self.master.resizable(False, False)

        self.style = ttk.Style()
        self.style.theme_use('clam')

        self.target_number = 0
        self.attempts = 0
        self.max_number = 100

        self.create_widgets()
        self.new_game()

    def create_widgets(self):
        # Title
        title_label = ttk.Label(self.master, text="Guess the Number!", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        # Frame for range selection
        range_frame = ttk.Frame(self.master)
        range_frame.pack(pady=5)

        ttk.Label(range_frame, text="Max Number:").pack(side=tk.LEFT)
        self.range_var = tk.StringVar(value="100")
        range_entry = ttk.Entry(range_frame, textvariable=self.range_var, width=5)
        range_entry.pack(side=tk.LEFT, padx=5)
        ttk.Button(range_frame, text="Set", command=self.set_range).pack(side=tk.LEFT)

        # Guess entry
        self.guess_var = tk.StringVar()
        guess_entry = ttk.Entry(self.master, textvariable=self.guess_var, font=("Arial", 14), width=10)
        guess_entry.pack(pady=10)
        guess_entry.bind('<Return>', lambda event: self.check_guess())

        # Guess button
        guess_button = ttk.Button(self.master, text="Guess", command=self.check_guess)
        guess_button.pack(pady=5)

        # Feedback label
        self.feedback_var = tk.StringVar(value="Guess a number and press Enter or click Guess!")
        feedback_label = ttk.Label(self.master, textvariable=self.feedback_var, font=("Arial", 12), wraplength=350)
        feedback_label.pack(pady=10)

        # Attempts label
        self.attempts_var = tk.StringVar(value="Attempts: 0")
        attempts_label = ttk.Label(self.master, textvariable=self.attempts_var)
        attempts_label.pack()

        # New Game button
        new_game_button = ttk.Button(self.master, text="New Game", command=self.new_game)
        new_game_button.pack(pady=10)

    def set_range(self):
        try:
            new_max = int(self.range_var.get())
            if new_max > 1:
                self.max_number = new_max
                self.new_game()
            else:
                self.feedback_var.set("Please enter a number greater than 1.")
        except ValueError:
            self.feedback_var.set("Please enter a valid number.")

    def new_game(self):
        self.target_number = random.randint(1, self.max_number)
        self.attempts = 0
        self.update_attempts()
        self.feedback_var.set(f"I'm thinking of a number between 1 and {self.max_number}. Can you guess it?")
        self.guess_var.set("")

    def check_guess(self):
        try:
            guess = int(self.guess_var.get())
            self.attempts += 1
            self.update_attempts()

            if guess < self.target_number:
                self.feedback_var.set("Too low! Try a higher number.")
            elif guess > self.target_number:
                self.feedback_var.set("Too high! Try a lower number.")
            else:
                self.feedback_var.set(f"Congratulations! You guessed the number {self.target_number} in {self.attempts} attempts!")
        except ValueError:
            self.feedback_var.set("Please enter a valid number.")

        self.guess_var.set("")  # Clear the guess entry

    def update_attempts(self):
        self.attempts_var.set(f"Attempts: {self.attempts}")

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
