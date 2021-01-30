#!/usr/bin/env python

from adafruit_servokit import ServoKit
import time 
import logging

def main():
    kit = ServoKit(channels=16)
    kit.servo[3].angle = 180
    #time.sleep(1)
    kit.servo[3].angle = 0
    kit.servo[3].actuation_range = 270
    kit.servo[3].angle = 180
    time.sleep(1)
    kit.servo[3].angle = 270
    time.sleep(1)
    kit.servo[3].angle = 0

    




if __name__=='__main__':
    main()
