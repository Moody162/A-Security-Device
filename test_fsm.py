import unittest
import fsm

class TestFsm(unittest.TestCase):
    
    def test_new_instance_initial_state(self):
        dev = fsm.SecurityDevice()
        self.assertEqual(dev.state, 0)

    def test_unlock_sequence_state(self):
        # unlock code: 828521
        dev = fsm.SecurityDevice()
        
        dev.enter(8)
        dev.enter(2)
        dev.enter(8)
        dev.enter(5)
        dev.enter(2)
        dev.enter(1)

        self.assertEqual(dev.state, dev.UNLOCK_STATE)

    def test_unlock_sequence_output(self):
        # unlock code: 828521
        dev = fsm.SecurityDevice()
        
        dev.enter(8)
        dev.enter(2)
        dev.enter(8)
        dev.enter(5)
        dev.enter(2)
        dev.enter(1)

        self.assertEqual(dev.output(), 'Unlock')

    def test_lock_sequence_state(self):
        # unlock code: 828542
        dev = fsm.SecurityDevice()
        
        dev.enter(8)
        dev.enter(2)
        dev.enter(8)
        dev.enter(5)
        dev.enter(2)
        dev.enter(4)

        self.assertEqual(dev.state, dev.LOCK_STATE)

    def test_lock_sequence_output(self):
        # unlock code: 828524
        dev = fsm.SecurityDevice()
        
        dev.enter(8)
        dev.enter(2)
        dev.enter(8)
        dev.enter(5)
        dev.enter(2)
        dev.enter(4)

        self.assertEqual(dev.output(), 'Lock')

    def test_output_for_states_from_0_to_5(self):
        dev = fsm.SecurityDevice()
        self.assertEqual(dev.state, 0)
        self.assertEqual(dev.output(), None)
        
        dev.enter(8)
        self.assertEqual(dev.state, 1)
        self.assertEqual(dev.output(), None)

        dev.enter(2)
        self.assertEqual(dev.state, 2)
        self.assertEqual(dev.output(), None)
        
        dev.enter(8)
        self.assertEqual(dev.state, 3)
        self.assertEqual(dev.output(), None)
        
        dev.enter(5)
        self.assertEqual(dev.state, 4)
        self.assertEqual(dev.output(), None)
        
        dev.enter(2)
        self.assertEqual(dev.state, 5)
        self.assertEqual(dev.output(), None)

    def test_sequence_number_of_unlocks_and_locks(self):
        # 3 unlocks, 3 lock
        seq = [2, 8, 2, 8, 2, 8, 5, 2, 8, -5, 2, -1, 4, 8, -2, 8, -5, -2, -1, -4, 8, 8, 8, 2, 8, 5, 8, 2, 8, 5, 'a', 'sadcasd', 'random', 'string', 8, 2, 8, -5, 2, 8, 2, 8, 2, 8, 5, 2, 4, 8, 2, -8, -5, -2, 1, 8, 2, 7, 8, 2, 8, 5, 2, 4, 8, 2, 8, 7, 8, 2, 8, 8, 2, 8, 5, 2, 1, 8, 2, 8, 5, 5, 8, 2, 8, 5, 2, 2, 8, 2, 8, 5, 2, 4]

        dev = fsm.SecurityDevice()
        unlocks = locks = 0
        for val in seq:
            dev.enter(val)
            if dev.state == dev.UNLOCK_STATE:
                unlocks += 1
            elif dev.state == dev.LOCK_STATE:
                locks += 1

        self.assertEqual(unlocks, 3)
        self.assertEqual(locks, 3)

test = TestFsm()
test.test_new_instance_initial_state()
test.test_unlock_sequence_state()
test.test_unlock_sequence_output()
test.test_lock_sequence_state()
test.test_lock_sequence_output()
test.test_output_for_states_from_0_to_5()
test.test_sequence_number_of_unlocks_and_locks()
