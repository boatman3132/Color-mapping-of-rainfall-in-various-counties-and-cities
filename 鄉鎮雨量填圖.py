# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 14:10:11 2023

@author: a1020
"""
import time
import numpy as np
import matplotlib.pyplot as plt

def search_town_data(all_record,keyword,column):
    """
    ['TOWNID', 'TOWNCODE', 'COUNTYNAME', 'TOWNNAME', 'TOWNENG',
           'COUNTYID', 'COUNTYCODE', 'geo_interface']
    """
    i = np.where(all_record,column)

npz_path = '鄉鎮基本參數_分區_邊界資料.npz'
npz_path2 = '縣市基本參數及邊界資料.npz'


A = np.load(npz_path,allow_pickle=True)
geo_properties = A['geo_properties']
RecordShapes   = A['RecordShapes'].tolist()
area_id        = A['area_id'].tolist()

A2 = np.load(npz_path2,allow_pickle=True)
geo_properties2 = A2['geo_properties']
RecordShapes2   = A2['RecordShapes'].tolist()

# 北海岸 基隆 東北角 新北東側 新北烏來 桃園山區 新竹山區 苗栗山區 
# 臺中山區 南投仁愛 南投信義 雲林山區 嘉義山區
# 臺南山區 高雄山區 高雄淺山 屏東山區 恆春半島
# 宜蘭北側 宜蘭南側 宜蘭淺山 花蓮秀林 花蓮萬榮 花蓮卓溪 花蓮海岸 
# 臺東北側 臺東南側 臺東北岸 臺東南岸   
# 臺北 新北 桃園 新竹 苗栗
# 臺中 彰化 南投 雲林 嘉義
# 臺南 高雄 屏東 宜蘭

# rainlist = [100, 50, 600, 50, 100, 50, 100, 50, 
#             100, 50, 100, 250, 50, 
#             150, 400, 250, 50, 100,
#             250, 150, 100, 30, 400, 150, 600,
#             30, 400, 50, 100,
#             30, 400, 30, 400, 30,
#             600, 30, 400, 600, 400,
#             30, 100, 30, 400]
# 填寫這邊

# #01/31
rainlist = [20, 60, 60, 20, 20, 20, 10, 10,
            10, 10, 10, 10, 10, 
            0, 0, 0, 0, 0,
            20, 60, 60, 20, 20, 0, 20,
            0, 0, 0, 0,
            20, 20, 20, 0, 0,
            0, 0, 0, 0, 0,
            0, 10, 10, 20]

#02/01
# rainlist = [20, 20, 20, 20, 20, 20, 20, 20,
#             20, 20, 20, 0, 0, 
#             0, 0, 0, 10, 10,
#             20, 20, 20, 20, 20, 20, 20,
#             0, 0, 20, 0,
#             20, 20, 20, 20, 0,
#             0, 0, 0, 0, 0,
#             0, 10, 10, 20]

# 02/02
# rainlist = [20, 20, 20, 20, 20, 20, 0, 0,
#             0, 0, 0, 0, 0, 
#             0, 0, 0, 10, 10,
#             20, 20, 20, 20, 20, 20, 20,
#             20, 0, 20, 0,
#             20, 20, 0, 0, 0,
#             0, 0, 0, 0, 0,
#             0, 10, 10, 20]

# # 02/03
# rainlist = [60, 60, 60, 20, 20, 20, 20, 20,
#             20, 20, 20, 0, 0, 
#             0, 0, 0, 10, 10,
#             20, 20, 20, 20, 20, 20, 20,
#             0, 0, 20, 0,
#             20, 20, 20, 20, 0,
#             0, 0, 0, 0, 0,
#             0, 10, 10, 20]

# 02/04
# rainlist = [40, 40, 40, 40, 40, 0, 0, 0,
#             0, 0, 0, 0, 0, 
#             0, 0, 0, 10, 10,
#             20, 20, 20, 20, 20, 0, 20,
#             0, 0, 0, 0,
#             0, 0, 0, 0, 0,
#             0, 0, 0, 0, 0,
#             0, 10, 10, 20]

# 09/23
# rainlist = [0, 0, 20, 20, 20, 20, 20, 0,
#             0, 0, 20, 20, 20, 
#             20, 20, 20, 20, 20,
#             20, 20, 20, 0, 0, 20, 0,
#             20, 20, 20, 20,
#             0, 0, 0, 0, 0,
#             0, 0, 20, 0, 20,
#             20, 20, 20, 20]

# 09/24
# rainlist = [0, 0, 20, 20, 20, 20, 20, 0,
#             0, 0, 0, 0, 0, 
#             20, 20, 20, 20, 20,
#             20, 20, 20, 20, 0, 0, 0,
#             20, 20, 20, 20,
#             0, 0, 0, 0, 0,
#             0, 0, 0, 0, 0,
#             20, 20, 20, 20]

filename = '0128F0204'

# 北海岸 基隆 東北角 新北東側 新北烏來 桃園山區 新竹山區 苗栗山區 
# 臺中山區 南投仁愛 南投信義 雲林山區 嘉義山區
# 臺南山區 高雄山區 高雄淺山 屏東山區 恆春半島
# 宜蘭北側 宜蘭南側 宜蘭淺山 花蓮秀林 花蓮萬榮 花蓮卓溪 花蓮海岸 
# 臺東北側 臺東南側 臺東北岸 臺東南岸   
# 臺北 新北 桃園 新竹 苗栗
# 臺中 彰化 南投 雲林 嘉義
# 臺南 高雄 屏東 宜蘭

# 水保局舊版
# color_levels = [
#     ['#FFFFFF',0,10],
#     ['#A6A6A6',10,40],
#     ['#00B0F0',40,80],
#     ['#92D050',80,130],
#     ['#FFFF00',130,200],
#     ['#ED7D31',200,350],
#     ['#FF0000',350,500],
#     ['#7030A0',500,1500] ]

# 周新版小間距
color_levels = [
    ['#FFFFFF',0,10],
    ['#7DDDFF',10,40],
    ['#F4B183',40,80],
    ['#FF0000',80,130],
    ['#FF66FF',130,200],
    ['#FFCCFF',200,350],
    ['#696969',350,500],
    ['#A9A9A9',500,750],
    ['#F0FFF0',750,1200],
    ]

plt.figure(figsize=(6,10.2))
for i,rec in enumerate(RecordShapes):
    fillvalue = rainlist[area_id[rec[7]]] #該鄉鎮的預估降雨
    fillcolor = '#000000'
    
    # 調整台南山區的範圍
    # if rec[3] in ['東勢區','新社區','太平區','霧峰區']:
    #     fillvalue = rainlist[8]
    if rec[3] in ['竹山鎮','鹿谷鄉','水里鄉']:
        fillvalue = rainlist[36]
    if rec[3] in ['東山區','白河區','柳營區','六甲區']:
        fillvalue = rainlist[13]
    if rec[3] in ['臺東市']:
        fillvalue = rainlist[28]
    
    for j in range(8):
        if fillvalue >= color_levels[j][1] and fillvalue <= color_levels[j][2]:
            fillcolor = color_levels[j][0]
            break
    # if rec[3] in ['蘇澳鎮','南澳鄉']:
    #     fillcolor = '#92D050'
    border_x = rec[8][:,0]
    border_y = rec[8][:,1]
    
    plt.fill(border_x,border_y,fillcolor)

for i2,rec2 in enumerate(RecordShapes2):
    border_x2 = rec2[-1][:,0]
    border_y2 = rec2[-1][:,1]
    
    plt.plot(border_x2,border_y2,'k')


    
plt.xlim((119.6,122.1))
plt.ylim((21.5,25.5))
plt.axis('off')

lct = time.localtime()
t_flag = str(lct[0])+'-'
if lct[1] < 10:
    t_flag = t_flag+'0'
t_flag = t_flag+str(lct[1])
if lct[2] < 10:
    t_flag = t_flag+'0'
t_flag = t_flag+str(lct[2])+'_'
if lct[3] < 10:
    t_flag = t_flag+'0'
t_flag = t_flag+str(lct[3])
if lct[4] < 10:
    t_flag = t_flag+'0'
t_flag = t_flag+str(lct[4])
if lct[5] < 10:
    t_flag = t_flag+'0'
t_flag = t_flag+str(lct[5])

if filename == '':
    plt.savefig('image_'+t_flag+'.png', bbox_inches='tight',pad_inches = 0, transparent=True)
else:
    plt.savefig(filename+'.png', bbox_inches='tight',pad_inches = 0, transparent=True)
    
    

"""
for i,rec in enumerate(RecordShapes):
    print(i,rec[2],rec[3])
    if i % 10 == 9:
        print('===================')
"""
