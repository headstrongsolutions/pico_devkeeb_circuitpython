import time
import board
import digitalio

class front_buttons:
    def __init__(self, pins_and_names):
        self.next_time_check = None
        self.pins_and_names = pins_and_names
        self.buttons = []
        self.init_buttons()

    def init_buttons(self):
        buttons = []
        for pin_and_name in self.pins_and_names:
            button = digitalio.DigitalInOut(pin_and_name[1])
            button.direction = digitalio.Direction.INPUT
            button.pull = digitalio.Pull.DOWN
            buttons.append((pin_and_name[0], button))
        self.buttons = buttons
        self.set_time_check()
    
    def set_time_check(self):
        self.next_time_check = time.monotonic_ns() + 250000000

    def test_buttons(self):
        active_button_names = []
        if time.monotonic_ns() >= self.next_time_check:
            for button in self.buttons:
                if button[1].value:
                    active_button_names.append(button[0])
            self.set_time_check()
        return active_button_names
