import tkinter as tk
from tkinter import ttk
import json

class HymnApp:
    def __init__(self, master):
        self.master = master
        master.title("Hymn Search")
        master.geometry("1000x400")

        # 上部区块 - 查询功能
        self.search_frame = ttk.Frame(master, padding="10")
        self.search_frame.pack(fill=tk.X)

        self.search_label = ttk.Label(self.search_frame, text="输入诗歌编号:")
        self.search_label.pack(side=tk.LEFT)

        self.search_entry = ttk.Entry(self.search_frame, width=10)
        self.search_entry.pack(side=tk.LEFT, padx=5)

        # 替换单个搜索按钮为四个不同的按钮
        self.search_buttons = []
        button_texts = ["诗歌本", "补充本", "新诗", "紅本新诗", "藍本新诗"]
        for text in button_texts:
            button = ttk.Button(self.search_frame, text=text, command=lambda t=text: self.search_hymn(t))
            button.pack(side=tk.LEFT, padx=2)
            self.search_buttons.append(button)

        # 下部区块 - 显示结果
        self.result_frame = ttk.Frame(master, padding="10")
        self.result_frame.pack(fill=tk.BOTH, expand=True)

        self.result_text = tk.Text(self.result_frame, wrap=tk.WORD, width=60, height=15)
        self.result_text.pack(fill=tk.BOTH, expand=True)

        # 加载诗歌数据
        with open('Hymn.json', 'r', encoding='utf-8') as file:
            self.hymn_data = json.load(file)

    def search_hymn(self, hymn_type):
        hymn_number = self.search_entry.get()
        
        # 构造新的键格式
        key = f"{hymn_type}_{hymn_number}"
        
        if key in self.hymn_data['content']:
            content = self.hymn_data.content[key]
            self.result_text.delete('1.0', tk.END)
            self.result_text.insert(tk.END, f"诗歌类型: {hymn_type}\n诗歌编号: {hymn_number}\n\n{content['hymn_content']}")
        else:
            self.result_text.delete('1.0', tk.END)
            self.result_text.insert(tk.END, f"未找到 {hymn_type} 中编号为 {hymn_number} 的诗歌")

if __name__ == "__main__":
    root = tk.Tk()
    app = HymnApp(root)
    root.mainloop()
