import tkinter as tk
from tkinter import messagebox

# Вспомогательная функция для добавления текста и сброса при повторном нажатии
def add_or_reset_text(new_text, state_var):
    if state_var.get():
        label.config(text="За кого ты дон:")
        state_var.set(False)
    else:
        current_text = label.cget("text")
        label.config(text=f"{current_text} {new_text}")
        state_var.set(True)

# Функция для обработки нажатия на кнопку "Чотам"
def handle_chotam():
    user_input = entry.get().strip()
    if user_input == "Извененья":
        messagebox.showinfo("Ответ", "щас братья по вере подъедут дон")
    else:
        messagebox.showinfo("Ответ", "Извененья")

# Создание основного окна
root = tk.Tk()
root.title("Подайте пятак червонца")

# Создание метки (label)
label = tk.Label(root, text="За кого ты дон =", font=("Arial", 16))
label.grid(row=0, column=0, pady=20, padx=10)

# Переменные состояния для кнопок
state_var1 = tk.BooleanVar(value=False)
state_var2 = tk.BooleanVar(value=False)

# Создание кнопок
button1 = tk.Button(root, text="уважженья", command=lambda: add_or_reset_text("уважженья", state_var1), font=("Arial", 14))
button1.grid(row=1, column=0, pady=10, padx=10)

button2 = tk.Button(root, text="42 братуха дон", command=lambda: add_or_reset_text("42 братуха", state_var2), font=("Arial", 14))
button2.grid(row=2, column=0, pady=10, padx=10)

button3 = tk.Button(root, text="драца будешь дон", command=lambda: add_or_reset_text("я еже братьев позову дон", state_var2), font=("Arial", 14))
button3.grid(row=3, column=0, pady=10, padx=10)

button4 = tk.Button(root, text="дон братья по вере кто", command=lambda: add_or_reset_text("Магомед Ахмед Айдар Султан брат", state_var2), font=("Arial", 14))
button4.grid(row=4, column=0, pady=10, padx=10)

# Создание поля для ввода текста
entry = tk.Entry(root, width=50, font=("Arial", 14))
entry.grid(row=0, column=1, rowspan=5, pady=10, padx=10)

# Создание кнопки "Чотам"
button_chotam = tk.Button(root, text="Чотам", command=handle_chotam, font=("Arial", 14))
button_chotam.grid(row=5, column=1, pady=10, padx=10)

# Запуск основного цикла событий
root.mainloop()
