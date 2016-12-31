#!/usr/bin/env python
# -*- coding: utf-8 -*-

# A program to control the movement of a single motor using the RTK MCB!
# Composed by The Raspberry Pi Guy to accompany his tutorial!

# Let's import the modules we will need!
import time
import RPi.GPIO as GPIO
import pyrebase

#Firebase Configuration
config = {
"apiKey": "apiKey",
"authDomain": "raspberrypi-23da0.firebaseapp.com",
"databaseURL": "https://raspberrypi-23da0.firebaseio.com",
"storageBucket": "raspberrypi-23da0.appspot.com"
}

firebase = pyrebase.initialize_app(config)

#Firebase Database Intialization
db = firebase.database()
# Next we setup the pins for use!
# Variables
ena1A=7
ena2A=11
foward1=13
backward1=15
#motor 2
ena3B=12
ena4B=16
foward2=18
backward2=22
hold_down=False

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ena1A,GPIO.OUT)
GPIO.setup(ena2A,GPIO.OUT)
GPIO.setup(backward1,GPIO.OUT)
GPIO.setup(foward1,GPIO.OUT)
# segundo motor azul
GPIO.setup(ena3B,GPIO.OUT)
GPIO.setup(ena4B,GPIO.OUT)
GPIO.setup(foward2,GPIO.OUT)
GPIO.setup(backward2,GPIO.OUT)



while True:
    try:
        #Get value of LED
        led = db.child("led").get()

        for user in led.each():
            if(user.val() == "OFF"):
                print('Stooping Motor')
                GPIO.output(ena1A, False)
                GPIO.output(ena2A, False)
                # motor 2
                GPIO.output(ena3B, False)
                GPIO.output(ena4B, False)
                GPIO.output(foward1, False)
                GPIO.output(foward2, False)
                GPIO.output(backward1, False)
                GPIO.output(backward2, False)

            #Check value of child(which is 'state')
            elif(user.val() == "UP"):
                #If value is off, turn LED off
                print('Foward Motor ')
                GPIO.output(ena1A, False)
                GPIO.output(ena2A, True)
                #motor 2
                GPIO.output(ena3B, False)
                GPIO.output(ena4B, True)
                GPIO.output(foward1, True)
                GPIO.output(foward2, True)
                GPIO.output(backward1, False)
                GPIO.output(backward2, False)
            elif(user.val() == "DOWN"):
                print('Backward Motor ')
                GPIO.output(ena1A, False)
                GPIO.output(ena2A, True)
                #motor 2
                GPIO.output(ena3B, False)
                GPIO.output(ena4B, True)
                GPIO.output(backward1, True)
                GPIO.output(backward2, True)
                GPIO.output(foward1,False)
                GPIO.output(foward2, False)
                time.sleep(3)
            elif(user.val() == "LEFT"):
                print('turning left')
                GPIO.output(ena1A, True)
                GPIO.output(ena2A, True)
                # motor 2
                GPIO.output(ena3B, True)
                GPIO.output(ena4B, True)
                GPIO.output(foward1, True)
                GPIO.output(foward2, False)
                GPIO.output(backward1, False)
                GPIO.output(backward2, False)
            elif(user.val() == "RIGHT"):
                print('turning right')
                GPIO.output(ena1A, True)
                GPIO.output(ena2A, True)
                # motor 2
                GPIO.output(ena3B, True)
                GPIO.output(ena4B, True)
                GPIO.output(foward1, False)
                GPIO.output(foward2, True)
                GPIO.output(backward1, False)
                GPIO.output(backward2, False)

            else:
                print('Stooping Motor')
                GPIO.output(ena1A, False)
                GPIO.output(ena2A, False)
                # motor 2
                GPIO.output(ena3B, False)
                GPIO.output(ena4B, False)
                GPIO.output(foward1, False)
                GPIO.output(foward2, False)
                GPIO.output(backward1, False)
                GPIO.output(backward2, False)

                # Spins the other way for a further 3 seconds
                #turn_left()

                # Makes the motor spin one way for 3 seconds


    except(KeyboardInterrupt):
        print('Stooping Motor')
        GPIO.output(ena1A, False)
        GPIO.output(ena2A, False)
        #motor 2
        GPIO.output(ena3B, False)
        GPIO.output(ena4B, False)
        GPIO.output(foward1, False)
        GPIO.output(foward2, False)
        GPIO.output(backward1, False)
        GPIO.output(backward2, False)

        GPIO.cleanup()


                # If a keyboard interrupt is detected then it exits cleanly!
                #stop_motor()
