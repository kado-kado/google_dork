import tkinter as tk
from tkinter import ttk
import webbrowser

# Dorkテンプレート
dorks = {
    "ログインページ": ['intitle:"login"', 'inurl:admin', 'intitle:"admin login"'],
    "パスワードファイル": ['filetype:log intext:"password"', 'filetype:env "DB_PASSWORD"', 'filetype:conf intext:password'],
    "カメラ/Webカム": ['intitle:"Live View / - AXIS"', 'inurl:"viewerframe?mode="', 'inurl:"webcamxp"'],
    "インデックス公開": ['intitle:"index of" "backup"', 'intitle:"index of" ".git"', 'intitle:"index of" "mp3"'],
    "データベース管理ツール": ['intitle:"phpMyAdmin"', 'intitle:"Mongo Express"', 'intitle:"Adminer"'],
    "エラー/脆弱性情報": ['intext:"You have an error in your SQL syntax"', 'intext:"Warning: mysql_fetch_array()"', 'intext:"Fatal error"'],
}

history = []

# メインウィンドウ
root = tk.Tk()
root.title("Google Dork ツール")
root.geometry("700x500")

# 画面フレーム定義
frames = {}

def show_frame(name):
    for f in frames.values():
        f.pack_forget()
    frames[name].pack(pady=10)

# ステップ1: モード選択画面
frames["mode"] = tk.Frame(root)
tk.Label(frames["mode"], text="どちらの方法でDorkを作成しますか？", font=("Arial", 14)).pack(pady=20)
tk.Button(frames["mode"], text="テンプレートを使用", command=lambda: show_frame("template")).pack(pady=10)
tk.Button(frames["mode"], text="カスタムDorkを作成", command=lambda: show_frame("custom")).pack(pady=10)
tk.Label(frames["mode"], text="made by kado").pack(pady=20)

# ステップ2: テンプレート選択
frames["template"] = tk.Frame(root)
tk.Label(frames["template"], text="カテゴリを選んでください").pack()
combo_category = ttk.Combobox(frames["template"], values=list(dorks.keys()), width=50)
combo_category.pack()

tk.Label(frames["template"], text="テンプレートを選んでください").pack()
combo_dork = ttk.Combobox(frames["template"], width=60)
combo_dork.pack()

def update_dork_list(event):
    selected_category = combo_category.get()
    combo_dork['values'] = dorks.get(selected_category, [])
    if combo_dork['values']:
        combo_dork.current(0)

combo_category.bind("<<ComboboxSelected>>", update_dork_list)

result_var = tk.StringVar()

def use_template():
    dork = combo_dork.get()
    result_var.set(dork)
    if dork not in history:
        history.append(dork)

    show_frame("result")

tk.Button(frames["template"], text="テンプレートを使用", command=use_template).pack(pady=10)

# ステップ3: カスタムDork作成
frames["custom"] = tk.Frame(root)
tk.Label(frames["custom"], text="カスタムキーワード（カンマ区切り）").pack()
entry_keywords = tk.Entry(frames["custom"], width=80)
entry_keywords.pack()

tk.Label(frames["custom"], text="検索タイプ").pack()
dork_type = ttk.Combobox(frames["custom"], values=["intitle", "inurl", "intext", "filetype", "site", "text"], width=20)
dork_type.set("intitle")
dork_type.pack()

tk.Label(frames["custom"], text="キーワード間の論理演算子").pack()
logic_operator = ttk.Combobox(frames["custom"], values=["AND", "OR"], width=10)
logic_operator.set("AND")
logic_operator.pack()

def generate_dork():
    keywords = entry_keywords.get().split(",")
    field = dork_type.get()
    operator = logic_operator.get()

    dork_parts = []
    for word in keywords:
        word = word.strip()
        if field == "text":
            dork_parts.append(f'"{word}"')
        else:
            dork_parts.append(f'{field}:"{word}"')

    dork_query = f" {operator} ".join(dork_parts)
    result_var.set(dork_query)

    if dork_query not in history:
        history.append(dork_query)

    show_frame("result")

tk.Button(frames["custom"], text="カスタムDorkを生成", command=generate_dork).pack(pady=10)

# ステップ4: 結果表示 + 検索
frames["result"] = tk.Frame(root)
tk.Label(frames["result"], text="生成されたDorkクエリ").pack()
entry_result = tk.Entry(frames["result"], textvariable=result_var, width=100)
entry_result.pack()

def search():
    query = result_var.get()
    if query:
        webbrowser.open(f"https://www.google.com/search?q={query}")

tk.Button(frames["result"], text="Googleで検索", command=search).pack(pady=10)
tk.Button(frames["result"], text="最初に戻る", command=lambda: show_frame("mode")).pack()

# 最初の画面表示
show_frame("mode")

root.mainloop()