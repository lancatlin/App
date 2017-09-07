import tkinter as tk
import sys


def buttoncommend(m):
    titlevar.set('選擇模式: '+buttonvar[m])
    global mode
    mode = m
def clean():
    inputentry.delete(0,'end')
    outputentry.delete(0,'end')
    wordtext.delete(1.0,'end')
    codeentry.delete(0,'end')
    outputtext.delete(1.0,'end')
def _print_(t):
    print(t)
    printvar.set(str(t))
def _input_(e):
    _input = inputentry.get()
    print(mode)
    if _input != '':
        try:
            _input += '.txt'
            o = open('file\\' + _input, 'r', encoding='utf-8-sig')
            text = o.read()
            wordtext.insert(1.0, text)
        except:
            _print_('文件不存在')
def start():
    # 輸入內容
    text=wordtext.get(1.0,'end')
    # 輸入密碼
    if mode == 0:
        long=len(text)
    elif mode == 1:
        long=''
        for i in range(len(text)):
            if text[i] == '!':
                print (long)
                text = text.strip(long+'!')
                break
            else:
                long += text[i]
        long = int(long)
    try:
        password = int(codeentry.get())
    except:
        _print_('密碼非數字')
    # 輸入輸出檔名
    outdoc = outputentry.get()
    if outdoc != '':
        outdoc += '.txt'
        f = open('file\\' + outdoc, 'w')
        f.close()
    # 計算
    password %= long
    while len(text) % password != 0 and mode == 0:
        text+=' '
    xword = len(text) // password
    result = []
    k = 0
    if mode == 1:
        p = password
        x = xword
    elif mode == 0:
        p = xword
        x = password
    else:
        print('你輸入錯誤的模式')
    for i in range(p):
        result.append('')
        for j in range(x):
            result[-1] += text[k]
            k += 1
    if mode == 0:
        string = str(long)+'!'
    else:
        string = ''
    for i in range(x):
        for j in result:
            string += j[i]
    print(string)
    outputtext.delete(1.0,'end')
    outputtext.insert(1.0,string)
    try:
        f = open('file\\' + outdoc, 'w', encoding='utf-8-sig')
        f.write(string)
        f.close()
    except:
        pass
window = tk.Tk()
window.title('Encoding')
window.geometry('300x400')

mode=None
titlevar=tk.StringVar()   #開頭問題變數
titlelabel=tk.Label(window,textvariable=titlevar)
titlelabel.grid(row=1,columnspan=4,sticky=tk.W)   #開頭問題label
titlevar.set('選擇模式:')
button=[]
buttonvar=['加密','解密']
for j in range(2):
    button.append(tk.Button(window,text = buttonvar[j],command=lambda j=j: buttoncommend(j),width=6))
    button[-1].grid(row=2,column=j,sticky=tk.N)
lab1=tk.Label(window,text='請輸入來源與輸出文件名(不需加.txt)')
lab1.grid(row=3,columnspan=6,sticky=tk.W)

inputlabel = tk.Label(window,text='來源文件檔:')
inputlabel.grid(row=4,columnspan=2,sticky=tk.W)

inputentry = tk.Entry(window)
inputentry.grid(row=4,column=1,columnspan=4)
inputentry.bind('<Return>',_input_)

outputlabel = tk.Label(window,text='輸出文件檔:')
outputlabel.grid(row=5,columnspan=2,sticky=tk.W)

outputentry = tk.Entry(window)
outputentry.grid(row=5,column=1,columnspan=4)

wordlabel=tk.Label(window,text='輸入文字內容:')
wordlabel.grid(row=6,columnspan=3,sticky=tk.W)

wordtext=tk.Text(window,width=35,height=6)
wordtext.grid(row=7,columnspan=6,sticky=tk.W,padx=20)

codelabel = tk.Label(window,text='密碼:')
codelabel.grid(row=8,columnspan=1,sticky=tk.W)

codeentry = tk.Entry(window,width=12)
codeentry.grid(row=8,column=1,columnspan=1)

enter = tk.Button(window,text='開始!',width=7,command=start)
enter.grid(row=8,column=3)
clear = tk.Button(window,text='清除',width=7,command=clean)
clear.grid(row=8,column=2)
printvar=tk.StringVar()
printlabel=tk.Label(window,textvariable=printvar)
printlabel.grid(row=9,columnspan=6)
outputtext = tk.Text(window,width=35,height=6)
outputtext.grid(row=10,columnspan=6,sticky=tk.W,padx=20)
window.mainloop()