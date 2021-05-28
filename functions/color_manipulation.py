from functions.change_color_to_8_bit import *

def change_color_mode(average_rgb_values_2d_list, SETTINGS):
    if SETTINGS["COLOR_MODE"] == "rgb":
        return average_rgb_values_2d_list
    elif SETTINGS["COLOR_MODE"] == "gray_scale":
        return list(map(lambda rgb: (max(rgb), max(rgb), max(rgb)), average_rgb_values_2d_list))
    elif SETTINGS["COLOR_MODE"] == "8_bit":
        return list(map(lambda rgb: change_color_to_8_bit(rgb, SETTINGS["EIGHT_BIT_MODE"]), average_rgb_values_2d_list))
    return average_rgb_values_2d_list
