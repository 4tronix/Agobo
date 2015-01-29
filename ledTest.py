# Agobo White LED Test
# Flashes White LEDs
# Press Ctrl-C to stop
#
# Run using: sudo python ledTest.py

import time
import agobo

agobo.init()

flashRate = 0.2
try:
    while True:
        agobo.setLED(0, 1)
        time.sleep(flashRate)
        agobo.setLED(0, 0)
        agobo.setLED(1, 1)
        time.sleep(flashRate)
        agobo.setLED(1,0)
                          
except KeyboardInterrupt:
    print

finally:
    agobo.cleanup()
