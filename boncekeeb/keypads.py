import time
import digitalio
import board
import adafruit_matrixkeypad
from boncekeeb.keypad_key_state import keypad_key_state
  
class keypads:
    def __init__(self, cols, rows, keys):
        self.cols = [digitalio.DigitalInOut(x) for x in cols]
        self.rows = [digitalio.DigitalInOut(x) for x in rows]
        self.keys = keys
        self.adafruit_keypad = adafruit_matrixkeypad.Matrix_Keypad(self.rows, self.cols, self.keys)
        self.key_count = len(cols) * len(rows)
        self.key_states = self.set_states()

    def set_states(self):
        states = []
        if self.key_count > 0:
            for key_index in range(1, self.key_count+1):
                key_state = keypad_key_state(key_index=key_index)
                states.append(key_state)
        return states

    def pressed_keys(self):
        temp_key_states = self.adafruit_keypad.pressed_keys
        if len(temp_key_states) > 0:
            self.key_states = self.get_states()
        for key in self.key_states:
            for temp_key_index in temp_key_states:
                if int(temp_key_index) == key.key_index:
                    key.press()
                else:
                    key.release()
    
    def get_states(self):
        return self.key_states
