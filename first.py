# Height of the tree (number of rows)
height = 6

# Outer loop: controls each row from top to bottom
for i in range(1, height + 1):
    #1,7 
    # (1) -----*
    # (2) ----***
    # (3) ---*****
    # (4) --*******
    # (5) -*********
    # (6) ***********
    
    # Inner loop 1: prints spaces for alignment
    for j in range(height - i):

        print(" ", end="")
        
    # Inner loop 2: prints stars to make the triangle
    for k in range(2 * i - 1):
        print("*", end="")
        
    # Move to the next line after finishing the row
    print()
