"""
File: ghost.py
--------------
Assignment #3 - CS106A of Stanford University
There are 3 pictures of Stanford, but each image has people walking through the scene.
With the ghost.py, the pictures are figured out a way to "ghost" out all the people and make them disappear
and giving a clear view of the scene without people in a new picture.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the square of the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): squared distance between red, green, and blue pixel values

    This Doctest creates a simple green image and tests against
    a pixel of RGB values (0, 0, 255)
    >>> green_im = SimpleImage.blank(20, 20, 'green')
    >>> green_pixel = green_im.get_pixel(0, 0)
    >>> get_pixel_dist(green_pixel, 0, 255, 0)
    0
    >>> get_pixel_dist(green_pixel, 0, 255, 255)
    65025
    >>> get_pixel_dist(green_pixel, 5, 255, 10)
    125
    """
    red_difference = pixel.red - red
    green_difference = pixel.green - green
    blue_difference = pixel.blue - blue

    color_squared_distance = red_difference ** 2 + green_difference ** 2 + blue_difference ** 2

    return color_squared_distance


def get_best_pixel(pixel1, pixel2, pixel3):
    """
    Given three pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across
    all pixels.

    Input:
        three pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    This doctest creates a red, green, and blue pixel and runs some simple tests.
    >>> green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    >>> red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    >>> blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    >>> best1 = get_best_pixel(green_pixel, blue_pixel, blue_pixel)
    >>> best1.red, best1.green, best1.blue
    (0, 0, 255)
    >>> best2 = get_best_pixel(green_pixel, green_pixel, blue_pixel)
    >>> best2.red, best2.green, best2.blue
    (0, 255, 0)
    >>> best3 = get_best_pixel(red_pixel, red_pixel, red_pixel)
    >>> best3.red, best3.green, best3.blue
    (255, 0, 0)
    """
    average_red = (pixel1.red + pixel2.red + pixel3.red) / 3
    average_green = (pixel1.green + pixel2.green + pixel3.green) / 3
    average_blue = (pixel1.blue + pixel2.blue + pixel3.blue) / 3

    distance_pixel1 = get_pixel_dist(pixel1, average_red, average_green, average_blue)
    distance_pixel2 = get_pixel_dist(pixel2, average_red, average_green, average_blue)
    distance_pixel3 = get_pixel_dist(pixel3, average_red, average_green, average_blue)

    if distance_pixel1 <= distance_pixel2 and distance_pixel1 <= distance_pixel3:
        return pixel1
    elif distance_pixel2 <= distance_pixel1 and distance_pixel2 <= distance_pixel3:
        return pixel2
    else:
        return pixel3


def create_ghost(image1, image2, image3):
    """
    Given three image objects, this function creates and returns a Ghost
    solution image based on the images passed in. All the images passed
    in will be the same size.

    Input:
        three images to be processed
    Returns:
        a new Ghost solution image
    """
    width = image1.width
    height = image1.height
    ghost_image = SimpleImage.blank(width, height)

    for y in range(height):
        for x in range(width):
            pixel1 = image1.get_pixel(x, y)
            pixel2 = image2.get_pixel(x, y)
            pixel3 = image3.get_pixel(x, y)
            pixel = get_best_pixel(pixel1, pixel2, pixel3)
            ghost_image.set_pixel(x, y, pixel)

    return ghost_image


######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########


def jpgs_in_dir(directory):
    """
    DO NOT MODIFY
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(directory):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(directory, filename))
    return filenames


def load_images(directory):
    """
    DO NOT MODIFY
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints to terminal the names of the files it loads.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(directory)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # DO NOT MODIFY
    args = sys.argv[1:]
    if len(args) != 1:
        print('Please specify directory of images on command line')
        return

    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    result = create_ghost(images[0], images[1], images[2])
    if result:
        print("Displaying image!")
        result.show()
    else:
        print("No image to display!")


if __name__ == '__main__':
    main()
