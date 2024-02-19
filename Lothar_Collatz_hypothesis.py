c0 = int(input("Enter a natural number: "))
steps = 0

while True:
    if c0%2 == 0:
        c0 //= 2
    else:
        c0 = c0*3 + 1
        
    steps += 1   
    
    print(c0)
    
    if c0 == 1:
        break

print("steps:",steps)
