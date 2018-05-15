# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
# NOTE: Here we can use any world for 'rooms' and rooms don't need to be defined
# above in the code.

for rooms in areas:
    print(rooms)

print("\n")
##########################################################

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for index, area in enumerate(areas) :
    print("room " + str(index) + ": " + str(area))
    
print("\n")
##########################################################

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Adapt the printout
for index, area in enumerate(areas) :
    print("room " + str(index + 1) + ": " + str(area))
print("\n")
'''On adding +1 to the index, the count will start from 1 instead of 0 '''

#################################################################

# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch
for x in house :
    print("the " + str(x[0]) + " is " + str(x[1]) + " Square Meters")





    
