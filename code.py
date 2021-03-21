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
dev_sprite_details = [
    ["Esc", Keycode.ESCAPE, 0xff0000, 0, 17],
    ["Sh-Del", [Keycode.SHIFT, Keycode.DELETE], 0xff0000, 16, 16],
    ["empty", None, 0x000000, 14, 9],
    ["F5", Keycode.F5, 0x00ff6e, 8, 8],
    ["Sh-F5", [Keycode.SHIFT, Keycode.F5], 0xff0000, 9, 1],

    ["Home", Keycode.HOME, 0x6af011, 1, 18],
    ["End", Keycode.END, 0xf782ff, 6, 15],
    ["F9", Keycode.F9, 0xed1351, 12, 10],
    ["F10", Keycode.F10, 0x00ccff, 10, 7],
    ["F11", Keycode.F11, 0x4374b5, 11, 2],

    ["Tilde", [Keycode.SHIFT, Keycode.GRAVE_ACCENT], 0x6af011, 17, 19],
    ["Pg-Up", Keycode.PAGE_UP, 0xf782ff, 7, 14],
    ["empty", None, 0x000000, 14, 11],
    ["Up", Keycode.UP_ARROW, 0x00aaff, 2, 6],
    ["empty", None, 0x000000, 14, 3],

    ["F12", Keycode.F12, 0x00ccff, 13, 20],
    ["Pg-Dn", Keycode.PAGE_DOWN, 0xf782ff, 15, 13],
    ["Left", Keycode.LEFT_ARROW, 0x00aaff, 4, 12],
    ["Down", Keycode.DOWN_ARROW, 0x00aaff, 3, 5],
    ["Right", Keycode.RIGHT_ARROW, 0x00aaff, 5, 4]
]

dev_sprites = sprite_sheet(display, 
                    "boncekeeb/tiles/dev_tiles.bmp", 
                    16, 16, dev_sprite_details)
for i in range(0, len(dev_sprite_details) -1): 
    for y in range (0, 4):
        for x in range (0, 5):
            dev_sprites.sprite[x,y] = dev_sprite_details[i][3]
dev_sprites.group.append(dev_sprites.sprite)
dev_sprites.display.show(dev_sprites.group)

def map_buttons_to_sprites(pixel_count, pixels, sprite_details, sprites):
    print(pixel_count)
    for i in range(0, pixel_count-1):
        selected_pixel = None
        sprite_detail = None
        for sprite in sprite_details:
            if sprite[3] == i:
                sprite_detail = sprite
                selected_color = sprite_detail[2]
                selected_pixel = sprite_detail[4]
                pixels.show_pixel(selected_pixel, selected_color)


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
pixel_count = 20
pixels = pretty_pixels(board.GP0, pixel_count, 3, 0.5, False, None)


def pretty_cycle():
    for n in range(1,2):
        display.test_text("Pretty Cycle: %d" % n)
        pixels.rainbow_cycle(0)
    pixels.clear_pixels()

def get_key_pixel_map(key: int, pixel: int) -> int:
    # array of arrays containing [keyboard_key_index, neopixel_index]
    key_pixel_map = [
        [5, 1], [10, 2], [15, 3], [20, 4], [19, 5], [14, 6],
        [9, 7], [4, 8], [3, 9], [8, 10], [13,11], [18,12],
        [17,13], [12,14], [7,15], [2,16], [1,17], [6,18],
        [11,19], [16,20]
    ]
    # Double check that someone hasn't asked with both key and pixel indexes
    if key and pixel:
        return None
        
    # Return pixel index from key index
    if key:
        return [key_pixel for key_pixel in key_pixel_map if key_pixel[0] == key][0][1]
    
    # Return key index from pixel index
    if pixel:
        return [key_pixel for key_pixel in key_pixel_map if key_pixel[1] == key][0][0]


pretty_cycle()
map_buttons_to_sprites(20, pixels, dev_sprite_details, dev_sprites)

while True:
    keypad.pressed_keys()
    for key in keypad.get_states():
        if key.triggering() is True:
            print(key.key_index)
            pixel_index = get_key_pixel_map(key.key_index, None)
            if pixel_index:
                pixels.show_pixel(pixel_index, get_colour(selected_color))
        # else:
        #     # TODO - fix key release
        #     #key.release()
            
    front_buttons_pressed = front_buttons.test_buttons()
    if len(front_buttons_pressed) > 0:
        if selected_color != front_buttons_pressed[0]: 
            selected_color = front_buttons_pressed[0]
            display.test_text(front_buttons_pressed)

