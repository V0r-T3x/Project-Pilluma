OLED Eyes Animation Script
This Python script animates two eyes on an OLED screen using the luma.oled and PIL libraries. It supports configurable screen settings, eye shapes, and a variety of animations, including eye movement, blinking, face expressions, and more. The script is designed to be modular and customizable through configuration files.

Features
Configurable Screen Parameters: Supports different OLED and LCD types (ssd1306, st7789, etc.) with I2C and SPI interfaces.
Dynamic Eye Animations:
Idle movements (smooth position transitions).
Eye blinking with adjustable speed and synchronization.
Eye closing and opening animations.
Expressive face changes (e.g., happy, angry, tired).
Eye "look" animations in all directions.
Curious Mode: Adjusts the eye shape dynamically based on movement.
Wakeup Animation: A sequence of opening and closing animations to simulate waking up.
Flexible Configuration:
Screen dimensions, driver settings, and interfaces.
Eye dimensions, roundness, and distance between the eyes.
Debugging and Logging: Comprehensive logging for easy debugging and performance analysis.
How It Works
Configuration:

Default settings are defined in the script.
External configuration files (screenconfig.toml, eyeconfig.toml) can override defaults.
Device Initialization:

The script initializes the OLED or LCD screen based on the configuration.
Supports I2C and SPI connections, dynamically loading the appropriate driver.
Animation Logic:

draw_eyes: Core function that draws the eyes with optional parameters for blinking, movement, and expressions.
look, blink, eye_close, eye_open, and wakeup: Helper functions for specific animations.
Smooth transitions and animation speeds are achieved using frame delays.
Main Loop:

Demonstrates the features through pre-programmed animations, such as wakeup, face changes, and various movements.
Setup
Prerequisites
Python 3.7 or later
Required libraries:
luma.oled or luma.lcd
PIL (Python Imaging Library)
toml
logging
Install dependencies using pip:

bash
Kód másolása
pip install luma.oled luma.lcd pillow toml
Configuration
screenconfig.toml: Defines screen settings, including type, driver, resolution, and interface.
eyeconfig.toml: Defines eye parameters such as size, roundness, and distance.
Example screenconfig.toml:

toml
Kód másolása
[screen]
type = "oled"
driver = "ssd1306"
width = 128
height = 64
interface = "i2c"
[screen.i2c]
address = "0x3C"
i2c_port = 1
Example eyeconfig.toml:

toml
Kód másolása
[render]
fps = 30

[eye]
distance = 10
[eye.left]
width = 36
height = 36
roundness = 8
[eye.right]
width = 36
height = 36
roundness = 8
Running the Script
Execute the script with:

bash
Kód másolása
python eyes.py
Customization
Modify the configuration files for custom screen and eye settings.
Add or modify animations in the script for new behaviors or expressions.
Logging
Enable or adjust logging by modifying the logging.basicConfig call at the start of the script. Logs include debug information about configuration, device initialization, and animation states.

License
This project is open-source. Feel free to modify and adapt it to your needs.
