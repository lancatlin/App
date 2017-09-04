import tkinter as tk
import sys


def buttoncommend(m):
    titlevar.set('選擇模式: '+buttonvar[m])
    global mode
    mode = m

window = tk.Tk()
window.title('Encoding')
window.geometry('300x500')

mode=0
titlevar=tk.StringVar()   #開頭問題變數
titlelabel=tk.Label(window,textvariable=titlevar).grid(row=1,columnspan=4,sticky=tk.W)   #開頭問題label
titlevar.set('選擇模式:')
button=[]
buttonvar=['加密','解密','文件加密','文件解密']
for j in range(4):
    button.append(tk.Button(window,text = buttonvar[j],command=lambda j=j: buttoncommend(j)).grid(row=2,column=j,sticky=tk.N))
lab1=tk.Label(window,text='請輸入來源與輸出文件名(不需加.txt)').grid(row=3,columnspan=6,sticky=tk.N)
inputlabel = tk.Label(window,text='來源文件檔:').grid(row=4,columnspan=2,sticky=tk.W)
inputentry = tk.Entry(window).grid(row=4,column=2,columnspan=4)
outputlabel = tk.Label(window,text='輸出文件檔:').grid(row=5,columnspan=2,sticky=tk.W)
outputentry = tk.Entry(window).grid(row=5,column=2,columnspan=4)
wordlabel=tk.Label(window,text='輸入文字內容:').grid(row=6,columnspan=3,sticky=tk.W)
wordtext=tk.Text(window,width=35,height=12).grid(row=7,columnspan=6,sticky=tk.N)
codelabel = tk.Label(window,text='密碼:').grid(row=8,columnspan=1,sticky=tk.W)
codeentry = tk.Entry(window,width=12).grid(row=8,column=1,columnspan=1)
def start():
    # 輸入內容
    print(inputentry)
    text=''
    if inputentry.get() != '':
        try:
            o=open('file\\'+inputentry.get()+'.txt','r')
            text+=o.read()+'/n'
        except:
            return 1
    text+=wordtext.get()
    print(text)
    # 輸入密碼
    try:
        password = int(codeentry.get())
    except:
        return 2
    # 輸入輸出檔名
    outdoc = outputentry.get()
    if outdoc != '':
        outdoc += '.txt'
        f = open('file\\' + outdoc, 'w')
        f.close()
    print()
    # 計算
    if mode % 2 == 1:
        text += ' ' * (password - len(text) % password)
    xword = len(text) // password
    result = []
    k = 0
    if mode == 2 or mode == 4:
        p = password
        x = xword
    elif mode == 1 or mode == 3:
        p = xword
        x = password
    else:
        print('你輸入錯誤的模式')
    for i in range(p):
        result.append('')
        for j in range(x):
            result[-1] += text[k]
            k += 1
    string = ''
    for i in range(x):
        for j in result:
            string += j[i]
    print(string)
    try:
        string_e = string.encode('utf-8-sig')
        f = open('file\\' + outdoc, 'w', encoding='utf-8-sig')
        f.write(string)
        f.close()
    except:
        print()
    x = input('按下Enter結束程序')
enter = tk.Button(window,text='開始!',width=10,command=start).grid(row=8,column=3)
window.mainloop()