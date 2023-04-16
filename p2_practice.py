string1 = "this is a string"
string2 = "this is another string"
# print(string1+string2)
length = len(string2)
string_upper_first_letter = string2.title()
# print(string_upper_first_letter)
string_lower_case = string_upper_first_letter.lower()
# print(string_lower_case)

d = "qwerty"
ch = d[3]
# print(ch)
chm = d[:]
# print(chm)

# d[4] = "f" <-- TypeError: 'str' object does not support item assignment

# ---------------- practice with digits -----------------------------

a = 5
b = 3

# print(int(a / b))
# print(a / b)
# print(a % b)
# print(a ** 2)

# param = 15 + string1 <-- TypeError: unsupported operand type(s) for +: 'int' and 'str'
param1 = "15" + string1
param2 = str(15) + string1

# n1 = input("Enter the first number: ")
# n2 = input("Enter the second number: ")
# n3 = float(n1)+float(n2)
# print(f" n1 plus n2 is { n3 } ")

# a_val = 1 / 3
# b_val = 2 / 9
# print("{:7.4f}".format(a_val))
# print("{:7.3f} {:7.3e}".format(a_val, b_val))

# n1 = input("Enter the first number: ")
# n2 = input("Enter the second number: ")
# n3 = float(n1)+float(n2)
# print(" n1 plus n2 is {0} ".format(n3))

# --------------------- practice with arrays ----------------------
list1 = [62, 65, 56, 74, 29, 56, 67]
# print(dir(list1))
# print(list1)
# list1.sort()
# print(list1)
# list1.sort(reverse=True)
# print(list1)

list2 = [3, 5, 67, 43, 87]
list2_sorted = sorted(list2)
# print(list2_sorted)

# --------------------- practice with tuples-------------------------
# print(dir(tuple))

seq = (3, 4, 6, 13, 1, 33, 21, 10, 33, 10, 18)
# print(seq.count(10))
# print(seq.index(0)) <-- ValueError: tuple.index(x): x not in tuple
# print(seq.index(10))  # <-- return first index of the value in tuple

list_seq = list(seq)
# print(list_seq)
# print(type(list_seq))
# print((type(seq)))

# -------------------- practice with dictionary -----------------

D = {"food": "Apple", "quantity": 3, "color": "Green"}
print(D["color"])

print(D["quantity"])
D["quantity"] += 5
print(D["quantity"])

dp = {}
# dp.__setitem__("name", "Sergey")
# print(dp)
# dp["age"] = 44
# print(dp)

# dp["name"] = input("Enter name ")
# dp["age"] = input("Enter age ")
# print(dp)

# -------------------- Data store ---------------------

rec = {"name": {"firstname": "Bob", "lastname": "Smith"}, "job": ["dev", "mgr"], "age": 25}
print(rec)
fullname = rec["name"]["firstname"]+" "+rec["name"]["lastname"]
print("Fullname: {0} {1}".format(rec["name"]["firstname"], rec["name"]["lastname"]))
jobs = rec["job"]
print("List of jobs: {0}".format(jobs))
jobs.append("janitor")
print("List of jobs: {0}".format(jobs))