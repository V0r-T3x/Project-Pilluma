**OLED Eyes Animation Script**

**WORK IN PROGRESS!!!**

Started as a cozmo/vector like eye plugin for the pwnagotchi, based on the [FluxGarage RoboEyes Library for arduino](https://github.com/FluxGarage/RoboEyes/tree/main).
I try to translate the arduino libraries features to python as a framework for displaying the pwnagotchis mood on an oled screen, that can be used for many other projects as well.
To make it flexible it is using the luma libraries for display handling, and PIL for drawing the frames from primitives (rounded rectangles, polygons etc.). It supports configurable screen settings, eye shapes, and a variety of animations, including eye movement, blinking, face expressions, and more. The script is designed to be modular and customizable through configuration files. 

**Implemented features:**
  - SSD1306 driver is tested and working with 128x64 and 128x32 screens, SH1107 driver is tested and working with 128x128 screen
  - Default eye and display settings are loaded from the script, but can be changed with eye.config.toml and screenconfig.toml.
  - Predefined faces with "eyelids" to display more emotions (angry, tired, happy).
  - Eye movement with look commands to cardinal directions (C,T,R,B,L and diagonals) and predefined speeds (slow, medium, fast).
  - Blinking and eye closing/openng animation with predefined blink speeds (slow, medium, fast) and option for eyes (both, left, right).
  - Curious mode, where the outer eye is 40% larger, while the inner is 40% smaller than the default.
  - **Pimoroni Pan-Tilt hat support to add head movement that follows the eye position.**

**Future plan:**
  - Matching feature set with the arduino library.
  - Display support for all displays in the luma.oled/luma.lcd library. Predefined screen config files for popular screens.
  - Fluid animation when changing faces (eyelid movement), and turning on/off curious mode (eye size). (Adding threading to have simultaneous move/blink routines for more complex animations)
  - Fix the get_constraints to calculate with eye size changes during curious mode.
  - Idle mode with autoblinker and random movements.
  - Adding animations like wake_up, sleep etc. to match pwnagotchi faces. (wakeup is already implemented to the main test loop)
  - Adding values for happiness/angriness/tiredness to draw eyelids proportionally to these values.
  - Eyeconfig randomizer. If the eyeconfig is not available for first run, the paramaters are choosen randomly or based on a seed like the pwnagotchis RSA-key (regarding the screen sizes to avoid extreme values), this way all pwnys could have different faces, but still could be edited after the first run.

**Features:**

*Configurable Screen Parameters:* 
 - Supports different OLED and LCD types (ssd1306, st7789, etc.) with I2C and SPI interfaces.
 - Default settings are defined in the script.
 - External configuration files (screenconfig.toml, eyeconfig.toml) can override defaults.
  - screenconfig.toml: Defines screen settings, including type, driver, resolution, and interface.
  - eyeconfig.toml: Defines eye parameters such as size, roundness, and distance. For color screens eye and background color could be set up as well.

*Dynamic Eye Animations:*
 - Idle movements (smooth position transitions). (ongoing)
 - Eye blinking with adjustable speed and synchronization.
 - Eye closing and opening animations.
 - Expressive face changes (e.g., happy, angry, tired).
 - Eye "look" animations in all directions.
 - Add or modify animations in the script for new behaviors or expressions.

*Wakeup Animation*: 
  - A sequence of opening and closing animations to simulate waking up.

*Curious Mode*: 
 - Adjusts the eye shape dynamically based on movement.

*Flexible Configuration:*
 - Screen dimensions, driver settings, and interfaces.
 - Eye dimensions, roundness, and distance between the eyes.

*Debugging and Logging:* 
 - Comprehensive logging for easy debugging and performance analysis.
 Enable or adjust logging by modifying the logging.basicConfig call at the start of the script. Logs include debug information about configuration, device initialization, and animation states.

**Prerequisites and installation**

**Don't follow this, these are basically notes for myself for now!!**

Python 3.7 or later
luma.oled and luma.lcd
PIL (Python Imaging Library)
toml
logging
threading

```bash
sudo apt install python3-pip python3-setuptools python3-dev python3-pantilthat
git clone https://github.com/rm-hull/luma.core.git
cd luma.core
pip install -r requirements.txt
sudo python3 setup.py install
cd~
git clone https://github.com/rm-hull/luma.oled.git
cd luma.oled
pip install -r requirements.txt
sudo python3 setup.py install
cd~
git clone https://github.com/rm-hull/luma.lcd.git
cd luma.lcd
pip install -r requirements.txt
sudo python3 setup.py install
```

Modify config.txt in /boot/fiirmware/ for higher I2C speeds:
```
dtparam=i2c_arm=on,i2c_arm_baudrate=400000
```

**BOM**

*pan tilt hat:*
https://thepihut.com/products/pan-tilt-hat?variant=696837832721

*there is no head pack now but can bought separately:*
https://thepihut.com/products/mini-pan-tilt-kit-assembled-with-micro-servos?variant=27739702673

*stemmaqt oled screen:*
https://thepihut.com/products/adafruit-monochrome-1-12-128x128-oled-graphic-display-stemma-qt-qwiic?variant=41322023583939

*stemma cable with female connectors to connect the screen:*
https://thepihut.com/products/stemma-qt-qwiic-jst-sh-4-pin-cable-with-premium-female-sockets-150mm-long

*male headers for the pantilt hat (works with friction fit but I will solder it):*
https://thepihut.com/products/break-away-0-1-36-pin-strip-right-angle-male-header-10-pack

*And all of it is on a pi3A+ with the geekworm case*
https://geekworm.com/products/p88?srsltid=AfmBOopiZOh1NuZKwYpvqdJRQvj6jh4go5El5dudx6dtSsQ94RDZkZkV

License
This project is open-source. Feel free to modify and adapt it to your needs.
