import tkinter as tk
from datetime import datetime
import threading

def load_card_to_employee_data(filename):
    employee_data = {}
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(", ")
            card_id = parts[0].split("：")[1].strip("{}")
            employee_id = parts[1].split("：")[1].strip("{}")
            name = parts[2].split("：")[1].strip("{}")
            employee_data[card_id] = (employee_id, name)
    return employee_data

card_to_employee_data = load_card_to_employee_data("card_to_employee.txt")

def update_time():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d-%A-%H:%M:%S")
    time_label.config(text=current_time)
    root.after(1000, update_time)  # 每秒更新時間

def record_entry(event):
    card_id = entry.get()
    employee_info = card_to_employee_data.get(card_id, ("未知", "未知"))
    employee_id, name = employee_info
    info_label.config(text=f"卡號：{card_id}, 工號：{employee_id}, 姓名：{name}")
    entry.delete(0, tk.END)

root = tk.Tk()
root.geometry("800x600")  # 設置窗口大小

time_label = tk.Label(root, font=('Helvetica', 18))
time_label.pack()

info_label = tk.Label(root, font=('Helvetica', 14))
info_label.pack()

entry = tk.Entry(root)
entry.bind("<Return>", record_entry)
entry.pack()
entry.focus_set()  # 在應用程式啟動時將焦點設置到輸入框

update_time()  # 初始化時間顯示
root.mainloop()
