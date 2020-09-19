
def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)

# print(bunnyEars(0))
# print(bunnyEars(1))
# print(bunnyEars(11))
# print(bunnyEars(100))
# print(bunnyEars(1000))

# has recursion
# when you hit 1000 bunnies the program stops working properly

def find_sum(n):
    sum = 0
    for i in range(n):
        j = 1
        while j < n:
            j *= 2
            sum += 1
    return sum

print(find_sum(0))
print(find_sum(1))
print(find_sum(2))
print(find_sum(10))
print(find_sum(100))
print(find_sum(1000))
print(find_sum(10000))