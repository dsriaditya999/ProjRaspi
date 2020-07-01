# Importing Libraries

import RPi.GPIO as GPIO
import time
import math

# Definitions

LEDpin = 18

duty = 0

# Setup GPIO

def mapfunc(x,inLo,inHi,outLo,outHi):
    inRange = inHi-inLo
    outRange = outHi-outLo
    inScale = (x-inLo)/inRange
    return outLo + (inScale*outRange)



GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDpin,GPIO.OUT)

GPIO.output(LEDpin,GPIO.LOW)
time.sleep(1)
GPIO.output(LEDpin,GPIO.HIGH)
time.sleep(1)
GPIO.output(LEDpin,GPIO.LOW)
time.sleep(1)

adv_blink = GPIO.PWM(LEDpin,200)
adv_blink.start(0)

# Loop
x = 0
try:
    while(1):

        step = 0.3

        duty = mapfunc(math.sin(x),-1,1,0,100)

        x += step

        adv_blink.ChangeDutyCycle(duty)

        if(x  >= 2*math.pi):
            x = 0

        time.sleep(0.05)


except KeyboardInterrupt:
    adv_blink.stop()
    GPIO.cleanup()
        
