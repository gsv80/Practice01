# import math
#
# #         ------------------ task 01 ------------------------------
# #  ---------------------- all values are known -------------------------
# #
# # d1 = input("Enter the shortest distance from lifesaver to shore, in yards: ")
# # d2 = input("Enter the shortest distance from drowning person to shore, in feet: ")
# # h = input("Enter vertical way from lifesaver to drowning person, in yards: ")
# # v_sand = input("Enter lifesaver's velocity on foot, in miles per hour: ")
# # n = input("Enter lifesaver velocity fall shore/water, in times: ")
# # theta = input("Enter lifesaver's way angle, in grads: ")
#
# # theta_rad = float(theta) * math.pi / 180
# # d1_foot = float(d1) * 3
# # # print("d1 in feet:", d1_foot)
# # # print(math.tan(theta_rad))
# #
# # # way by foot
# # x = d1_foot * math.tan(float(theta_rad))
# # len1 = math.sqrt(d1_foot ** 2 + x ** 2)
# # print("Shortest way by shore", len1)
# #
# # # way by swim
# # h_foot = float(h) * 3
# # len2 = math.sqrt((h_foot - x) ** 2 + float(d2) ** 2)
# # print("Shortest way by swimming", len2)
# #
# # # lifesaver time
# # v_sand_feet_per_sec = float(v_sand) * 5280 / 3600
# # time = 1 / v_sand_feet_per_sec * (len1 + float(n) * len2)
# # print("Time in sec for all way to drowning person:{:5.1f} sec".format(time))
#
#
# #          --------------------- task 2 ------------------------------
# #              --------------- functions use ----------------
import math


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
theta = input_start_angle("lifesaver's way start")

print(d1, d2, h, v_sand, v_water, n, theta)


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
theta_rad = angle_to_rad(theta)


# function to calculate distance


def calc_vert_side(hor_side, alpha):
    vert_side = hor_side * math.tan(alpha)
    return vert_side


def calc_hypo(side_one, side_two):
    hypo = math.sqrt(side_one ** 2 + side_two ** 2)
    return hypo


h1_feet = calc_vert_side(d1_feet, theta_rad)
h2_feet = h_feet - h1_feet

length_shore = calc_hypo(d1_feet, h1_feet)
length_water = calc_hypo(d2_feet, h2_feet)


# ----- time calculation
def time_calc(distance, velocity):
    time = distance / velocity
    return time


time_shore = time_calc(length_shore, v_sand_feet_sec)
time_water = time_calc(length_water, v_water_feet_sec)

time_overall = time_shore + time_shore

print(time_overall, "sec")
