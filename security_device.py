#!/usr/bin/env python3

import fsm

def start_device():
    dev = fsm.SecurityDevice()
    while True:
        val = input()
        dev.enter(val)
        #print('Current state', str(dev.state))
        message = dev.output()
        if message:
            print(dev.output())

start_device()
