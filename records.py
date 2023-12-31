import tkinter as tk
from datetime import datetime, timedelta
import pandas as pd
import threading

def load_card_to_employee_data(filename):
    employee_data = {}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(", ")
            card_id = parts[0].split("：")[1].strip("{}")
            employee_id = parts[1].split("：")[1].strip("{}")
            name = parts[2].split("：")[1].strip("{}")
            employee_data[card_id] = (employee_id, name)
    return employee_data

card_to_employee_data = load_card_to_employee_data("card_to_employee.txt")
attendance_records = {}

def update_time():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d-%A-%H:%M:%S")
    time_label.config(text=current_time)
    root.after(1000, update_time)

def record_entry(event):
    global attendance_records
    card_id = entry.get()
    timestamp = datetime.now()
    employee_info = card_to_employee_data.get(card_id, ("未知", "未知"))
    employee_id, name = employee_info
    if card_id not in attendance_records:
        attendance_records[card_id] = {'上班時間': timestamp, '下班時間': None}
    else:
        attendance_records[card_id]['下班時間'] = timestamp
    info_label.config(text=f"卡號：{card_id}, 工號：{employee_id}, 姓名：{name}")
    entry.delete(0, tk.END)

def auto_export_to_excel():
    date_str = datetime.now().strftime("%Y%m%d")
    export_path = f"{date_str}_attendance.xlsx"
    df = pd.DataFrame.from_dict(attendance_records, orient='index')
    df.to_excel(export_path)

def calculate_seconds_until(schedule_time_str):
    now = datetime.now()
    schedule_time = datetime.strptime(schedule_time_str, '%H:%M').replace(year=now.year, month=now.month, day=now.day)
    if schedule_time < now:
        schedule_time += timedelta(days=1)
    return (schedule_time - now).total_seconds()

export_time = "17:00"  # 可自訂的下班時間
threading.Timer(calculate_seconds_until(export_time), auto_export_to_excel).start()

root = tk.Tk()
root.geometry("800x600")

time_label = tk.Label(root, font=('Helvetica', 18))
time_label.pack()

info_label = tk.Label(root, font=('Helvetica', 14))
info_label.pack()

entry = tk.Entry(root)
entry.bind("<Return>", record_entry)
entry.pack()
entry.focus_set()

update_time()
root.mainloop()
