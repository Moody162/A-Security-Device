# A Security Device #

## Project description ##

**IIT Fall 2022 - CS330 Coding assignment**

1. In the first part, `security_device.py` implements a simple Security Device in Python utilizing a Finite State Machine. The unlock code for the Security device is: **828521**. The lock code for the Security Device is: **828524**. THE State Transition Digram of the FSM can be seen below. Input that cannot be understood by the FSM (i.e. characters or strings, for example), will reset the state of the FSM to the initial state (state 0).

2. In the second part, `generator.py` randomly guesses the unlock passcode of the Security Device 20 times, and prints a 3-tuple `(min, max, average)` 
describing the minumum and maximum number of digits randomly generated until the passcode was guessed, and the average within all 20 times.

Both parts import the `fsm.py` module, where I have implemented the class for a Security Device that utilizes a Finite State Machine. 

![Screenshot from 2022-11-22 17-21-37](https://user-images.githubusercontent.com/16467758/203440884-e4d3daa9-5836-4e7e-9882-520ac116decf.png)

## Getting started ##

Instructions in this README file are for a Linux environment (Ubuntu 22.04).

### Prerequisites ###

In order to effectively setup the project, `python`, the `coverage` Python module, and `git` have to be installed.

1. To install `python`, run the following commands:
```
$ sudo apt update
$ sudo apt install python3
```

2. To install the `coverage` module, run the following command:
```
$ pip install coverage
```

3. To install `git`, run the following commands:
```
$ sudo apt-get update
$ sudo apt-get install git-all
```

### Setup ###

1. Clone the repository:
```
$ git clone https://github.com/Moody162/A-Security-Device.git
```

2. Run unittests and generate coverage data:
```
$ python3 -m coverage run -m unittest
```

3. View unittest coverage report:
```
$ python3 -m coverage report
```

and to generate the coverage report in HTML format:
```
$ python3 -m coverage html
```

The HTML version of the unittest coverage report can be found at `./htmlcov/index.html`.

4. Run the executables:

For the first part of the project, run `security_device.py`, the Security Device simulator:
```
$ ./security_device.py
```
Enter input from keyboard, once at a time, followed by `Enter`.

After every sequence of characters that make up the unlock passcode **828521**, the message "Unlock" should be displayed. 

After every sequence of characters that make up the lock passcode **828524**, the message "Lock" should be displayed.

For the second part, run `generator.py`:
```
$ ./generator.py
```
