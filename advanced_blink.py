
# Importing Libraries

import RPi.GPIO as GPIO
import time

# Definitions

LEDpin = 18

duty = 80

# Setup GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDpin,GPIO.OUT)

GPIO.output(LEDpin,GPIO.LOW)
time.sleep(1)
GPIO.output(LEDpin,GPIO.HIGH)
time.sleep(1)
GPIO.output(LEDpin,GPIO.LOW)
time.sleep(1)

adv_blink = GPIO.PWM(LEDpin,200)
adv_blink.start(duty)

# Loop

try:
    while(1):
        adv_blink.ChangeDutyCycle(duty)
        time.sleep(1)
        adv_blink.ChangeDutyCycle(100-duty)
        time.sleep(1)

except KeyboardInterrupt:
    adv_blink.stop()
    GPIO.cleanup()
        
