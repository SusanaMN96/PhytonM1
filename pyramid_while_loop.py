blocks = int(input("Enter the number of blocks: "))
used_blocks = blocks
height = 0
counter = 1

while counter <= blocks:
    used_blocks = used_blocks - counter
    if used_blocks >= 0:
        height += 1 
    else:
        break
    counter += 1

print("The height of the pyramid:", height)
