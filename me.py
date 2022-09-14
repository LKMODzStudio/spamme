import pyautugui as pg
import time

messages = input("MESSAGE : ")
number = int(input("NUMBER : "))

print("Plz wait 5s")
time.sleep(5)

for i in range(number):
    pg.typewrite(messages)
    pg.pross('ENTER')
    
print("Done")