# import RPi.GPIO as GPIO
# import time
 
# #GPIO SETUP
# channel = 21
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(channel, GPIO.IN)
 
# def callback(channel):
#         if GPIO.input(channel):
#                 print("Water Detected")
#         else:
#                 print("water not detected")
 
# GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
# GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change
 
# # infinite loop
# while True:
#         time.sleep(1)


#following lines of code is an alternate implementation

# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time

import board

from adafruit_seesaw.seesaw import Seesaw

i2c_bus = board.I2C()  # uses board.SCL and board.SDA
# i2c_bus = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller

ss = Seesaw(i2c_bus, addr=0x36)

while True:
    # read moisture level through capacitive touch pad
    touch = ss.moisture_read()

    # read temperature from the temperature sensor
    temp = ss.get_temp()

    print("temp: " + str(temp) + "  moisture: " + str(touch))
    time.sleep(1)