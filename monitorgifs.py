import spidev
from PIL import Image, ImageSequence
import time

# ILI9341 display configuration
SPI_BUS = 0
SPI_DEVICE = 0
SPEED_HZ = 16000000  # SPI speed, adjust as needed

# Initialize SPI
spi = spidev.SpiDev()
spi.open(SPI_BUS, SPI_DEVICE)
spi.max_speed_hz = SPEED_HZ

# ILI9341 commands
ILI9341_SWRESET = 0x01
ILI9341_DISPON = 0x29
ILI9341_CASET = 0x2A
ILI9341_PASET = 0x2B
ILI9341_RAMWR = 0x2C

# ILI9341 display dimensions
WIDTH = 240
HEIGHT = 320

# Function to send a command to the display
def send_command(command):
    spi.xfer2([command])

# Function to send data to the display
def send_data(data):
    spi.xfer2(data)

# Function to initialize the ILI9341 display
def initialize_display():
    send_command(ILI9341_SWRESET)
    time.sleep(0.1)
    send_command(ILI9341_DISPON)

# Function to display a GIF on the ILI9341 display
def display_gif(gif_path):
    image = Image.open(gif_path)

    # Initialize display
    initialize_display()

    for frame in ImageSequence.Iterator(image):
        # Resize the frame to match the display dimensions
        frame = frame.resize((WIDTH, HEIGHT), Image.ANTIALIAS)

        # Convert the frame to RGB mode
        frame = frame.convert("RGB")

        # Extract RGB values
        pixels = list(frame.getdata())

        # Set the column and page addresses
        send_command(ILI9341_CASET)
        send_data([0x00, 0x00, 0x00, WIDTH - 1])
        send_command(ILI9341_PASET)
        send_data([0x00, 0x00, 0x00, HEIGHT - 1])

        # Write pixel data to the display
        send_command(ILI9341_RAMWR)
        send_data(sum(pixels, ()))

        time.sleep(0.1)  # Adjust delay as needed

# Example usage
if __name__ == "__main__":
    gif_path = "happy"
    display_gif(gif_path)
