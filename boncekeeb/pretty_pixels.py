import time
import board
import neopixel

class pretty_pixels:

    def __init__(self, signal_pin, count, rgbw, brightness, auto_write=False, order=None):
        self.signal_pin = signal_pin
        self.count = count
        self.rgbw = rgbw
        self.brightness = brightness
        self.auto_write = auto_write
        self.order = order
        self.pixels = neopixel.NeoPixel(pin=self.signal_pin, n=self.count, 
                                        bpp=self.rgbw, brightness=self.brightness, 
                                        auto_write=self.auto_write, pixel_order=self.order)

    def wheel(self, pos):
        # Input a value 0 to 255 to get a color value.
        # The colours are a transition r - g - b - back to r.
        if pos < 0 or pos > 255:
            return (0, 0, 0)
        if pos < 85:
            return (255 - pos * 3, pos * 3, 0)
        if pos < 170:
            pos -= 85
            return (0, 255 - pos * 3, pos * 3)
        pos -= 170
        return (pos * 3, 0, 255 - pos * 3)


    def rainbow_cycle(self, wait):
        for j in range(255):
            for i in range(self.count):
                rc_index = (i * 256 // self.count) + j
                self.pixels[i] = self.wheel(rc_index & 255)
            self.pixels.show()
            time.sleep(wait)

    def clear_pixels(self):
        for i in range(self.count):
            self.pixels[i] = 0
        self.pixels.show()
    
    def show_pixel(self, pixel, colour=0xFF0000):
        self.pixels[pixel-1] = colour
        self.pixels.show()

