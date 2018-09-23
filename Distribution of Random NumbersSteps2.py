# NOTE: PROGRAM WILL GIVE TWO OUTPUT GRAPHS, KEEP IT RUNNING UNTIL BOTH APPEAR
'''
In ths code we have increase the loop duration to 250.
Hence, more the loop iterate through the model, the more accutate it would be.
'''

import matplotlib.pyplot as plt
import numpy as np
np.random.seed(123)
all_walks = []

# Simulate random walk 250 times
for i in range(250) :
    random_walk = [0]
    for x in range(10) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        # Implement clumsiness
        if np.random.rand() <= 0.001 :
            step = 0

        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)
plt.show()

##############################################################################

''' In the below code we want to know about the end points of all the random
walks that we have simulated. These end points have a certain distribution that
we can visulaize with a Histogram.

Note: Histagram is a kind of Plot.
'''

import matplotlib.pyplot as plt
import numpy as np
np.random.seed(123)
all_walks = []

# Simulate random walk 500 times
for i in range(500) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:    # We are selecing the range of dice numbers upto 2
            step = max(0, step - 1)
        elif dice <= 5:  # Here we have select the range of dice numbers upto 5
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1,:]      # Here we are selecting the last row

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()
