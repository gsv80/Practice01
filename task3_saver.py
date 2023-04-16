# --------------------- task 3 -----------------------------

import math
import unittest

import test
from test import find_opt_angle


def input_dist_feet(text):
    x = float(input("Enter distance {0}, in feets: ".format(text)))
    return x


def input_dist_yards(text):
    x = float(input("Enter distance {0}, in yards: ".format(text)))
    return x


def input_velocity(text):
    x = float(input("Enter velocity {0}, in miles per hour ".format(text)))
    return x


def input_start_angle(text):
    x = float(input("Enter {0} angle , in grades ".format(text)))
    return x


d1 = input_dist_yards("from lifesaver to shore line")
d2 = input_dist_feet("from drowning person to shore line")
h = input_dist_yards("from lifesaver to drowning man by vertical")
v_sand = input_velocity("on shore")
v_water = input_velocity("in water")
n = v_sand / v_water
# theta = input_start_angle("lifesaver's way start")

print(d1, d2, h, v_sand, v_water, n)


# ---------------- check and format input data functions --------------

def yards_to_feet(yards):
    return float(yards) * 3


def angle_to_rad(grades):
    return float(grades) * math.pi / 180


def velocity_feet_sec(miles_hour):
    return float(miles_hour) * 5280 / 3600


# values for use in calculations ---------------------------------------

d1_feet = yards_to_feet(d1)
d2_feet = d2
h_feet = yards_to_feet(h)
v_sand_feet_sec = velocity_feet_sec(v_sand)
v_water_feet_sec = velocity_feet_sec(v_water)


# theta_rad = angle_to_rad(theta)


# try to find the best solution for the overall time


# function to calculate distance


def calc_vert_side(hor_side, alpha):
    vert_side = hor_side * math.tan(alpha)
    return vert_side


def calc_hypo(side_one, side_two):
    hypo = math.sqrt(side_one ** 2 + side_two ** 2)
    return hypo


h1_feet = calc_vert_side(d1_feet, test.find_opt_angle(d1_feet, d2_feet, h_feet, n))
print("#### optimized angle:", test.find_opt_angle(d1_feet, d2_feet, h_feet, n) * 180 / math.pi)
h2_feet = h_feet - h1_feet

length_shore = calc_hypo(d1_feet, h1_feet)
length_water = calc_hypo(d2_feet, h2_feet)


# ----- time calculation
def time_calc(distance, velocity):
    time = distance / velocity
    return time


time_shore = time_calc(length_shore, v_sand_feet_sec)
time_water = time_calc(length_water, v_water_feet_sec)

print("length_shore : {0} feet, v_sand_feet_sec : {1} feet/sec".format(length_shore, v_sand_feet_sec))
print("time_shore : {0} sec".format(time_shore))
print("length_water : {0} feet, v_water_feet_sec : {1} feet/sec".format(length_water, v_water_feet_sec))
print("time_water : {0} sec".format(time_water))
time_overall = time_shore + time_water

print("time_overall : ", time_overall, "sec")


# unit tests

class TestCalculationMethods(unittest.TestCase):
    def test_calc_vert_side(self):
        hor_side = 1
        alpha = 0
        self.assertEqual(round(calc_vert_side(hor_side, alpha), 5), 0)
        alpha = 45 * math.pi / 180
        self.assertEqual(round(calc_vert_side(hor_side, alpha), 5), 1)

    def test_calc_hypo(self):
        side = 1
        self.assertEqual(calc_hypo(side, side), math.sqrt(2))

    def test_opt_start_angle(self):
        side = 1
        n_same = 1
        self.assertEqual(round(find_opt_angle(side, side, 2 * side, n_same), 3), round(45 * math.pi / 180, 3))


if __name__ == '__main__':
    unittest.main()
