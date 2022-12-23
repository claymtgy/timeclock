import csv
import datetime, time

date = datetime.datetime.now().date() 

def clock_in():
  date = datetime.datetime.now().date()
  time = datetime.datetime.now().time()
  with open("time_clocks.csv", "a", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([date, time, ""])
  print(f"Clocked in at {time} on {date}")
  return date


def clock_out():
  date = datetime.datetime.now().date()
  time = datetime.datetime.now().time()
  with open("time_clocks.csv", "r", newline="") as csvfile:
    reader = csv.reader(csvfile)
    rows = list(reader)
  with open("time_clocks.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    for row in rows:
      if row[0] == str(date) and row[1] != "":
        row[2] = time
      writer.writerow(row)
  print(f"Clocked out at {time} on {date}")

print(date)
clock_in()
time.sleep(5)
clock_out()
print("done!")

def get_total_time(date):
  total_time = 0 
  with open("time_clocks.csv", "r", newline="") as csvfile:
    reader = csv.reader(csvfile)
    rows = list(reader)
  for row in rows:
    if row[0] == str(date):
      clock_in_time = datetime.datetime.strptime(row[1], "%H:%M:%S").time()
      clock_out_time = datetime.datetime.strptime(row[2], "%H:%M:%S").time()
      total_time += datetime.datetime.combine(date, clock_out_time) - datetime.datetime.combine(date, clock_in_time)
  return total_time

get_total_time(date)
print(total_time)
