#Loop control statements
# 1.break
#stops the loop immediately

for i in range(1,6):
    if i==3:
        break
    print(i)
    
 #continue
 #skips current iteration
    
for i in range(1,6):
    if i==3:
        continue
    print(i)
    
    
    #3.pass
    #does nothing(placeholder)
for i in range(5):
    pass

#Task 1
#print 1 to 5 using for loop
for i in range (1,11):
    print(i)
    
#Task 2
# print 1 to 20 using for loop
for i in range(1,21):
   if i% 2 == 0:
       print(i)

# for i in range(2,21,2):
   print(i)

# Task 3
# print the odd number from 1 to 15
for i in range(1,16,2):
    print(i)

# Task 4
#  print each charactor from the string 
# Task 4  print each charector from the string
 text = 'python'
for char in text:
   print(char)

#  Task 5 
# print all the items in the list
 data = ["Data", "Science","AI"]
 for items in data:
     print(items)

#Task 6
#find the sum of numbers from 1 to 10
 total = 0
 for i in range(1,11):
 total += i
 print("Sum:",total)

#Task 7
#print multiplication table foe 5
for i in range(1,11):
 print("5 x",i, "=",5 * i)

#Task 8
#count the how many vowels is string
 text = "Hello World"
 count = 0
 for char in text:
  if char.lower() in "aeiou":
   count += 1