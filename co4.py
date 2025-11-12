start = int(input("enter the starting range: "))
end = int(input("enter the ending range: "))

even_digit_numbers = []
for num in range(start, end + 1):
    s = str(num)
    if all(int(digit) % 2 == 0 for digit in s):
        even_digit_numbers.append(num)

print("Four-digit numbers with all even digit: ")
print(even_digit_numbers)
