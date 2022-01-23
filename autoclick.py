# Load Packages, use pip install pyautogui
from operator import truediv
import pyautogui    #these are for our clicks and keyboard strokes!
import time         #required to call any time commands (i.e. delays)

# ONE -- Get Cursor Location - Just press play and put your cursos where you want to get the loc
time.sleep(1)
print(pyautogui.position())

#print = Point(x=870, y=47) copy the X and Y and paste at ''pyautogui.click(xxx, yyy)''

# TWO -- Click
while True:
    pyautogui.click(118, 1057)      #click the loc 
    time.sleep(2)                   #time of wait to repeat

#If want to do more clicks, just copy pyautogui.click(xxx, yyy) and put inside the loop.

#Its working for me all night with BombCrypto, without any problem.

#Its a super simple script which can be modified as you want.