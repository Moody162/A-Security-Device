#!/usr/bin/env python3

import fsm
import random

# returns the number of generated symbols until the passcode was guessed
def guess_passcode():
    dev = fsm.SecurityDevice()
    
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

print("(min, max, avg) =", guess_average(20))
