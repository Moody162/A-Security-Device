#!/usr/bin/env python3

import random

class SecurityDevice:
    # This class implements a security lock device using a FSM
    # Unlock Code = '828521'
    # Lock Code = '828524'

    def __init__(self):
        self.state = 0

        # some class constants
        self.UNLOCK_STATE = 6
        self.LOCK_STATE = 7
    
    def output(self):
        if self.state == self.UNLOCK_STATE:
            print('Unlock')
        elif self.state == self.LOCK_STATE:
            print('Lock')

    def enter(self, val):
        try:
            val = int(val)
            if self.state == 0: # ''
                if val == 8:
                    self.state += 1
                else:
                    self.state = 0
            elif self.state == 1: # '8'
                if val == 2:
                    self.state += 1
                elif val == 8:
                    self.state = 1
                else:
                    self.state = 0
            elif self.state == 2: # '82'
                if val == 8:
                    self.state += 1
                else:
                    self.state = 0
            elif self.state == 3: # '828'
                if val == 5:
                    self.state += 1
                elif val == 2:
                    self.state = 2
                elif val == 8:
                    self.state = 1
                else:
                    self.state = 0
            elif self.state == 4: # '8285'
                if val == 2:
                    self.state += 1
                elif val == 8:
                    self.state = 1
                else:
                    self.state = 0
            elif self.state == 5: # '82852'
                if val == 1:
                    self.state = self.UNLOCK_STATE
                elif val == 4:
                    self.state = self.LOCK_STATE
                elif val == 8:
                    self.state = 1
                else:
                    self.state = 0
            elif self.state == self.UNLOCK_STATE or self.state == self.LOCK_STATE: # '828521' / '828524'
                if val == 8:
                    self.state = 1
                else:
                    self.state = 0
        except:
            pass

# returns the number of generated symbols until the passcode was guessed
def guess_passcode():
    dev = SecurityDevice()
    
    count = 0
    while dev.state != dev.UNLOCK_STATE:
        val = random.randint(0, 9)
        dev.enter(val)
        count += 1
    
    return count

# returns (minimum, maximum, average), the minimum, maximum, and average number of guesses if we guess 'tries' times
def guess_average(tries):
    minimum = maximum = total = guess_passcode()
    for i in range(tries - 1):
        count = guess_passcode()
        total += count

        if count < minimum:
            minimum = count
        if count > maximum:
            maximum = count

    return (minimum, maximum, total / tries)

print("(min, max, avg) =", guess_average(50))

