import sys
print('歡迎使用Encoding')
#選擇模式
while True:
    try:
        mode = int(input('輸入模式:1.加密  2.解密 3.文件加密 4.文件解密:'))
        print(mode)
        break
    except:
        print('你輸入的不是整數')
#輸入內容
if mode < 3:
    text=input('輸入文字內容:')
else:
    while True:
        try:
            name = input('輸入來源檔案:') + '.txt'
            c=open('file'+'\\'+name,mode='r',encoding = 'utf-8-sig')
            text = c.read()
            break
        except FileNotFoundError as e:
            print('錯誤')
            print(e)
            print('程序即將結束')
            sys.exit()
print(text)
print('-'*80)
print()
#輸入密碼
while True:
    try:
        password=int(input('輸入密碼:'))
        break
    except:
        print('你輸入的不是整數')
#輸入輸出檔名
outdoc=input('輸入輸出檔名(不存檔請留空):  ')
if outdoc != '':
    outdoc+='.txt'
    f=open('file\\'+outdoc,'w')
    f.close()
print()
#計算
if mode%2 ==1 :
    text+=' '*(password-len(text)%password)
xword=len(text) // password
result=[]
k=0
if mode == 2 or mode == 4 :
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
string=''
for i in range(x):
    for j in result:
        string += j[i]
print(string)
try:
    string_e=string.encode('utf-8-sig')
    f=open('file\\'+outdoc,'w',encoding='utf-8-sig')
    f.write(string)
    f.close()
except:
    print()
x=input('按下Enter結束程序')