'''
ToDo
1. 答對按鈕變綠色 

2. 改成class結構 重新命名變數 美化城市結構

3. 取樣 吉他聲音

4. 轉成exe、上傳到github、製作短片


播放長度設定、間格時間
'''

from tkinter import * 
from tkinter import ttk
import random, time, pygame

'''

'''

# initial
pygame.init()
pygame.mixer.init()
win = Tk()                                                      
win.title("吉他和弦聽力訓練")
win.geometry("280x150")

play = ["C", "G"]
capo = ["0", "1", "2"]
chords_name = ["I","IIm","IIIm","IV","V","VI","V/VII"]
wav_files = {}
chords = []         #七個按鈕物件
statement = False     #True: play按鈕播新的和絃
first_play = True #是否是第一次播放
ans_num = 0         #正確答案 

play_value = StringVar(value="C")
capo_value = IntVar(value=0)
select_value = IntVar() #用戶選擇的值 順接和弦1~7
total_value = IntVar(value=0) #回答問題 簡介
right_value = IntVar(value=0) #答對數

label_1 = Label(win, text="Play:")  
label_2 = Label(win, text="Capo:")
label_3 = Label(win, text= "0 / 0")
combobox_1 = ttk.Combobox(win, values=play, width=4, textvariable= play_value)
combobox_2 = ttk.Combobox(win, values=capo, width=4, textvariable= capo_value)
zero_button = Button(win, text="歸零", command=lambda: [total_value.set(0), right_value.set(0), edit_corret_label()],width=4, bg="#c4b4b4") # 歸零
 
for k in play:
    for i in capo: #這是capo
        for j in range(7):
            wav_files[k+i+str(j)] = pygame.mixer.Sound("./guitar_wav/" + k + i + str(i)+ ".wav")





# button for play sound
def play_chords():
    global first_play
    global statement
    global ans_num
    if first_play == True:
        first_play = False
        for i in range(7):
            chords[i]['state'] = NORMAL
        
    if statement == True:
        statement = False
        ans_num = random.randint(0,6)
        #加一些間格時間再播放
    time.sleep(0.45)
    name = play_value.get() + str(capo_value.get()) +str(ans_num)
    wav_files[name].play()
    print(name)
    # 不可以連續點擊按鈕 偵測是否在撥放中
        
    


def select_chord(i):
    global statement
    total_value.set(total_value.get()+1)
    edit_corret_label()
    print("choose: ",i)
    select_value.set(i)

    if select_value.get() == ans_num:
        right_value.set(right_value.get()+1) 
        edit_corret_label()
        change_button_color(i,"green")# 先改成綠色
        statement = True
        for k in range(7):
            change_button_color(k, "SystemButtonFace")
            chords[k]['state'] = NORMAL
        play_chords()
    else:
        chords[i]['state'] = DISABLED
        print("wrong")
        statement = False
        change_button_color(i,"OrangeRed3")
        

def change_button_color(i,color): #傳入兩個參數 位置和顏色
    chords[i].configure(bg=color)

def edit_corret_label():
    label_3.config(text= str(right_value.get()) + " / " + str(total_value.get()))



play_photo = PhotoImage(file='./play.png')
play_button = Button(bg="gray", image=play_photo, command= play_chords, height=55, width=55) #有時候是重複播放 有時候是新的

# position_setting
label_1.grid(row = 0, column = 0, sticky=W)
label_2.grid(row = 1, column = 0, sticky=W)
combobox_1.grid(row = 0, column = 1, sticky = W) 
combobox_2.grid(row = 1, column = 1, sticky = W)

play_button.grid(row = 0, column = 2 , sticky= N, rowspan=2)

label_3.grid(row=0, column=3)


zero_button.grid(row = 1, column = 3,padx=20, pady=15, sticky=W)

for i in range(7):
    chords.append(Button(text = chords_name[i], command=lambda i=i: select_chord(i), state=DISABLED, width=7))
    if i<4:
        chords[i].grid(row=3, column=i,padx=5, sticky=W)
    else:
        chords[i].grid(row=4, column=i-4,padx=5,pady=10, sticky=W)



win.mainloop()

