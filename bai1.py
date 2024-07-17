import tkinter as tk

window = tk.Tk()
window.geometry("600x300")
window.configure(bg="pink")

# Thêm nhãn tiêu đề lớn ở giữa
title_label = tk.Label(window, text="Frame Recorder", font=("Arial", 20))
title_label.pack()

# Thêm trường đầu vào cho FPS
fps_label = tk.Label(window, text="FPS (khung hình trên giây):")
fps_label.pack()

fps_entry = tk.Entry(window)
fps_entry.pack()

# Tạo hàng nút "Tạm dừng", "Bắt đầu" và "Kết thúc"
button_frame = tk.Frame(window)

pause_button = tk.Button(button_frame, text="Tạm dừng")
pause_button.pack(side="left")

start_button = tk.Button(button_frame, text="Bắt đầu")
start_button.pack(side="left")

end_button = tk.Button(button_frame, text="Kết thúc")
end_button.pack(side="left")

button_frame.pack()

# Thêm nhãn trạng thái
status_label = tk.Label(window, text="Recording Paused", font=("Arial", 12))
status_label.pack(side="bottom")

window.mainloop()