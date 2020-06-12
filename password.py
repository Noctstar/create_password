import tkinter as tk
import random
import string
import pyperclip

password_length = 8

# ボタンを押したときの処理
def create_password():
    # パスワードの生成
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=password_length))
    Result_label['text'] = password
    pyperclip.copy(password)

# ウィンドウの作成
win = tk.Tk()
win.title("パスワード生成アプリ")
win.geometry("400x300")

# 部品を作成
# テキスト
text = tk.Label(win, text=u'パスワードを作成します。')
text.pack()

# タイトル
title_label = tk.Label(win, text=u'タイトル')
title_label.pack()
title_box = tk.Entry(win)
title_box.pack()

# アカウント
account_label = tk.Label(win, text=u'アカウント')
account_label.pack()
account_box = tk.Entry(win)
account_box.insert(tk.END, 'example@gmail.com')
account_box.pack()

# パスワードの長さ
password_length_label = tk.Label(win, text=u'パスワードの長さ')
password_length_label.pack()
password_length_box = tk.Entry(win)
password_length_box.insert(tk.END, '8')
password_length_box.pack()

# 入力情報を取得
title = title_box.get()
account = account_box.get()
password_length = int(password_length_box.get())

# 決定ボタン
create_password_Button = tk.Button(win, text=u'生成する')
create_password_Button["command"] = create_password
create_password_Button.pack()

# 生成したパスワードを表示
Result_label = tk.Label(win, text=u'')
Result_label.pack()

# 保存ボタン
save_Button = tk.Button(win, text=u'保存する')
# save_Button["command"] = 
save_Button.pack()


# ウィンドウを動かす
win.mainloop()