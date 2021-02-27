#!/usr/bin/env python
import math
import numpy as np
GRAVITY=9.8

def interface():
    '''
    interface between controller and actuator or acutator simulator
    '''


def servo_control(servo_id, angle):
    '''
    select the servo_id and set the control angle
    '''

class ObjectState(object):
    def __init__(self, x=0, y=0, r=0, theta=0):
        self.x = x
        self.y = y
        self.target_x = x
        self.target_y = y
        self.r = r
        self.target_r = r
        self.theta = theta
        self.target_theta = theta
        self.speed = 0 #
        self.acceleration = 0
        self.delta_t = 0.001 # 1ms

    def get_state(self):
        return (self.x, self.y, self.r, self.theta)

    def set_target_location_euclidean(self, target_x, target_y):
        self.target_x = target_x
        self.target_y = target_y

        return (self.target_x, self.target_y, self.target_r, self.target_theta)

    def set_target_location_polar(self, target_polar, target_theta):
        self.polar = target_polar
        self.theta = target_theta

        return (self.target_x, self.target_y, self.target_r, self.target_theta)

    def simulate_step(self):
        self.x, self.y += (
            self.speed*self.delta_t + 0.5*self.acceleration*self.delta_t**2
        )
        self.speed += self.acceleration*self.delta_t




def convert_dv_to_angles(ax, ay):
    '''
    input: acceleration in x, y domain
    output: angles to apply to each servo that is assumed to be positioned on vertices of a right triangle
    '''
    # thinking:
    # x axis has two vertices v1, v2, and v2 is on [(v1_x+v2_x)/2, (v2_x - v1_x)*sqrt(3)]
    # output could be in form of delta angles, with a factor adjusting how fact to react
    # 1. use polar coordinate to determine strength and angle in x, y plain, (r, theta)
    # 2. theta = 0 can be mapped to pointing towards one of the vertex, say v2
    # 3. normalize r s.t. r = 1 meaning the max tilt possible


