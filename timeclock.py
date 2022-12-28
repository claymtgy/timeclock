import csv, datetime, time, tk
#import tkinter as tk
import customtkinter as ctk
from timeclock_functions import clock_in, clock_out, get_total_time

date = datetime.datetime.now().date()

timeclock = ctk.CTk()
timeclock.geometry('400x240')

in_button = ctk.CTkButton(master=timeclock, text='Clock In', command = clock_in)
out_button = ctk.CTkButton(master=timeclock, text='Clock Out', command = clock_out)

in_button.place(relx = 0.5, rely = 0.25, anchor = "center")
out_button.place(relx = 0.5, rely = 0.5, anchor = "center")

clock_in()
time.sleep(1)
clock_out()
get_total_time()

## Get the last total time
with open("time_clocks.csv", "r", newline="") as csvfile:
    reader = csv.reader(csvfile)
    rows = list(reader)
    last_time = rows[-1]
    print(last_time)

#last_time = 
last_time_label = ctk.CTkLabel(master=timeclock, text = last_time, anchor = "center")

last_time_label.place(relx = 0.5, rely = .10, anchor = "center")

timeclock.mainloop()
