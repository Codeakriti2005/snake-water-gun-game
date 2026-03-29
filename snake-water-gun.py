import tkinter as tk
import random
import pyttsx3

# Initialize voice engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Game choices
choices = ["Snake", "Water", "Gun"]

# Score variable
score = 0

# Decide winner
def decide_winner(user, computer):
    if user == computer:
        return "It's a Tie!"
    
    if (user == "Snake" and computer == "Water") or \
       (user == "Water" and computer == "Gun") or \
       (user == "Gun" and computer == "Snake"):
        return "You Win!"
    else:
        return "Computer Wins!"

# Play function
def play(user_choice):
    global score
    
    computer_choice = random.choice(choices)
    result = decide_winner(user_choice, computer_choice)
    
    # Update score
    if result == "You Win!":
        score += 1
    elif result == "Computer Wins!":
        score -= 1

    # Update labels
    label_user.config(text=f"Your Choice: {user_choice}")
    label_computer.config(text=f"Computer Choice: {computer_choice}")
    label_result.config(text=f"Result: {result}")
    score_label.config(text=f"Score: {score}")

    # Voice output
    speak(f"You chose {user_choice}")
    speak(f"Computer chose {computer_choice}")
    speak(result)

# Reset function
def reset_game():
    global score
    score = 0
    score_label.config(text="Score: 0")
    label_result.config(text="Result: ")
    speak("Game reset")

# GUI setup
root = tk.Tk()
root.title("Snake Water Gun Game")
root.geometry("400x450")

title = tk.Label(root, text="Snake Water Gun Game", font=("Arial", 16, "bold"))
title.pack(pady=10)

# Buttons
btn_snake = tk.Button(root, text="Snake 🐍", width=15, command=lambda: play("Snake"))
btn_snake.pack(pady=5)

btn_water = tk.Button(root, text="Water 💧", width=15, command=lambda: play("Water"))
btn_water.pack(pady=5)

btn_gun = tk.Button(root, text="Gun 🔫", width=15, command=lambda: play("Gun"))
btn_gun.pack(pady=5)

# Labels
label_user = tk.Label(root, text="Your Choice: ", font=("Arial", 12))
label_user.pack(pady=10)

label_computer = tk.Label(root, text="Computer Choice: ", font=("Arial", 12))
label_computer.pack(pady=10)

label_result = tk.Label(root, text="Result: ", font=("Arial", 14, "bold"))
label_result.pack(pady=10)

# Score label
score_label = tk.Label(root, text="Score: 0", font=("Arial", 14))
score_label.pack(pady=10)

# Reset button
reset_btn = tk.Button(root, text="Reset Game", command=reset_game)
reset_btn.pack(pady=10)

# Run app
root.mainloop()