import tkinter as tk
from tkinter import messagebox
from datetime import datetime


def add_log():
    """

    :return: str
    """
    log_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    log_type = log_type_var.get()
    log_content = log_text.get("1.0", tk.END).strip()

    with open("mylog.txt", "r") as f:
        content = f.read()

    # if content.startswith(log_time[:10]):
    #     sep = ""
    # else:
    #     sep = "*"*50 + "\n"
    sep = ""
    log = f"{sep}{log_time} [{log_type}] {log_content}\n{content}"
    with open("mylog.txt", "w") as f:
        f.write(log)

    log_type_var.set("INFO")
    log_text.delete("1.0", tk.END)
    tk.messagebox.showinfo("提示", "日志添加成功！")


root = tk.Tk()
root.title("项目日志")
root.geometry("400x300")

header = tk.Label(root, text="添加日志", font=("Arial", 16))
header.pack(pady=10)

time_label = tk.Label(root, text=f"时间：{datetime.now().strftime('%Y-%m-%d %H:%M')}")
time_label.pack()

log_type_var = tk.StringVar(root, "INFO")
log_type_label = tk.Label(root, text="修改类型：")
log_type_label.pack()
log_type_menu = tk.OptionMenu(root, log_type_var, "INFO", "ERROR", "DEBUG")
log_type_menu.pack()

log_content_label = tk.Label(root, text="内容：")
log_content_label.pack()
log_text = tk.Text(root, height=5)
log_text.pack()

add_button = tk.Button(root, text="添加日志", command=add_log, width=10)
add_button.pack(pady=10)

root.mainloop()



