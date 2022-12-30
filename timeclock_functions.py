import csv
import datetime, time

date = datetime.datetime.now().date() 
csv_file = r'~/repos/TimeClock/timeclocks.csv'

user = ''
def get_last_time():
  print("1")
  if f"time_clocks{user}.csv":
    with open(f"time_clocks{user}.csv", "r", newline="") as csvfile:
      reader = csv.reader(csvfile)
      rows = list(reader)
      if rows:
        last_time = rows[-1]
        print(last_time)
        return last_time
      else:
        last_time = "No previous time recorded"
        return last_time
  else:
    last_time = "No User"
    return last_time

def check_for_csv():
  print("2")
  flag = os.path.isfile(csv_file)
  if flag:
    print(f"The file exists")
  else:
    print("The file does not exist, creating file")
    with open(csv_file,'w') as creating_new_file:
      pass
    print("New file created")
#  get_last_time()

def clock_in():
  print("3")
  date = datetime.datetime.now().strftime('%Y-%m-%d')
  time = datetime.datetime.now().strftime('%H:%M:%S')
  with open(f"time_clocks{user}.csv", "a", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([date, time, "", ""])
  print(f"Clocked in at {time} on {date}")
  return date

def clock_out():
  print("4")
  date = datetime.datetime.now().strftime('%Y-%m-%d')
  time = datetime.datetime.now().strftime('%H:%M:%S')
  with open(f"time_clocks{user}.csv", "r", newline="") as csvfile:
    reader = csv.reader(csvfile)
    rows = list(reader)
  with open(f"time_clocks{user}.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    for row in rows:
      if row[0] == str(date) and row[1] != "" and row [2] == "":
        row[2] = time
        writer.writerow(row)
  print(f"Clocked out at {time} on {date}")
  get_total_time()
#  last_time_label.config(text=last_time)

def get_total_time():
  print("5")
  total_time = 0 
  with open(f"time_clocks{user}.csv", "r+", newline="") as csvfile:
    reader = csv.reader(csvfile)
    writer = csv.writer(csvfile)
    rows = list(reader)
  with open(f"time_clocks{user}.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    for row in rows:
      if row[0] == str(date):
        clock_in_time = datetime.datetime.strptime(row[1], "%H:%M:%S")
        clock_out_time = datetime.datetime.strptime(row[2], "%H:%M:%S")
        total_time = clock_out_time - clock_in_time
        print(total_time)
        row[3] = total_time
      writer.writerow(row)
  return total_time
  print(total_time)
