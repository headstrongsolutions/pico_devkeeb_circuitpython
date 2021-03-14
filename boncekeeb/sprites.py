import time
import board
import displayio
import adafruit_imageload
from boncekeeb.ssd_1306s import ssd_1306s

# display = ssd_1306s(board.GP2, board.GP3, 128, 64)

# # Load the sprite sheet (bitmap)
# sprite_sheet, palette = adafruit_imageload.load("boncekeeb/tiles/dev_tiles.bmp",
#                                                 bitmap=displayio.Bitmap,
#                                                 palette=displayio.Palette)
# # Create a sprite (tilegrid)
# sprite = displayio.TileGrid(sprite_sheet, pixel_shader=palette,
#                             width = 1,
#                             height = 1,
#                             tile_width = 16,
#                             tile_height = 16)

# # Create a Group to hold the sprite
# group = displayio.Group(scale=1)

# # Add the sprite to the Group
# group.append(sprite)

# # Add the Group to the Display
# display.show(group)

# # Set sprite location
# group.x = 0
# group.y = 0

# # Loop through each sprite in the sprite sheet
# source_index = 0
# # while True:
# #     sprite[0] = source_index
# #     if source_index < 20:
# #         source_index += 1
# #         print(source_index)
# #     else:
# #         source_index = 0
# #    time.sleep(2)

class sprite_sheet:
    def __init__(self, display, sheet_file_path, height, width, sprite_names):
        self.display = display
        self.sheet_file_path = sheet_file_path
        self.height = height
        self.width = width
        self.sprite_names = sprite_names
        self.sprite_sheet, self.palette = adafruit_imageload.load(
            self.sheet_file_path,
            bitmap=displayio.Bitmap, 
            palette=displayio.Palette)
        self.sprite = displayio.TileGrid(
                            self.sprite_sheet, 
                            pixel_shader=self.palette,
                            width = 5,
                            height = 4,
                            tile_width = 16,
                            tile_height = 16)
        self.group = displayio.Group(scale=1)
        


        # Create a Group to hold the sprite
        self.group = displayio.Group(scale=1)

        # Add the sprite to the Group
        #self.group.append(self.sprite)

        # Add the Group to the Display
        self.display.show(self.group)

        # Set sprite location
        self.group.x = 48
        self.group.y = 0


    def create_sprites(self, count, sprite_group):
        for sprite in range(0, count):
            sprite = displayio.TileGrid(
                            self.sprite_sheet, 
                            pixel_shader=self.palette,
                            width = 1,
                            height = 1,
                            tile_width = self.width,
                            tile_height = self.height)
            self.group.append(sprite)
            

    def test_sprites(self):
        self.display.show(self.group)
        self.group.x = 0
        self.group.y = 0
        source_index = 0
        while True:
            self.sprite[0] = source_index % 6
            source_index += 1
    
    def show_sprite(self, index, tile_index, x, y):
        self.display.show(self.group)
        self.group.x = x
        self.group.y = y
        self.sprite[index] = tile_index 

    def get_sprite_by_name(self, search_sprite_name):
        sprite_index = [s for s in self.sprite_names if s[0] == "Sh-F5"][0][2]
        return self.sprite[sprite_index]