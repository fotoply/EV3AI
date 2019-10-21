import ev3dev.ev3 as ev3
from time import sleep

import signal

motorRight = ev3.LargeMotor('outA')
motorLeft = ev3.LargeMotor('outB')

THRESHOLD_LEFT = 30
THRESHOLD_RIGHT = 350

BASE_SPEED = 50
BACKWARDS_BASE_SPEED = BASE_SPEED*0.8
TURN_SPEED = 80

lightSensorLeft = ev3.ColorSensor('in1')
lightSensorRight = ev3.ColorSensor('in2')

assert lightSensorLeft.connected, "LightSensorLeft(ColorSensor) is not connected"
assert lightSensorRight.connected, "LightSensorRight(ColorSensor) is not conected"

motorLeft.run_direct()
motorRight.run_direct()

motorRight.polarity = "normal"
motorLeft.polarity = "normal"


def signal_handler(sig, frame):
    print('Shutting down gracefully')
    motorRight.duty_cycle_sp = 0
    motorLeft.duty_cycle_sp = 0

    exit(0)


signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C to exit')

# while True:
testString = "frfrfrfrfrfrfrfrfrfrfrfrfrfrfr"

for char in testString:
    print("Next command: " + char)
    if char == "f":
        sensorLeft = lightSensorLeft.value()
        sensorRight = lightSensorRight.value()

        LINE_THRESHOLD = 10
        while sensorLeft < LINE_THRESHOLD and sensorRight < LINE_THRESHOLD:
            sensorLeft = lightSensorLeft.value()
            sensorRight = lightSensorRight.value()

            #print("TsensorLeft: ", sensorLeft, " TsensorRight: ", sensorRight)
            diff = sensorRight - sensorLeft
            motorLeft.duty_cycle_sp = BASE_SPEED - BASE_SPEED * (diff / 200)
            motorRight.duty_cycle_sp = BASE_SPEED + BASE_SPEED * (diff / 200)

            #print("Left: " + str(motorLeft.duty_cycle_sp) + "/" + "Right: " + str(motorRight.duty_cycle_sp))
        while True:
            sensorLeft = lightSensorLeft.value()
            sensorRight = lightSensorRight.value()

            #print("sensorLeft: ", sensorLeft, " sensorRight: ", sensorRight)
            diff = sensorRight - sensorLeft
            motorLeft.duty_cycle_sp = BASE_SPEED - BASE_SPEED * (diff / 200)
            motorRight.duty_cycle_sp = BASE_SPEED + BASE_SPEED * (diff / 200)

            if sensorRight < LINE_THRESHOLD and sensorLeft < LINE_THRESHOLD:
                break

            #print("Left: " + str(motorLeft.duty_cycle_sp) + "/" + "Right: " + str(motorRight.duty_cycle_sp))
    elif char == "r":
        sensorLeft = lightSensorLeft.value()
        sensorRight = lightSensorRight.value()

        LINE_THRESHOLD = 75
        while True:
            sensorLeft = lightSensorLeft.value()
            sensorRight = lightSensorRight.value()

            diff = sensorRight - sensorLeft
            motorLeft.duty_cycle_sp = 80
            motorRight.duty_cycle_sp = motorLeft.duty_cycle_sp*-0.8
            if sensorRight > LINE_THRESHOLD and sensorLeft > LINE_THRESHOLD:
                print("TsensorLeft: ", sensorLeft, " TsensorRight: ", sensorRight)
                print("Left: " + str(motorLeft.duty_cycle_sp) + "/" + "Right: " + str(motorRight.duty_cycle_sp))
                break

    elif char == "l":
        pass
    elif char == "b":
        sensorLeft = lightSensorLeft.value()
        sensorRight = lightSensorRight.value()

        LINE_THRESHOLD = 10
        while sensorLeft < LINE_THRESHOLD and sensorRight < LINE_THRESHOLD:
            sensorLeft = lightSensorLeft.value()
            sensorRight = lightSensorRight.value()

            print("TsensorLeft: ", sensorLeft, " TsensorRight: ", sensorRight)
            diff = sensorRight - sensorLeft
            motorLeft.duty_cycle_sp = -(BACKWARDS_BASE_SPEED - BACKWARDS_BASE_SPEED * (diff / 200))
            motorRight.duty_cycle_sp = -(BACKWARDS_BASE_SPEED + BACKWARDS_BASE_SPEED * (diff / 200))

            print("Left: " + str(motorLeft.duty_cycle_sp) + "/" + "Right: " + str(motorRight.duty_cycle_sp))
        while True:
            sensorLeft = lightSensorLeft.value()
            sensorRight = lightSensorRight.value()

            print("sensorLeft: ", sensorLeft, " sensorRight: ", sensorRight)
            diff = sensorRight - sensorLeft
            motorLeft.duty_cycle_sp = -(BACKWARDS_BASE_SPEED - BACKWARDS_BASE_SPEED * (diff / 200))
            motorRight.duty_cycle_sp = -(BACKWARDS_BASE_SPEED + BACKWARDS_BASE_SPEED * (diff / 200))

            if sensorRight < LINE_THRESHOLD and sensorLeft < LINE_THRESHOLD:
                break

            print("Left: " + str(motorLeft.duty_cycle_sp) + "/" + "Right: " + str(motorRight.duty_cycle_sp))
    motorLeft.duty_cycle_sp = 0
    motorRight.duty_cycle_sp = 0