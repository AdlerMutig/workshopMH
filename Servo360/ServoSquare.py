import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)

pwm1=GPIO.PWM(11,50)
pwm2=GPIO.PWM(13,50)

pwm1.start(7.5)
pwm2.start(7.5)

pwm1.ChangeDutyCycle(6.4)
pwm2.ChangeDutyCycle(7.875)
time.sleep(1)

pwm1.ChangeDutyCycle(7.23)
pwm2.ChangeDutyCycle(7.23)
time.sleep(1)

pwm1.ChangeDutyCycle(7.5)
pwm2.ChangeDutyCycle(7.5)
time.sleep(1)

pwm1.ChangeDutyCycle(7.23)
pwm2.ChangeDutyCycle(7.23)
time.sleep(1)

pwm1.ChangeDutyCycle(6.4)
pwm2.ChangeDutyCycle(7.875)
time.sleep(1)

pwm1.ChangeDutyCycle(7.23)
pwm2.ChangeDutyCycle(7.23)
time.sleep(1)

pwm1.ChangeDutyCycle(7.5)
pwm2.ChangeDutyCycle(7.5)
time.sleep(1)

pwm1.ChangeDutyCycle(7.23)
pwm2.ChangeDutyCycle(7.23)
time.sleep(1)

pwm1.ChangeDutyCycle(6.4)
pwm2.ChangeDutyCycle(7.875)
time.sleep(1)

pwm1.ChangeDutyCycle(7.23)
pwm2.ChangeDutyCycle(7.23)
time.sleep(1)

pwm1.ChangeDutyCycle(7.5)
pwm2.ChangeDutyCycle(7.5)
time.sleep(1)

pwm1.ChangeDutyCycle(7.23)
pwm2.ChangeDutyCycle(7.23)
time.sleep(1)

pwm1.ChangeDutyCycle(6.4)
pwm2.ChangeDutyCycle(7.875)
time.sleep(1)

pwm1.stop()
pwm2.stop()