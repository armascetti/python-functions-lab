# Challenge 1 
#Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

def sum_to(num):
  sum = 0 
  for n in range(1, num +1):
    sum += n
  return sum 


#Challenge 2 
#Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

num = [40, 3, 20, 106, 99, 30]

max_value = max(num)
print("The largest number is:", max_value)


#Challenge 3 
#Write a function named occurances that takes two string arguments as input and counts the number of occurances of the second string inside the first string.

# str1= 'the dog is big'
# str2= 'is'

# count = str1.count(str2)
# print("The number of occurances is:", count)

def occurances(str1, str2):
  return str1.count(str2)


# Challenge 4 
#Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product. HINT: Review your notes on args.

