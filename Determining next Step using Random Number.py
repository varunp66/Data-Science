''' Imagine if we throw a dice 100 times to determine our next step
# In the below example we are throwing coin with Heads = 0 and Tails = 1

import numpy as np
np.random.seed(123)
outcomes = []
for x in range(10):         # We are playing the game here 10 times.
    coin = np.random.randint(0,2)
    if coin == 0:
        outcomes.append("heads")
    else:
        ourcomes.append("tails")
print(outcomes)

'''

# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Initialize random_walk
random_walk = [0]

# Complete the ___
for x in range(100) :
    # Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)


'''
How low can you go?

Things are shaping up nicely! You already have code that calculates
your location in the Empire State Building after 100 dice throws.
However, there's something we haven't thought about - you can't go below 0!

A typical way to solve problems like this is by using max().
If you pass max() two arguments, the biggest one gets returned.
For example, to make sure that a variable x never goes below 10
when you decrease it, you can use:

Here we have to use : step = max(0, step - 1)
Instead of  step = step - 1(In previous code.

'''

# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Initialize random_walk
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        # Replace below: use max to make sure step can't go below 0
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

print(random_walk)

############################################################################

'''
The below code the Plot the outpot of the previous codes in the Graph
'''

# Initialization
import numpy as np

np.random.seed(123)
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)

# Show the plot
plt.show()


