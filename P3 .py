
# Emmanuel Cruz 

# Oct 22, 2024

# This program will iterate over the numbers from 1 to 50.


for number in range (1,51):
   if number % 3 == 0 and number % 5 == 0:
       print ("Divisible by both")
   elif number % 3 == 0:
       print ("Divisible by three")
   elif number % 5 == 0:
       print ("Divisible by five")
   else:
       print (number)
