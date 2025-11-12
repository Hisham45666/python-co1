list1 = input("enter colors for list 1(comma separated): ").split(",")
list2 = input("enter colors for list 2(comma separated): ").split(",")


difference = [c for c in list1 if c not in list2]
print("colors in list 1 in list 2:", difference)
