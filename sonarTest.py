# Agobo Sonar Test
# Prints the distance read by the ultrasonic sensor every second
# Press Ctrl-C to stop
#
# Run using: sudo python sonarTest.py

import time
import agobo

agobo.init()

try:
    while True:
        dist = agobo.getDistance()
        print "Distance: ", int(dist)
        time.sleep(1)

except KeyboardInterrupt:
    print

finally:
    agobo.cleanup()
