import RPi.GPIO as GPIO
import time #needed for sleep
import os   #needed for os calls
from multiprocessing import Process

GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.IN)

fileName = "/home/pi/soundArtJS/public_html/index.html"
cycleTime = 358 * 4 * 20 / 1000
cycles = 2
runTime = cycles * cycleTime
#print(runTime)

def otherProcess():
    os.system("chromium-browser " + fileName)

def buttonPressHandler():
    p = Process(target=otherProcess)
    #print('hello')
    p.start()
    #print('world')
    time.sleep(runTime)
    os.system("kill $(ps aux | grep '[c]hromium-browser' | awk '{print $2}')")
    p.join()

#Run loop
while True:
    if not GPIO.input(2):
        buttonPressHandler()
    time.sleep(.001)