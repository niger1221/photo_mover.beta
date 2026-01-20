import os
import shutil

import customtkinter as ctk
from tkinter import filedialog

ctk.set_appearance_mode('System')
ctk.set_default_color_theme('dark-blue')

app = ctk.CTk()
app.geometry('600x400')
app.title('PhotoMover/beta')

info = ctk.CTkLabel(master=app, text='', wraplength=200)
info.place(relx=0.6, rely=0.1)
paths = {'from': '', 'to': ''}
photo_extensions = ('.png', '.jpg', '.jpeg', '.webp')

btn_from = ctk.CTkButton(master=app, text='Папка откуда: ', command=lambda: select_path('from'))
btn_to = ctk.CTkButton(master=app, text='Папка куда: ', command=lambda: select_path('to'))


def select_path(key):
    path = filedialog.askdirectory()
    if path:
        paths[key] = path
        info.configure(text=f"Откуда: {paths['from']}\nКуда: {paths['to']}")


def show_file_menu():
    btn_from.place(relx=0.55, rely=0.5, anchor='center')
    btn_to.place(relx=0.85, rely=0.5, anchor='center')
    btn_start.place(relx=0.7, rely=0.6, anchor='center')
    info.configure(text='Выберите папки')


def start_moving():
    src = paths['from']
    dst = paths['to']

    if not src or not dst:
        info.configure(text='Выберите ОБЕ папки')
        return
    try:
        files = os.listdir(src)
        moved_count = 0
        for file in files:
            if file.lower().endswith(photo_extensions):
                old_path = os.path.join(src, file)
                new_path = os.path.join(dst, file)

                shutil.move(old_path, new_path)
                moved_count += 1
        info.configure(text=f'Успешно! Файлов перенесено: {moved_count}')
    except Exception as e:
        info.configure(f'Ошибка! {e}')


btn_start = ctk.CTkButton(master=app, text='ПЕРЕНЕСТИ', command=start_moving)


def show_about_page():
    btn_from.place_forget()
    btn_to.place_forget()
    btn_start.place_forget()
    info.configure(text='PhotoMover. Программа для переноса фото. Beta-версия')


buttons_data = [
    ('Файлы', show_file_menu),
    ('О проекте', show_about_page)
]

for i, (name, func) in enumerate(buttons_data):
    btn = ctk.CTkButton(master=app, text=name, command=func)
    btn.place(relx=0.2, rely=0.1 + (i * 0.15), anchor='center')

app.mainloop()
