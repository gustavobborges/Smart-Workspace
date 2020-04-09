from datetime import time
import time
import sys
sys.platform
import os

horaAtual = time.localtime()
print (horaAtual)

if horaAtual.tm_wday < 5:
    if 13 <= horaAtual.tm_hour < 19 or 12 < horaAtual.tm_hour < 19 and horaAtual.tm_min > 50:
        os.startfile('notepad.exe')
        os.startfile(r"C:\Users\gusta\AppData\Local\slack\slack.exe")
        os.startfile(r"C:\Users\gusta\Desktop\IBRIDGE")

    else:
        os.startfile('https://youtube.com')
        os.startfile(r"C:\Program Files\JetBrains\PyCharm Community Edition 2019.2.5\bin\pycharm64.exe")
else:
    os.startfile('http://netflix.com')
    os.startfile(r"C:\Users\gusta\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Yooiistudios\Yooii Apps\Mobile Buddy.exe")

