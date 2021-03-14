import board
import busio
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306

class ssd_1306s:
    def __init__(self, sda_pin, scl_pin, width, height, address=0x3c):
        self.address = address
        self.sda_pin = sda_pin
        self.scl_pin = scl_pin
        self.width = width
        self.height = height
        self.display = None
        self.initialise_screen()

    def initialise_screen(self):
        displayio.release_displays()
        self.i2c = busio.I2C(self.scl_pin, self.sda_pin)
        self.display_bus = displayio.I2CDisplay(self.i2c, device_address=self.address)
        self.display = adafruit_displayio_ssd1306.SSD1306(self.display_bus, width=self.width, height=self.height)

    def load(self):
        splash = displayio.Group(max_size=10)
        self.display.show(splash)

        color_bitmap = displayio.Bitmap(128, 64, 1)
        color_palette = displayio.Palette(1)
        color_palette[0] = 0xFFFFFF  # White

        bg_sprite = displayio.TileGrid(
            color_bitmap, pixel_shader=color_palette, x=0, y=0)
        splash.append(bg_sprite)

        # Draw a smaller inner rectangle
        inner_bitmap = displayio.Bitmap(118, 56, 1)
        inner_palette = displayio.Palette(1)
        inner_palette[0] = 0x000000  # Black
        inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=5, y=4)
        splash.append(inner_sprite)

        # Draw a label
        text = "Bonce's Keeb"
        text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=28, y=30)
        splash.append(text_area)

    def test_text(self, string):
        splash = displayio.Group(max_size=10)
        self.display.show(splash)
        text = str(string)
        text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=28, y=30)
        splash.append(text_area)
    
    def show(self, thing):
        self.display.show(thing)