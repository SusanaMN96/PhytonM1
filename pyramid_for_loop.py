blocks = int(input("Enter the number of blocks: "))
used_blocks = blocks
height = 0

for i in range (1, blocks):
    used_blocks = used_blocks - i
    if used_blocks >= 0:
        height += 1 
    else:
        break

print("The height of the pyramid:", height)
