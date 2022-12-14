from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    #once you click the reset button
    #timer_text "00:00"
    canvas.itemconfig(timer_text, text="00:00")
    #title_label
    title_label.config(text="Timer")
    #reset check_marks
    check_marks.config(text="")
    #
    global reps
    reps =0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
     global reps
     reps += 1
     work_sec = WORK_MIN * 60
     short_break_sec = SHORT_BREAK_MIN * 60
     long_break_sec = LONG_BREAK_MIN * 60

     #if it's the 1st/3rd/5th/7th rep:
     if reps % 8 == 0:
         # if it's  the 8th rep:
         count_down(long_break_sec)
         title_label.config(text="Long Break",fg=RED)
     elif reps % 2 == 0:
         #if it's 2nd/4th/6th rep:
         count_down(short_break_sec)
         title_label.config(text="Short Break", fg=GREEN)
     else:
         count_down(work_sec)
         title_label.config(text="Work Time", fg=YELLOW)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    #setting the string in the start as "05:00"
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    #the after work like (time, function, argument)
    if count > 0:
        global timer
        timer = window.after(1000, count_down,count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✅"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
#the "bg"  stand for background
window.config(padx=100, pady=50, bg=PINK)
#label for timer
title_label = Label(text="Timer", fg=YELLOW, bg=PINK, font=(FONT_NAME,55, "bold"))
title_label.grid(column=1, row=0)
text = "✔"
#creating the canvas same the size of the image of tomato
#the "bg"  stand for background, chaaning the background of the canvas
#the "highlightthickness" is used to remove the boarder of the image as the same color of the bg
canvas = Canvas(width=200,height=224, bg=PINK, highlightthickness=0)
#we will use the PhotoImage lass of tkinter to load the image
tomato_img = PhotoImage(file="tomato.png")
#adding the image
#but we can't add the image name or path directly here
canvas.create_image(100, 112, image=tomato_img)

#creating text layer over the image
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=("counter",40, "bold"))
canvas.grid(column=1, row=1)

#Creating buttons
#Start button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
#Reset Button
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

#check marks
check_marks = Label(fg=YELLOW, bg=PINK)
check_marks.grid(column=1, row=3)



window.mainloop()