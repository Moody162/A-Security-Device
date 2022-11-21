#!/usr/bin/env python3

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
        except:
            self.state = 0

        if self.state == 0:
            if val == 8:
                self.state += 1
            else:
                self.state = 0
        elif self.state == 1:
            if val == 2:
                self.state += 1
            elif val == 8:
                self.state = 1
            else:
                self.state = 0
        elif self.state == 2:
            if val == 8:
                self.state += 1
            else:
                self.state = 0
        elif self.state == 3:
            if val == 5:
                self.state += 1
            elif val == 2:
                self.state = 2
            elif val == 8:
                self.state = 1
            else:
                self.state = 0
        elif self.state == 4:
            if val == 2:
                self.state += 1
            elif val == 8:
                self.state = 1
            else:
                self.state = 0
        elif self.state == 5:
            if val == 1:
                self.state = self.UNLOCK_STATE
            elif val == 4:
                self.state = self.LOCK_STATE
            elif val == 8:
                self.state = 1
            else:
                self.state = 0
        elif self.state == self.UNLOCK_STATE or self.state == self.LOCK_STATE:
            if val == 8:
                self.state = 1
            else:
                self.state = 0

def start_device():
    dev = SecurityDevice()

    while True:
        val = input()
        dev.enter(val)
        #print('Current state', str(dev.state))
        dev.output()

start_device()
