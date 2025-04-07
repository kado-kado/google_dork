import tkinter as tk
from tkinter import ttk
import webbrowser

dorks = {
    "ログインページ": [
        'intitle:"login"',
        'inurl:admin',
        'intitle:"admin login"',
    ],
    "パスワードファイル": [
        'filetype:log intext:"password"',
        'filetype:env "DB_PASSWORD"',
        'filetype:conf intext:password',
    ],
    "カメラ/Webカム": [
        'intitle:"Live View / - AXIS"',
        'inurl:"viewerframe?mode="',
        'inurl:"webcamxp"',
    ],
    "インデックス公開": [
        'intitle:"index of" "backup"',
        'intitle:"index of" ".git"',
        'intitle:"index of" "mp3"',
    ],
    "データベース管理ツール": [
        'intitle:"phpMyAdmin"',
        'intitle:"Mongo Express"',
        'intitle:"Adminer"',
    ],
    "エラー/脆弱性情報": [
        'intext:"You have an error in your SQL syntax"',
        'intext:"Warning: mysql_fetch_array()"',
        'intext:"Fatal error"',
    ]
}

def search():
    category = combo_category.get()
    dork = combo_dork.get()
    query = entry_custom.get()
    if query:
        url = f"https://www.google.com/search?q={query}"
    else:
        url = f"https://www.google.com/search?q={dork}"
    webbrowser.open(url)

def update_dork_list(event):
    selected_category = combo_category.get()
    combo_dork['values'] = dorks.get(selected_category, [])
    combo_dork.current(0)

# UI
root = tk.Tk()
root.title("Google Dorking Tool")
root.geometry("500x250")

tk.Label(root, text="カテゴリ選択:").pack()
combo_category = ttk.Combobox(root, values=list(dorks.keys()))
combo_category.pack()
combo_category.bind("<<ComboboxSelected>>", update_dork_list)

tk.Label(root, text="テンプレートから選ぶ:").pack()
combo_dork = ttk.Combobox(root)
combo_dork.pack()

tk.Label(root, text="または任意のDorkを入力:").pack()
entry_custom = tk.Entry(root, width=60)
entry_custom.pack()

btn = tk.Button(root, text="Googleで検索", command=search)
btn.pack(pady=10)

root.mainloop()
