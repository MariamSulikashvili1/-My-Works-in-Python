#Rearrange an array 
x = 5 
arr = {1,2,3,4,5,6,19,27} 
 for i in arr: 
 print (i)
 
# Recursive function
def recursive_fibonacci(n):
  if n <= 1:
      return n
  else:
      return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))
 
n_terms = 10
 
if n_terms <= 0:
  print("Invalid input ! Please input a positive value")
else:
  print("Fibonacci series:")
for i in range(n_terms):
    print(recursive_fibonacci(i))
    
    # list of numbers
list1 = [10, 20, 4, 45, 99]
 
# sorting the list
list1.sort()
 
# printing the last element
print("Largest element is:", list1[-1])