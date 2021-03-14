import board
import time
import displayio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

from boncekeeb.ssd_1306s import ssd_1306s
from boncekeeb.pretty_pixels import pretty_pixels
from boncekeeb.keypads import keypads
from boncekeeb.front_buttons import front_buttons
from boncekeeb.sprites import sprite_sheet 


# == screen setup == #
display = ssd_1306s(board.GP2, board.GP3, 128, 64)

# == spritesheets setup == #
dev_sprite_names = [
    ["Esc", Keycode.ESCAPE, 0],
    ["Home", Keycode.HOME, 1],
    ["Up", Keycode.UP_ARROW, 2],
    ["Down", Keycode.DOWN_ARROW, 3],
    ["Left", Keycode.LEFT_ARROW, 4],
    ["Right", Keycode.RIGHT_ARROW, 5],
    ["End", Keycode.END, 6],
    ["Pg-Up", Keycode.PAGE_UP, 7],
    ["F5", Keycode.F5, 8],
    ["Sh-F5", [Keycode.SHIFT, Keycode.F5], 9],
    ["F10", Keycode.F10, 10],
    ["F11", Keycode.F11, 11],
    ["F8", Keycode.F8, 11],
    ["F12", Keycode.F12, 12],
    ["Pg-Dn", Keycode.PAGE_DOWN, 15],
    ["Sh-Del", [Keycode.SHIFT, Keycode.DELETE], 16],
    ["Tilde", [Keycode.SHIFT, Keycode.GRAVE_ACCENT], 17],
    ["Baktik", Keycode.GRAVE_ACCENT, 17]
]

dev_sprites = sprite_sheet(display, 
                    "boncekeeb/tiles/dev_tiles.bmp", 
                    16, 16, dev_sprite_names)


# == front buttons setup == #
names_and_pins = [ ["Blue", board.GP21, 0x0000ff],
                   ["Green", board.GP20, 0x00ff00],
                   ["Red", board.GP19, 0xff0000],
                   ["Yellow", board.GP18, 0xffff00] ]
front_buttons = front_buttons(names_and_pins)
selected_color = "Red"

def get_colour(colour_name):
    button = [button for button in names_and_pins if button[0] == colour_name]
    return button[0][2]


# == keyboard setup == #
cols = (board.GP13, board.GP12, board.GP11, board.GP10, board.GP9)
rows = (board.GP22, board.GP26, board.GP27, board.GP28)
keys = [["1", "2", "3", "4", "5"],
        ["6", "7", "8", "9", "10"],
        ["11", "12", "13", "14", "15"],
        ["16", "17", "18", "19", "20"]]
keypad = keypads(cols, rows, keys)

# == neopixels setup == #
pixels = pretty_pixels(board.GP0, 20, 3, 0.5, False, None)

for n in range(1,2):
    pixels.rainbow_cycle(0)
#pixels.clear_pixels()
wipe_cycle = time.monotonic() +2

def key_to_pixel(key_index):
    if key_index == 5:
        return 1
    elif key_index == 10:
        return 2
    elif key_index == 15:
        return 3
    elif key_index == 20:
        return 4
    elif key_index == 19:
        return 5
    elif key_index == 14:
        return 6
    elif key_index == 9:
        return 7
    elif key_index == 4:
        return 8
    elif key_index == 3:
        return 9
    elif key_index == 8:
        return 10
    elif key_index == 13:
        return 11
    elif key_index == 18:
        return 12
    elif key_index == 17:
        return 13
    elif key_index == 12:
        return 14
    elif key_index == 7:
        return 15
    elif key_index == 2:
        return 16
    elif key_index == 1:
        return 17
    elif key_index == 6:
        return 18
    elif key_index == 11:
        return 19
    elif key_index == 16:
        return 20

esc_sprite = dev_sprites.get_sprite_by_name("Esc")


while True:
    keypad.pressed_keys()
    for key in keypad.get_states():
        if key.triggering() is True:
            print(key.key_index)
            pixel_index = key_to_pixel(key.key_index)
            if pixel_index:
                pixels.show_pixel(pixel_index, get_colour(selected_color))
        # else:
        #     # TODO - fix key release
        #     #key.release()
            
    # TODO - make pixel states independant so they 
    # can hide themselves or reset back to the 
    # original set colour
    if time.monotonic() >= wipe_cycle:
        #pixels.clear_pixels()
        wipe_cycle = time.monotonic() +2
    
    front_buttons_pressed = front_buttons.test_buttons()
    if len(front_buttons_pressed) > 0:
        if selected_color != front_buttons_pressed[0]: 
            selected_color = front_buttons_pressed[0]
            display.test_text(front_buttons_pressed)


    #time.sleep(0.1)
    
