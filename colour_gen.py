import random

FLOAT_ERROR = 0.0000005

import math

def hex_to_rgb(hex):
    rgb = hex

    if len(rgb) == 6:
        r, g, b = rgb[0:2], rgb[2:4], rgb[4:6]
    elif len(rgb) == 3:
        r, g, b = rgb[0] * 2, rgb[1] * 2, rgb[2] * 2

    return tuple([int(v, 16)  for v in (r, g, b)])


def rgb_to_lum(rgb):
    vals = []
    for v in rgb:
        v = v / 255
        if v <= 0.03928:
            vals.append(v/12.92)
        else:
            vals.append(math.pow(((v+0.055)/1.055), 2.4))

    return vals[0] * 0.2126 + vals[1] * 0.7152 + vals[2] * 0.0722


def contrast_from_lums(colour1, colour2):
    if colour1 > colour2:
        return 1 / ((colour2 + 0.05) / (colour1 + 0.05))
    return 1 / ((colour1 + 0.05) / (colour2 + 0.05))

def get_random_hex():
    hex_codes = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

    indices = [random.randint(0, len(hex_codes)-1) for _ in range(6)]

    return ''.join([hex_codes[i] for i in indices])

def run():
    colours = []
    ratios = []
    for i in range(10):
        colours.append(get_random_hex())
    for colour1 in colours:
        colour1_lum = rgb_to_lum(hex_to_rgb(colour1))
        for colour2 in colours:
            colour2_lum = rgb_to_lum(hex_to_rgb(colour2))
            ratio = contrast_from_lums(colour1_lum, colour2_lum)
            if ratio != 1:
                ratios.append(ratio)
    with open("average_ratios3.txt", "a+") as f:
        f.write(f"{round(sum(ratios)/len(ratios),1)},{','.join(colours)}\n")

for i in range(100000):
    run()
#
# colour_a = "FF00FF"
# colour_b = "0000FF"
# lum_a = rgb_to_lum(hex_to_rgb(colour_a))
# lum_b = rgb_to_lum(hex_to_rgb(colour_b))
# print(contrast_from_lums(lum_a , lum_b))