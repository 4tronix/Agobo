# Agobo IR Sensor Test
# Prints IR sensor values whenever they change
# Press Ctrl-C to stop
#
# Run using: sudo python irTest.py

import sys, time
import agobo

agobo.init()


try:
    lastLineL = agobo.irLeftLine()
    lastLineR = agobo.irRightLine()
    print 'LeftLine, RightLine:', lastLineL, lastLineR
    print
    while True:
        newLineL = agobo.irLeftLine()
        newLineR = agobo.irRightLine()
        if (newLineL != lastLineL) or (newLineR != lastLineR):
            print 'LeftLine, RightLine:', newLineL, newLineR
            print
            lastLineL = newLineL
            lastLineR = newLineR
        time.sleep(0.1)
                          
except KeyboardInterrupt:
    print

finally:
    agobo.cleanup()
