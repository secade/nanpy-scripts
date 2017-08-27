from time import sleep
from nanpy import ArduinoApi
from nanpy import DHT
from nanpy import SerialManager

print 'Booting system'

LED_PIN = 13
DHT_PIN = 12
PRES_PIN = 'A0'
WET_PIN = 'A1'

CONNECTION = SerialManager(device='/dev/cu.usbmodem1411')
ARDUINO = ArduinoApi(connection=CONNECTION)
ENV_SENSOR = DHT(DHT_PIN, DHT.DHT22, connection=CONNECTION)

# Setup
ARDUINO.pinMode(LED_PIN, ARDUINO.OUTPUT)
ARDUINO.pinMode(DHT_PIN, ARDUINO.INPUT)
ARDUINO.pinMode(PRES_PIN, ARDUINO.INPUT)
ARDUINO.pinMode(WET_PIN, ARDUINO.INPUT)
# MEANINGLESS DATA STILL

# Loop
try:
    while True:
        ARDUINO.digitalWrite(LED_PIN, ARDUINO.HIGH)
        print 'Gathering data...'
        pres = ARDUINO.analogRead(PRES_PIN)
        print 'Light Resistance: ', pres
        temp = ENV_SENSOR.readTemperature(True)
        print 'Temperature: %.2f Farenheit' % temp
        hum = ENV_SENSOR.readHumidity()
        print 'Humidity: %2.f %%' % hum
        wet = ARDUINO.analogRead(WET_PIN)
        print 'Wetness: %(wet)03d' % locals()
        ARDUINO.digitalWrite(LED_PIN, ARDUINO.LOW)
        print ''
        sleep(3)
except Exception as error:
    if hasattr(error, 'message'):
        print(error.message)
    else:
        print(error)
    print 'Shutting down script'
    ARDUINO.digitalWrite(LED_PIN, ARDUINO.LOW)
