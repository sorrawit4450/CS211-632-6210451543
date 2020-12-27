a = float(input("Minutes before due: "))
b = float(input("Temperature: "))
c = input("Is it raining (y/n)? ")
x1 = a/1440 
x2 = (a/1440)+1
if a%1440 >= 720 :
    print(">>> %d days before due." %x2)
else:
    print(">>> %d days before due." %x1)
if a <= 2160:
    print(">>> I will do the assignment.")   
elif a >= 7920:
    print(">>> I will not do the assignment.")     
elif (b >= 40) or ((c == "Y" or c =="y") and b >= 25): 
    print(">>> I will not do the assignment.") 
else:
    print(">>> I will do the assignment.") 