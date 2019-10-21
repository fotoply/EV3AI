from ev3dev import ev3

lightSensorLeft = ev3.ColorSensor('in1')
lightSensorRight = ev3.ColorSensor('in2')

assert lightSensorLeft.connected, "LightSensorLeft(ColorSensor) is not connected"
assert lightSensorRight.connected, "LightSensorRight(ColorSensor) is not conected"

while True:
    sensorLeft = lightSensorLeft.value()
    sensorRight = lightSensorRight.value()

    print("sensorLeft: ", sensorLeft, " sensorRight: ", sensorRight)