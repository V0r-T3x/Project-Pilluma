import logging
import time
import toml
from PIL import Image, ImageDraw
from luma.core.interface.serial import spi
from luma.lcd.device import st7789

# Enable debug logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def load_config(file_path):
    """
    Load configuration from a TOML file.
    :param file_path: Path to the TOML file
    :return: Configuration dictionary
    """
    try:
        with open(file_path, "r") as f:
            config = toml.load(f)
            logging.info(f"Configuration loaded from {file_path}")
            return config
    except Exception as e:
        logging.error(f"Error loading configuration from {file_path}: {e}")
        raise

def main():
    try:
        # Load configuration
        config = load_config("screenconfig.toml")
        screen = config["screen"]
        spi_config = config["screen"]["spi"]
        gpio_config = config["screen"]["gpio"]

        # Log the loaded configuration
        logging.info(f"Screen configuration: {screen}")
        logging.info(f"SPI configuration: {spi_config}")
        logging.info(f"GPIO configuration: {gpio_config}")

        # Initialize the SPI interface without the reset pin
        logging.info("Initializing SPI interface")
        serial = spi(
            port=spi_config["spi_port"],
            device=spi_config["spi_device"],
            gpio_DC=gpio_config["gpio_data_command"],
            gpio_CS=gpio_config["gpio_chip_select"],
            gpio_backlight=gpio_config["gpio_backlight"],
            bus_speed_hz=spi_config["spi_bus_speed"],
        )
        logging.info("SPI interface initialized")

        # Initialize the ST7789 display
        logging.info("Initializing ST7789 display")
        device = st7789(serial, width=screen["width"], height=screen["height"], rotate=screen["rotate"], mode=screen["mode"])
        logging.info("ST7789 display initialized")

        # Turn on the backlight
        device.backlight(False)  # Set to False to turn on the backlight
        logging.info("Backlight turned on")

        # Create a blank image for drawing
        logging.info("Creating blank image for drawing")
        image = Image.new("RGB", (screen["width"], screen["height"]), "black")
        draw = ImageDraw.Draw(image)

        # Draw a simple rectangle
        logging.info("Drawing rectangle on the image")
        draw.rectangle((10, 10, screen["width"] - 10, screen["height"] - 10), outline="white", fill="blue")

        # Display the image
        logging.info("Displaying the image on the screen")
        device.display(image)
        logging.info("Displayed test image on the screen")

        # Keep the image displayed for 10 seconds
        time.sleep(10)

    except Exception as e:
        logging.error(f"Error: {e}")

    finally:
        # Turn off the backlight
        device.backlight(True)  # Set to True to turn off the backlight
        logging.info("Backlight turned off")

if __name__ == "__main__":
    main()