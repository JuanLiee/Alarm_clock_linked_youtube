import time
import datetime
import webbrowser

alarm_time = input("Set the alarm time (HH:MM): ")

youtube_url = "https://www.youtube.com/watch?v=yZLfa7BT9nE"

try:

    alarm_hour, alarm_minute = map(int, alarm_time.split(":"))
    alarm_time_obj = datetime.time(hour=alarm_hour, minute=alarm_minute)
except ValueError:
    print("Invalid time format. Please use HH:MM format.")
    exit()

print(f"Alarm set for {alarm_time}...")

while True:
    
    now = datetime.datetime.now()
    current_time_obj = now.time()

    if current_time_obj.hour == alarm_hour and current_time_obj.minute == alarm_minute:
        print("Alarm ringing! Opening YouTube video...")
        webbrowser.open(youtube_url)
        break

    time.sleep(1)
