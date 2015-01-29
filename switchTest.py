#!/usr/bin/env python
#Simply prints the state of the input button

# Must be run as root - sudo python switchTest.py 

import time, agobo

agobo.init()

print "Press ctrl-C to exit"

try:
  while True:
    if agobo.getSwitch():
      print "ON"
    else:
      print "OFF"
    time.sleep(0.5)

except KeyboardInterrupt:
  print

finally:
  agobo.cleanup()
  
  
