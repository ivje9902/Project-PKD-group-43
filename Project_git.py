from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()
motorpair = MotorPair('A', 'B')
colorsensor = ColorSensor('B')
motor = Motor('C')
colortree = {'white': motorpair.start(0, 10), 'blue': motorpair.start(2, 'cm', 0, 10), 'green': motorpair.start(2, 'cm', -100, 10), 'red': motorpair.start(2, 'cm', 100, 10)}
colortree[]
while True:
    color = colorsensor.get_color() 
    colortree[color]
