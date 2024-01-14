import RPi.GPIO as GPIO
import time

pwm_r_back = 12
pwm_l_back = 35
pwm_r = 32
pwm_l = 33
ultra_trig = 3
ultra_echo = 5
pulse_send = 0
pulse_recieved = 0
distance = 0

#backward code
def backward():
    pi_pwm_l.ChangeDutyCycle(80)
    pi_pwm_l_back.ChangeDutyCycle(0)
    pi_pwm_r.ChangeDutyCycle(80)
    pi_pwm_r_back.ChangeDutyCycle(0)

#backward code
def forward():
    pi_pwm_l.ChangeDutyCycle(0)
    pi_pwm_l_back.ChangeDutyCycle(80)
    pi_pwm_r.ChangeDutyCycle(0)
    pi_pwm_r_back.ChangeDutyCycle(80)

GPIO.setwarnings(False)			#disable warnings
GPIO.setmode(GPIO.BOARD)		#set pin numbering system
GPIO.setup(pwm_r_back,GPIO.OUT)
GPIO.setup(pwm_l_back,GPIO.OUT)
GPIO.setup(pwm_l,GPIO.OUT)
GPIO.setup(pwm_r,GPIO.OUT)
GPIO.setup(ultra_trig,GPIO.OUT)
GPIO.setup(ultra_echo,GPIO.IN)
GPIO.output(ultra_trig,GPIO.LOW)
time.sleep(2)

pi_pwm_l = GPIO.PWM(pwm_l,1000)		#create PWM instance with frequency
pi_pwm_r = GPIO.PWM(pwm_r,1000)
pi_pwm_l_back = GPIO.PWM(pwm_r_back,1000)		
pi_pwm_r_back = GPIO.PWM(pwm_l_back,1000)
pi_pwm_l.start(0)				#start PWM of required Duty Cycle 
pi_pwm_r.start(0)	
pi_pwm_l_back.start(0)				
pi_pwm_r_back.start(0)	

# while True:
#     print ('signal')
#     #detect distance
#     GPIO.output(ultra_trig,GPIO.HIGH)
#     time.sleep(0.00001)
#     GPIO.output(ultra_trig,GPIO.LOW)
#     print ('wait')
#     while GPIO.input(ultra_echo)==0:
#         pulse_send = time.time()
#     while GPIO.input(ultra_echo)==1:
#         pulse_recieved = time.time()
#         if(pulse_recieved-pulse_send >= 0.1): # if no obstable for too long just skip waiting
#             print('no ref')
#             break
#     print('calc')
#     pulse_duration = pulse_recieved - pulse_send
#     pulse_duration = round(pulse_duration/2,0)
#     distance = 340*pulse_duration
#     print(distance)
#     #determine when to stop/slowdown
#     print ('determine')
#     if (distance<=10):
#         print('stop')
#         pi_pwm_l.ChangeDutyCycle(0)
#         pi_pwm_l_back.ChangeDutyCycle(0)
#         pi_pwm_r.ChangeDutyCycle(0)
#         pi_pwm_r_back.ChangeDutyCycle(0)
#     elif(distance<=20):
#         print('slow down')
#         pi_pwm_l.ChangeDutyCycle(30)
#         pi_pwm_r.ChangeDutyCycle(30)
#     else:
        #move
    print('move')
    forward()
    time.sleep(2)
