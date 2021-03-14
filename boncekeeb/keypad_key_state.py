import time 

class keypad_key_state:
    def __init__(self, key_index:int, state=False, timeout_delay=1):
        self.key_index = key_index
        self.state = state
        self.repeating = False
        self.timeout = None
        self.timeout_delay = timeout_delay
    
    def release(self):
        self.timeout = None
        self.state = False
        self.repeating = False

    def press(self):
        time_now = time.monotonic()
        delta_from_now = time_now + self.timeout_delay

        if  self.timeout == None:
            self.timeout = delta_from_now
            self.repeating = False
            self.state = True

        elif self.state and self.timeout != None and self.timeout > time_now:
            self.repeating = True
            self.state = True

        elif self.state and self.timeout != None and self.timeout <= time_now:
            self.timeout = delta_from_now + 1
            self.timeout = None
            self.repeating = False
            self.state = False
    
    def triggering(self):
        if self.state and self.repeating is False:
            return True
        else:
            return False