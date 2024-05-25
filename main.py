from tkinter import *
from tkinter import messagebox
from word_bank import create_random_typing_test
from math import floor

timer = None
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 600
TIME_IN_MINUTES = 1


def start_timer():
    new_word_bank = create_random_typing_test()
    for word in new_word_bank:
        text_to_copy.insert(END, word + ' ')

    count_down(60 * TIME_IN_MINUTES)


def count_down(count):
    global timer

    if count >= 0:
        minutes = floor(count / 60)
        seconds = count % 60
        if seconds < 10:
            seconds = f"0{seconds}"

        time.config(text=f"Time Left: {minutes}:{seconds}")
        timer = window.after(1000, count_down, count - 1)

    # Timer is finished
    else:
        calculate_wpm()


def calculate_wpm():
    user_text = user_input.get("1.0", "end-1c").split(" ")
    prompt_text = text_to_copy.get("1.0", "end-1c").split(" ")[:len(user_text)]

    gross_wpm = (len(user_input.get("1.0", "end-1c")) / 5) / TIME_IN_MINUTES
    num_errors = calculate_errors(prompt_text, user_text)
    net_wpm = gross_wpm - (num_errors / TIME_IN_MINUTES)
    accuracy = ((len(user_text) - num_errors) / len(prompt_text)) * 100

    print(prompt_text)
    print(user_text)

    messagebox.showinfo(title='Its over!',
                        message=f"Test is over...\n"
                                f"WPM: {net_wpm}\n"
                                f"Accuracy: {floor(accuracy)}%")


def calculate_errors(prompt_text, user_text) -> int:
    errors = 0
    for i in range(len(prompt_text)):
        if user_text[i] != prompt_text[i]:
            errors += 1

    return errors


window = Tk()
window.title("Typing Speed Test")
window.config(padx=25, pady=25)
window.maxsize(WINDOW_HEIGHT, WINDOW_WIDTH)
window.minsize(WINDOW_HEIGHT, WINDOW_WIDTH)

title = Label(text='Typing Test')
title.grid(column=2, row=1)

time = Label(text='Time Left: 0')
time.grid(column=2, row=2)

text_to_copy = Text(height=10, width=85, wrap=WORD, padx=10, pady=10)
text_to_copy.grid(column=2, row=3)

# Create text widget and specify size.
user_input = Text(window, height=10, width=85, wrap=WORD, padx=10, pady=10)
user_input.grid(column=2, row=4)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=2, row=5)

window.mainloop()
