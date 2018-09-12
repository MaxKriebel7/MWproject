import time
import RPi.GPIO as GPIO        # erst die imports damit es funktiniert

LIGHT_SENSOR_PIN = 4           # dann pin angeben fuer den lightsensor


def init():
     GPIO.setmode(GPIO.BCM)
     GPIO.setup(LIGHT_SENSOR_PIN,GPIO.IN)      # allgemeinheiten BCM, setmode, setup

counter = 0     # zaehleinheit

try:
    while True:   # 4 ever loop
        init()    # ?
        light_barrier_input = GPIO.input(LIGHT_SENSOR_PIN)       # ?
        if light_barrier_input == True:
            print "detected!"
            counter = counter + 1
            print('number of passed people %s' % counter)      # %s' % ... == entspricht
        else:
            print "NOT DETECTED!!!!!"    
        time.sleep(0.1)               # wait half a second

except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt
    stop()
    GPIO.cleanup()
