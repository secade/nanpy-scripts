from time import sleep
from nanpy import ArduinoApi
from nanpy import SerialManager

LED_PIN = 13

# try:
CONNECTION = SerialManager(device='/dev/cu.usbmodem1411')
ARDUINO = ArduinoApi(connection=CONNECTION)
# except:
#     print("Meh")

ARDUINO.pinMode(LED_PIN, ARDUINO.OUTPUT)

def print_stuff():
    print 'Setting ledpin \'', LED_PIN, '\' to: \'', ARDUINO.digitalRead(LED_PIN), '\''

try:
    while True:
        ARDUINO.digitalWrite(LED_PIN, ARDUINO.HIGH)
        print_stuff()
        sleep(1)
        ARDUINO.digitalWrite(LED_PIN, ARDUINO.LOW)
        print_stuff()
        sleep(1)
except:
    print 'Shutting down script'
    ARDUINO.digitalWrite(LED_PIN, ARDUINO.LOW)

