# A Security Device #

## Project description ##

1. In the first part, `security_device.py` implements a simple Security Device in Python utilizing a Finite State Machine. The unlock code for the Security device is: **828521**. The lock code for the Security Device is: **828524**. THE State Transition Digram of the FSM can be seen below. Input that cannot be understood by the FSM (i.e. characters or strings, for example), will reset the state of the FSM to the initial state (state 0).
2. In the second part, `generator.py` randomly guesses the unlock passcode of the Security Device 20 times, and prints a 3-tuple `(min, max, average)` describing the minumum and maximum number of digits randomly generated until the passcode was guessed, and the average within all 20 times.

![Screenshot from 2022-11-22 17-21-37](https://user-images.githubusercontent.com/16467758/203440884-e4d3daa9-5836-4e7e-9882-520ac116decf.png)
