from ev3dev import ev3

motorRight = ev3.LargeMotor('outA')
motorLeft = ev3.LargeMotor('outB')
motorLeft.run_direct()
motorRight.run_direct()


print('Shutting down gracefully')
motorRight.duty_cycle_sp = 0
motorLeft.duty_cycle_sp = 0

exit(0)
