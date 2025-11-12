l1 = list(map(int, input("Enter numbers for the first list: ").split()))
l2 = list(map(int, input("Enter numbers for the second list: ").split()))

s1 = len(11) == len(12)
ss = len(11) == sum(12)
cv = set(11) & set(12)

print("Same length:", s1)
print("Same sum:", ss)
print("Common values:", cv)
