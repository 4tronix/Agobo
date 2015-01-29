# Agobo Motor Test
# Moves: Forward, Reverse, turn Right, turn Left, Stop - then repeat
# Press Ctrl-C to stop
#
# To check wiring is correct ensure the order of movement as above is correct
# Run using: sudo python motorTest.py


import agobo, time

speed = 80

agobo.init()

# main loop
try:
    while True:
        agobo.forward(speed)
        print 'Forward'
        time.sleep(3)
        agobo.reverse(speed)
        print 'Reverse'
        time.sleep(3)
        agobo.spinRight(speed)
        print 'Spin Right'
        time.sleep(3)
        agobo.spinLeft(speed)
        print 'Spin Left'
        time.sleep(3)
        agobo.stop()
        print 'Stop'
        time.sleep(3)

except KeyboardInterrupt:
    print

finally:
    agobo.cleanup()
    
