import csv, datetime, time, os.path, tk
#import tkinter as tk
import customtkinter as ctk
from timeclock_functions import clock_in, clock_out, get_total_time, csv_file, get_last_time, check_for_csv

date = datetime.datetime.now().date()
last_time = ''

csv_file = r'~/repos/TimeClock/timeclock.csv'

flag = os.path.isfile(csv_file)
if flag:
    print(f"The file exists")
else:
    print("The file does not exist, creating file")
    with open('time_clocks.csv', 'w') as creating_new_file:
        pass
    print("New file created")

timeclock = ctk.CTk()
timeclock.geometry('400x240')

user_options = ["Katrina", "Clayton"]

combo = ctk.CTkComboBox(master = timeclock, state = "readonly", values = user_options)

in_button = ctk.CTkButton(master=timeclock, text='Clock In', command = clock_in)
out_button = ctk.CTkButton(master=timeclock, text='Clock Out', command = clock_out)

combo.pack(padx = 20, pady = 5)
in_button.pack(padx = 20, pady = 15)
out_button.pack(padx = 20, pady = 20)

get_last_time()

last_time_label = ctk.CTkLabel(master=timeclock, text = last_time, anchor = "center")

last_time_label.pack(padx = 20, pady = 10)

timeclock.mainloop()

#return_time
