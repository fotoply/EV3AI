import ev3dev.ev3 as ev3
from time import sleep

import signal

motorRight = ev3.LargeMotor('outA')
motorLeft = ev3.LargeMotor('outB')

THRESHOLD_LEFT = 30
THRESHOLD_RIGHT = 350

BASE_SPEED = 50
BACKWARDS_BASE_SPEED = BASE_SPEED*0.5
TURN_SPEED = 80

lightSensorLeft = ev3.ColorSensor('in1')
lightSensorRight = ev3.ColorSensor('in2')
lightSensorObject = ev3.LightSensor('in3')

assert lightSensorLeft.connected, "LightSensorLeft(ColorSensor) is not connected"
assert lightSensorRight.connected, "LightSensorRight(ColorSensor) is not conected"
assert lightSensorObject.connected, "LightSensorObject(LightSensor) is not conected"

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
testString = "ffrflflfolfrfrfffolfrfrfforflflffforflflffforflflfo"
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
        timeout=0
        while True:
            sensorLeft = lightSensorLeft.value()
            sensorRight = lightSensorRight.value()

            # print("sensorLeft: ", sensorLeft, " sensorRight: ", sensorRight)
            diff = sensorRight - sensorLeft
            motorLeft.duty_cycle_sp = BASE_SPEED - BASE_SPEED * (diff / 200)
            motorRight.duty_cycle_sp = BASE_SPEED + BASE_SPEED * (diff / 200)
            timeout += 1

            if timeout > 20:
                break
        motorRight.duty_cycle_sp = 0
        motorLeft.duty_cycle_sp = 0

        counter = 0
        previous = "w"

        while True:
            sensorRight = lightSensorRight.value()

            motorLeft.duty_cycle_sp = 40
            motorRight.duty_cycle_sp = motorLeft.duty_cycle_sp*-1

            if sensorRight < 10 and previous == "w":
                previous = "b"
                counter += 1
            elif sensorRight > 70 and previous == "b":
                previous = "w"
                counter += 1

            if counter == 2:
                break


    elif char == "l":
        sensorLeft = lightSensorLeft.value()
        sensorRight = lightSensorRight.value()

        LINE_THRESHOLD = 75
        timeout = 0
        while True:
            sensorLeft = lightSensorLeft.value()
            sensorRight = lightSensorRight.value()

            diff = sensorRight - sensorLeft
            motorLeft.duty_cycle_sp = BASE_SPEED - BASE_SPEED * (diff / 200)
            motorRight.duty_cycle_sp = BASE_SPEED + BASE_SPEED * (diff / 200)
            timeout += 1

            if timeout > 20:
                break
        motorRight.duty_cycle_sp = 0
        motorLeft.duty_cycle_sp = 0

        counter = 0
        previous = "w"

        while True:
            sensorLeft = lightSensorLeft.value()

            motorRight.duty_cycle_sp = 40
            motorLeft.duty_cycle_sp = motorRight.duty_cycle_sp * -1

            if sensorLeft < 10 and previous == "w":
                previous = "b"
                counter += 1
            elif sensorLeft > 70 and previous == "b":
                previous = "w"
                counter += 1

            if counter == 2:
                break


    elif char == "b":
        previous = "w"
        counter = 0

        while True:
            sensorLeft = lightSensorLeft.value()
            sensorRight = lightSensorRight.value()

            diff = sensorRight - sensorLeft
            motorLeft.duty_cycle_sp = -(BACKWARDS_BASE_SPEED - diff / 25)
            motorRight.duty_cycle_sp = -(BACKWARDS_BASE_SPEED + diff / 25)

            if sensorLeft < 10 and sensorRight < 10 and previous == "w":
                previous = "b"
                counter += 1
            elif sensorLeft > 75 and sensorRight > 75 and previous == "b":
                previous = "w"
                counter += 1

            if counter == 3:
                break

        motorLeft.duty_cycle_sp = 0
        motorRight.duty_cycle_sp = 0

    elif char == "p":
        sleep(10)

    elif char == "u":
        timeout = 0

        while timeout < 1060:
            motorLeft.duty_cycle_sp = BACKWARDS_BASE_SPEED
            motorRight.duty_cycle_sp = -BACKWARDS_BASE_SPEED
            timeout += 1

    elif char == "o":
        sensorLeft = lightSensorLeft.value()
        sensorRight = lightSensorRight.value()

        counter = 0
        previous = "w"
        LINE_THRESHOLD = 10
        REDUCED_SPEED = BASE_SPEED * 0.6
        while sensorLeft < LINE_THRESHOLD and sensorRight < LINE_THRESHOLD:
            sensorLeft = lightSensorLeft.value()
            sensorRight = lightSensorRight.value()

            diff = sensorRight - sensorLeft
            motorLeft.duty_cycle_sp = REDUCED_SPEED - REDUCED_SPEED * (diff / 200)
            motorRight.duty_cycle_sp = REDUCED_SPEED + REDUCED_SPEED * (diff / 200)

        while True:
            sensorLeft = lightSensorLeft.value()
            sensorRight = lightSensorRight.value()
            sensorObject = lightSensorObject.value()

            diff = sensorRight - sensorLeft
            motorLeft.duty_cycle_sp = REDUCED_SPEED - REDUCED_SPEED * (diff / 200)
            motorRight.duty_cycle_sp = REDUCED_SPEED + REDUCED_SPEED * (diff / 200)

            if sensorObject < 450 and previous == "w":
                previous = "b"
                counter += 1
            elif sensorObject > 600 and previous == "b":
                previous = "w"
                counter += 1

            if counter == 2:
                break

        previous = "w"
        counter = 0

        while True:
            sensorLeft = lightSensorLeft.value()
            sensorRight = lightSensorRight.value()

            diff = sensorRight - sensorLeft
            motorLeft.duty_cycle_sp = -(BACKWARDS_BASE_SPEED - diff / 25)
            motorRight.duty_cycle_sp = -(BACKWARDS_BASE_SPEED + diff / 25)

            if sensorLeft < 10 and sensorRight < 10 and previous == "w":
                previous = "b"
                counter += 1
            elif sensorLeft > 75 and sensorRight > 75 and previous == "b":
                previous = "w"
                counter += 1

            if counter == 1:
                break

        motorLeft.duty_cycle_sp = 0
        motorRight.duty_cycle_sp = 0


    motorLeft.duty_cycle_sp = 0
    motorRight.duty_cycle_sp = 0
