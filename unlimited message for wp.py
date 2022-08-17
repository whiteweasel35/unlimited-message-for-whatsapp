import pyautogui as gui
import time

#author white weasel
message = input("mesajınızı giriniz:")
number = input("kaç defa göndermek istediğinizi girin:")

time.sleep(2)

for i in range(int(number)):
    gui.typewrite(message)
    gui.press('enter')
