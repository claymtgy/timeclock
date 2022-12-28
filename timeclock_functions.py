import csv
import datetime, time

date = datetime.datetime.now().date() 

def clock_in():
  date = datetime.datetime.now().strftime('%Y-%m-%d')
  time = datetime.datetime.now().strftime('%H:%M:%S')
  with open("time_clocks.csv", "a", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([date, time, "", ""])
  print(f"Clocked in at {time} on {date}")
  return date


def clock_out():
  date = datetime.datetime.now().strftime('%Y-%m-%d')
  time = datetime.datetime.now().strftime('%H:%M:%S')
  with open("time_clocks.csv", "r", newline="") as csvfile:
    reader = csv.reader(csvfile)
    rows = list(reader)
  with open("time_clocks.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    for row in rows:
      if row[0] == str(date) and row[1] != "" and row [2] == "":
        row[2] = time
      writer.writerow(row)
  print(f"Clocked out at {time} on {date}")

def get_total_time():
  total_time = 0 
  with open("time_clocks.csv", "r+", newline="") as csvfile:
    reader = csv.reader(csvfile)
    writer = csv.writer(csvfile)
    rows = list(reader)
  with open("time_clocks.csv", "w", newline="") as csvfile:
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
