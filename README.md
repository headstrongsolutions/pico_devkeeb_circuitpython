# Devkeeb - a macro keyboard with display and rgb led's

It's called DevKeeb as I wanted a macro keyboard for common debug buttons (f5, sh+f5, f10, f11 etc).

I want to use a Raspberry Pi Pico for this as the boards are extremely cheap, but extremely powerful and have a lot of pin. The 'bang-to-buck' makes it a no-brainer.

I want it to have different 'layers' which mean knowing which keyboard button corresponds with which pressed key is a pain, so I'll backlight them with individual RGB LED's.

I want the different layers to be selectable from buttons on the front face.
I want a OLED LCD screen as a display on the front to display the currently selected keyboard layer.

I started this as a collection of C projects to solve each individual problem and frankly I'll likely go back to that when I've polished the funcitonality, but I was having teething problems with understanding how to mix and match C and C++ projects into one project, so I switched to Python as I'm more comfortable with that.
Micro Python at time of writing hasn't yet had an USB-HID implementation created for the RP2040 (the chip on a Raspberry Pi Pico), meaning at this time I can't use it as a keyboard (HID == Human Interface Device, so a keyboard, mouse etc).

Adafruit's Circuit Python however does have a functioning HID library for the RP2040, so to get this moving I've switched to using that for this project.

It's outside of scope on this project to go into the detail of running Circuit Python, there are many guides out there to do that, however I do use VS Code along with some extensions to make my life easier, so I will be holding those VSCode project settings in this repo (short story, this repo might help guide you on your way to getting Circuit Python and VSCode working nicely ;) ).

Quick disclaimer, this project is just to get the device working as a prototype, I fully plan to move this to c/c++ as soon as I've worked out the main usages through this project.
