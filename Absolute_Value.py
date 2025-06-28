num = int(input("Please enter a number:"))

if(num < 0):
    print(abs(num))

else:
    print(num)    

# Easier way 
print(abs(num) if num<0 else num)    