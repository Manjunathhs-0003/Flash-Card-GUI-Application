from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("ENTER THE PATH TO YOUR words_to_learn FILE (Enter the full path of the csv file)")
except FileNotFoundError:
    original_data = pandas.read_csv("ENTER THE PATH TO YOUR french_words FILE (Enter the full path of the csv file)")
    to_learn = original_data.to_dict(orient = "records")
else:
    to_learn = data.to_dict(orient="records") 


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text = "French", fill = "black")
    canvas.itemconfig(card_word, text = current_card["French"], fill = "black")
    canvas.itemconfig(card_bg, image = card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text = "English", fill = "white")
    canvas.itemconfig(card_word, text = current_card["English"], fill = "white")
    canvas.itemconfig(card_bg, image = card_back_img)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("ENTER THE PATH TO YOUR words_to_learn FILE (Enter the full path of the csv file)", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="ENTER THE PATH TO YOUR card_front IMAGE FILE (Enter the full path of the .png file)")
card_back_img = PhotoImage(file = "ENTER THE PATH TO YOUR card_back IMAGE FILE (Enter the full path of the .png file)")
card_bg = canvas.create_image(400, 263,image = card_front_img)
card_title = canvas.create_text(400, 150,text="Title",font=("Ariel", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263,text="Word", font=("Ariel", 60, "bold"), fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="ENTER THE PATH TO YOUR wrong IMAGE FILE (Enter the full path of the .png file)")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card, highlightbackground=BACKGROUND_COLOR)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="/ENTER THE PATH TO YOUR right IMAGE FILE (Enter the full path of the .png file)")
know_button = Button(image=check_image, highlightthickness=0, command=is_known, highlightbackground=BACKGROUND_COLOR)
know_button.grid(row=1, column=1)

next_card()

window.mainloop()
