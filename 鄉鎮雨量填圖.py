# -*- coding: utf-8 -*-
"""
GUI 版：使用者可自行輸入各區域的降雨數值，
並利用捲軸與自訂排列方式（依照下列格式）
排列輸入欄位：
    "北海岸", "基隆", "東北角", "新北東側", "新北烏來", "桃園山區", "新竹山區", "苗栗山區",
    "臺中山區", "南投仁愛", "南投信義", "雲林山區", "嘉義山區",
    "臺南山區", "高雄山區", "高雄淺山", "屏東山區", "恆春半島",
    "宜蘭北側", "宜蘭南側", "宜蘭淺山", "花蓮秀林", "花蓮萬榮", "花蓮卓溪", "花蓮海岸",
    "臺東北側", "臺東南側", "臺東北岸", "臺東南岸",
    "臺北", "新北", "桃園", "新竹", "苗栗",
    "臺中", "彰化", "南投", "雲林", "嘉義",
    "臺南", "高雄", "屏東", "宜蘭"
視窗大小設定為 950x500。
"""

import tkinter as tk
from tkinter import messagebox, ttk
import numpy as np
import matplotlib.pyplot as plt
import time

# 區域名稱（共 43 個）
region_names = [
    "北海岸", "基隆", "東北角", "新北東側", "新北烏來", "桃園山區", "新竹山區", "苗栗山區",
    "臺中山區", "南投仁愛", "南投信義", "雲林山區", "嘉義山區",
    "臺南山區", "高雄山區", "高雄淺山", "屏東山區", "恆春半島",
    "宜蘭北側", "宜蘭南側", "宜蘭淺山", "花蓮秀林", "花蓮萬榮", "花蓮卓溪", "花蓮海岸",
    "臺東北側", "臺東南側", "臺東北岸", "臺東南岸",
    "臺北", "新北", "桃園", "新竹", "苗栗",
    "臺中", "彰化", "南投", "雲林", "嘉義",
    "臺南", "高雄", "屏東", "宜蘭"
]

# 預設的降雨數值（共 43 筆）
default_rainlist = [20, 60, 60, 20, 20, 20, 10, 10,
                    10, 10, 10, 10, 10,
                    0, 0, 0, 0, 0,
                    20, 60, 60, 20, 20, 0, 20,
                    0, 0, 0, 0,
                    20, 20, 20, 0, 0,
                    0, 0, 0, 0, 0,
                    0, 10, 10, 20]

def plot_map(rainlist):
    """
    利用輸入的 rainlist 來繪製地圖。
    """
    npz_path = '鄉鎮基本參數_分區_邊界資料.npz'
    npz_path2 = '縣市基本參數及邊界資料.npz'
    try:
        A = np.load(npz_path, allow_pickle=True)
    except Exception as e:
        messagebox.showerror("錯誤", f"無法讀取 {npz_path}\n{e}")
        return
    geo_properties = A['geo_properties']
    RecordShapes   = A['RecordShapes'].tolist()
    area_id        = A['area_id'].tolist()

    try:
        A2 = np.load(npz_path2, allow_pickle=True)
    except Exception as e:
        messagebox.showerror("錯誤", f"無法讀取 {npz_path2}\n{e}")
        return
    geo_properties2 = A2['geo_properties']
    RecordShapes2   = A2['RecordShapes'].tolist()

    color_levels = [
        ['#FFFFFF', 0, 10],
        ['#7DDDFF', 10, 40],
        ['#F4B183', 40, 80],
        ['#FF0000', 80, 130],
        ['#FF66FF', 130, 200],
        ['#FFCCFF', 200, 350],
        ['#696969', 350, 500],
        ['#A9A9A9', 500, 750],
        ['#F0FFF0', 750, 1200],
    ]

    plt.figure(figsize=(6, 10.2))
    for i, rec in enumerate(RecordShapes):
        try:
            fillvalue = rainlist[ area_id[ rec[7] ] ]
        except Exception as e:
            fillvalue = 0
        fillcolor = '#000000'
        
        # 特殊鄉鎮調整
        if rec[3] in ['竹山鎮','鹿谷鄉','水里鄉']:
            if len(rainlist) > 36:
                fillvalue = rainlist[36]
        if rec[3] in ['東山區','白河區','柳營區','六甲區']:
            if len(rainlist) > 13:
                fillvalue = rainlist[13]
        if rec[3] in ['臺東市']:
            if len(rainlist) > 28:
                fillvalue = rainlist[28]
        
        for j in range(len(color_levels)):
            if fillvalue >= color_levels[j][1] and fillvalue <= color_levels[j][2]:
                fillcolor = color_levels[j][0]
                break
        
        border_x = rec[8][:, 0]
        border_y = rec[8][:, 1]
        plt.fill(border_x, border_y, fillcolor)
    
    for i2, rec2 in enumerate(RecordShapes2):
        border_x2 = rec2[-1][:, 0]
        border_y2 = rec2[-1][:, 1]
        plt.plot(border_x2, border_y2, 'k')
    
    plt.xlim((119.6, 122.1))
    plt.ylim((21.5, 25.5))
    plt.axis('off')
    
    filename = 'output'
    t_flag = time.strftime("%Y%m%d_%H%M%S", time.localtime())
    plt.savefig(filename + '.png', bbox_inches='tight', pad_inches=0, transparent=True)
    plt.show()
    
    messagebox.showinfo("完成", f"圖檔已儲存為 {filename}.png")

def start_plot():
    """
    從 GUI 中取得使用者輸入，轉換成數值後呼叫 plot_map()。
    """
    try:
        rainlist = [float(entry.get()) for entry in entries]
    except Exception as e:
        messagebox.showerror("輸入錯誤", "請確認所有欄位皆輸入數字！")
        return
    plot_map(rainlist)

def _on_mousewheel(event):
    """
    滾輪事件處理函式：
      - Windows 與 MacOS 使用 event.delta
      - Linux 透過 event.num 判斷（Button-4 向上，Button-5 向下）
    """
    if event.delta:
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    elif event.num == 4:
        canvas.yview_scroll(-1, "units")
    elif event.num == 5:
        canvas.yview_scroll(1, "units")

# 建立主視窗
root = tk.Tk()
root.title("降雨數值輸入")
root.geometry("950x550")
# 如需禁止使用者調整視窗大小，可取消下行註解
# root.resizable(False, False)

# 建立可捲動的區域
container = ttk.Frame(root)
container.pack(fill="both", expand=True)

canvas = tk.Canvas(container, height=400)
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

canvas.bind_all("<MouseWheel>", _on_mousewheel)
canvas.bind_all("<Button-4>", _on_mousewheel)
canvas.bind_all("<Button-5>", _on_mousewheel)

# 自訂排版格式：每列依據下列數量排列，共 8 行
# 第一列：8，第二列：5，第三列：5，第四列：7，
# 第五列：4，第六列：5，第七列：5，第八列：4
row_layout = [8, 5, 5, 7, 4, 5, 5, 4]  # 總計 43 個

entries = []
current_index = 0
for row, count in enumerate(row_layout):
    for col in range(count):
        if current_index >= len(region_names):
            break
        region = region_names[current_index]
        cell_frame = ttk.Frame(scrollable_frame)
        cell_frame.grid(row=row, column=col, padx=5, pady=5, sticky="w")
        lbl = ttk.Label(cell_frame, text=f"{region}：")
        lbl.pack(anchor="w")
        entry = ttk.Entry(cell_frame, width=10)
        entry.insert(0, str(default_rainlist[current_index]))
        entry.pack(anchor="w")
        entries.append(entry)
        current_index += 1

btn = tk.Button(root, text="產生地圖", command=start_plot)
btn.pack(pady=10)

root.mainloop()
