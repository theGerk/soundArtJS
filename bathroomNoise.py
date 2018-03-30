#!/usr/bin/env python

import RPi.GPIO as GPIO #needed for GPIO pins on PI
import time #needed for sleep
import os   #needed for os calls
from multiprocessing import Process #needed for running chrome on seperate process
from random import *


location = "/home/pi/soundArtJS/"
GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.IN)

fileName = "public_html/index.html"
cycleTime = 358 * 4 * 20 / 1000
cycles = 2
runTime = cycles * cycleTime
rickChance = 1024
#print(runTime)

def otherProcess():
    os.system("chromium-browser " + location + fileName)

rickTime = 3 * 60 + 31
def rickRoll():
    os.system("vlc " + location + "Never\ Gonna\ Give\ You\ Up\ Original.mp3")

def buttonPressHandler():
    print("hi")
    if randint(1, rickChance) == 1:
        p = Process(target=rickRoll)
        p.start()
        time.sleep(rickTime + 5)
        os.system("kill $(ps aux | grep '[v]lc' | awk '{print $2}')")
        p.join()
    else:
        p = Process(target=otherProcess)
        #print('hello')
        p.start()
        #print('world')
        time.sleep(runTime)
        os.system("kill $(ps aux | grep '[c]hromium-browser' | awk '{print $2}')")
        p.join()
        
buttonPressHandler()

#Run loop
while True:
    if not GPIO.input(2):
        buttonPressHandler()
    time.sleep(.001)
