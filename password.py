import tkinter as tk
from tkinter import font
import random
import string

output_path = f'./password.txt'

# パスワードを生成
def create_password():
    password = ''.join(random.choices(string.ascii_letters + string.digits, 
        k=int(password_length_box.get())))
    Result_label['text'] = password

# テキストファイルにパスワードを保存
def save_password():
    with open(output_path, mode='a') as f:
        f.write(
            f"{title_box.get()}\n{account_box.get()}\n{Result_label['text']}\n\n"
        )

# ウィンドウの作成
win = tk.Tk()
win.title("パスワード生成アプリ")
win.geometry("300x300")
font1 = font.Font(family='メイリオ', size=10)


# 部品を作成
# タイトル
title_label = tk.Label(win, text=u'タイトル', font=font1)
title_label.pack()
title_box = tk.Entry(win)
title_box.pack()

# アカウント
account_label = tk.Label(win, text=u'アカウント', font=font1)
account_label.pack()
account_box = tk.Entry(win)
account_box.insert(tk.END, 'example@gmail.com')
account_box.pack()

# パスワードの長さ
password_length_label = tk.Label(win, text=u'パスワードの長さ', font=font1)
password_length_label.pack()
password_length_box = tk.Entry(win)
password_length_box.insert(tk.END, '8')
password_length_box.pack()


# 決定ボタン
create_password_Button = tk.Button(win, text=u'生成する', font=font1)
create_password_Button['command'] = create_password
create_password_Button.pack()

# 生成したパスワードを表示
Result_label = tk.Label(win, text=u'')
Result_label.pack()

# 保存ボタン
save_Button = tk.Button(win, text=u'保存する', font=font1)
save_Button['command'] = save_password
save_Button.pack()


# ウィンドウを動かす
win.mainloop()