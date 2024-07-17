import tkinter as tk
from tkinter import ttk

def submit_data():
    # Xử lý dữ liệu người dùng tại đây
    # In thông báo ra bảng điều khiển
    print("Data submitted successfully!")

window = tk.Tk()
window.geometry("500x400")

# Khung thông tin người dùng
user_info_frame = tk.Frame(window)
user_info_frame.pack()

first_name_label = tk.Label(user_info_frame, text="First Name:")
first_name_label.pack()

first_name_entry = tk.Entry(user_info_frame)
first_name_entry.pack()

last_name_label = tk.Label(user_info_frame, text="Last Name:")
last_name_label.pack()

last_name_entry = tk.Entry(user_info_frame)
last_name_entry.pack()

title_label = tk.Label(user_info_frame, text="Title:")
title_label.pack()

title_combobox = ttk.Combobox(user_info_frame, values=["Mr.", "Mrs.", "Ms.", "Dr."])
title_combobox.pack()

age_label = tk.Label(user_info_frame, text="Age:")
age_label.pack()

age_entry = tk.Entry(user_info_frame)
age_entry.pack()

nationality_label = tk.Label(user_info_frame, text="Nationality:")
nationality_label.pack()

nationality_entry = tk.Entry(user_info_frame)
nationality_entry.pack()

# Khung đăng ký
registration_frame = tk.Frame(window)
registration_frame.pack()

registration_status_checkbutton = tk.Checkbutton(registration_frame, text="Registration Status")
registration_status_checkbutton.pack()

completed_courses_label = tk.Label(registration_frame, text="Completed Courses:")
completed_courses_label.pack()

completed_courses_spinbox = tk.Spinbox(registration_frame, from_=0, to=10)
completed_courses_spinbox.pack()

semesters_label = tk.Label(registration_frame, text="Semesters:")
semesters_label.pack()

semesters_spinbox = tk.Spinbox(registration_frame, from_=0, to=10)
semesters_spinbox.pack()

# Khung Điều khoản và Điều kiện
terms_frame = tk.Frame(window)
terms_frame.pack()

terms_checkbutton = tk.Checkbutton(terms_frame, text="I accept the Terms & Conditions")
terms_checkbutton.pack()

# Nút Gửi
submit_button = tk.Button(window, text="Submit", command=submit_data)
submit_button.pack()

window.mainloop()