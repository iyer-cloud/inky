"""
Utility functions ported over from Pimoroni for easier use
"""
import time

from PIL import Image
from inky.auto import auto
from inky.inky_uc8159 import CLEAN

inky_display = auto(ask_user=True, verbose=True)
saturation = 0.5
cycles = 3
images_prefix = '~/main/inky/images/'

def reset_screen() -> None:
    """
    Flash through red/black/white and reset the screen
    """
    colours = (inky_display.RED, inky_display.BLACK, inky_display.WHITE)
    colour_names = (inky_display.colour, "black", "white")

    # New canvas to draw on
    img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))

    # Loop through the specified number of cycles and completely
    # fill the display with each colour in turn.

    for i in range(cycles):
        print("Cleaning cycle %i\n" % (i + 1))
        for j, c in enumerate(colours):
            print("- updating with %s" % colour_names[j])
            inky_display.set_border(c)
            for x in range(inky_display.WIDTH):
                for y in range(inky_display.HEIGHT):
                    img.putpixel((x, y), c)
            inky_display.set_image(img)
            inky_display.show()
            time.sleep(1)
        print("\n")

    print("Screen reset complete")


def clear_screen() -> None:
    """
    Flash through all pixels and clear to neutral
    """
    for _ in range(2):
        for y in range(inky.height - 1):
            for x in range(inky.width - 1):
                inky.set_pixel(x, y, CLEAN)

        inky.show()
        time.sleep(1.0)


def render_image(image_name: str) -> None:
    """
    Fetch an image and render it
    """
    image_path = f'{images_prefix}{image_name}'
    image = Image.open(image_path)
    resizedimage = image.resize(inky.resolution)

    inky.set_image(resizedimage, saturation=saturation)
    inky.show()