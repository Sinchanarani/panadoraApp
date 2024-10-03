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
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    timer_label.config(text="WORK")
    check_mark.config(text="")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    if reps%8==0:
        count_down(long_break_sec)
        timer_label.config(text="LONG BREAK",fg=RED)
    elif reps%2==0:
        count_down(short_break_sec)
        timer_label.config(text="SHORT BREAK",fg=PINK)
        timer_label.place(x=25,y=-45)
    else:
        count_down(work_sec)
        timer_label.config(text="WORK",fg=GREEN)
        timer_label.place(x=75,y=-45)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_min = math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        mark=""
        work_session=math.floor(reps/2)
        for _ in range(work_session):
            mark+="✔"
        check_mark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas=Canvas(width=202,height=224,bg=YELLOW,highlightthickness=0)

tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.pack()

timer_label=Label(text="Timer",font=("century gothic",20,"bold"),bg=YELLOW,fg=GREEN)
timer_label.place(x=75,y=-45)

start_button=Button(text="Start",command=start_timer)
start_button.place(x=-45,y=230)

reset_button=Button(text="Reset",command=reset_timer)
reset_button.place(x=220,y=230)

check_mark=Label(text="✔",fg=GREEN)
check_mark.place(x=110,y=230)

window.mainloop()