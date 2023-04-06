import math

#         ------------------ task 01 ------------------------------
#  ---------------------- all values are known -------------------------
#
d1 = input("Enter the shortest distance from lifesaver to shore, in yards: ")
d2 = input("Enter the shortest distance from drowning person to shore, in feet: ")
h = input("Enter vertical way from lifesaver to drowning person, in yards: ")
v_sand = input("Enter lifesaver's velocity on foot, in miles per hour: ")
n = input("Enter lifesaver velocity fall shore/water, in times: ")
theta = input("Enter lifesaver's way angle, in grads: ")

theta_rad = float(theta) * math.pi / 180
d1_foot = float(d1) * 3
# print("d1 in feet:", d1_foot)
# print(math.tan(theta_rad))

# way by foot
x = d1_foot * math.tan(float(theta_rad))
len1 = math.sqrt(d1_foot ** 2 + x ** 2)
print("Shortest way by shore", len1)

# way by swim
h_foot = float(h) * 3
len2 = math.sqrt((h_foot - x) ** 2 + float(d2) ** 2)
print("Shortest way by swimming", len2)

# lifesaver time
v_sand_feet_per_sec = float(v_sand) * 5280 / 3600
time = 1 / v_sand_feet_per_sec * (len1 + float(n) * len2)
print("Time in sec for all way to drowning person:{:5.1f} sec".format(time))
