import RPi.GPIO as io
import time
io.setmode(io.BCM)
in1_pin = 4
in2_pin = 17
###
in3_pin = 27
in4_pin = 22
pwmpin1 = 18
pwmpin2 = 23
io.setup(in1_pin, io.OUT)
io.setup(pwmpin1, io.OUT)
io.setup(in2_pin, io.OUT)

io.setup(in3_pin, io.OUT)
io.setup(pwmpin2, io.OUT)
io.setup(in4_pin, io.OUT)

pwm1 = io.PWM(pwmpin1, 50)
pwm2 = io.PWM(pwmpin2, 50)
pwm1.start(95)
pwm2.start(95)

def clockwise():
	io.output(in1_pin, io.HIGH)
	io.output(in2_pin, io.LOW)
	io.output(in3_pin, io.HIGH)
	io.output(in4_pin, io.LOW)

def counter():
	io.output(in2_pin, io.HIGH)
	io.output(in1_pin, io.LOW)
	io.output(in4_pin, io.HIGH)
	io.output(in3_pin, io.LOW)

clockwise()
j=0;
while(1):
	j =  raw_input("Enter the direction and speed like 0to 9 eg:  9f   or 9r  :")
	pwm1.ChangeDutyCycle(int(j[0])*11)
	pwm2.ChangeDutyCycle(int(j[0])*11)
	if (j[1] == "f"):
		clockwise()
	else:
		counter()
	time.sleep(1)
pwm1.stop()
pwm2.stop()
io.cleanup()		
