import RPi.GPIO as GPIO
import time

test_motor_1 = 3
test_motor_2 = 5
enable = 7

GPIO.setwarnings(False)			#disable warnings
GPIO.setmode(GPIO.BOARD)		#set pin numbering system
GPIO.setup(test_motor_1,GPIO.OUT)
GPIO.setup(test_motor_2,GPIO.OUT)
GPIO.setup(enable,GPIO.OUT)
GPIO.output(enable,GPIO.HIGH)
  
GPIO.output(test_motor_1,GPIO.HIGH)
GPIO.output(test_motor_2,GPIO.LOW)
time.sleep(2)
GPIO.output(test_motor_1,GPIO.LOW)
GPIO.output(test_motor_2,GPIO.LOW)