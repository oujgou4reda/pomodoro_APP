from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 * 60
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 20 * 60
reps = 0
timer = None


# --------------------------- TIMER MECHANISM ------------------------------- #
def start():
    global reps
    reps += 1

    # Check the type of session (Work/Break) based on reps counter
    if reps % 2 == 0:  # Even reps indicate a Break session
        count_down(SHORT_BREAK_MIN)
        title_label.config(text="Break Time", fg=PINK)
    elif reps % 2 != 0:  # Odd reps indicate a Work session
        count_down(WORK_MIN)
        title_label.config(text="Work Time", fg=GREEN)
    elif reps % 8 == 0:  # Every 8th rep indicates a Long Break session
        count_down(LONG_BREAK_MIN)
        title_label.config(text="Break Time", fg=RED)

    # Update check label with completed sessions
    if reps % 2 == 0:
        session = int(reps / 2)
        check_label.config(text="✔" * session)


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    global reps
    minute = '%02d' % int(count / 60)
    sec = '%02d' % int(count % 60)
    time = minute + ":" + sec
    canvas.itemconfig(timer_text, text=time)

    if count > 0:
        # Continue the countdown by scheduling the next call to count_down after 1 second
        timer = window.after(1000, count_down, count - 1)
    else:
        # If the countdown is complete, start the next session
        start()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

# Create the Tomato image canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Create the labels and buttons
title_label = Label(window, text="Timer", font=(FONT_NAME, 70, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(row=0, column=1)

start_button = Button(window, text="start", highlightbackground=YELLOW, command=start)
start_button.grid(row=2, column=0)

reset_button = Button(window, text="reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

check_label = Label(window, font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
check_label.grid(row=3, column=1)

window.mainloop()
