''' It is used to generate Random Numbers, we can simulate/generate the process
thousand of times and can see which simulations can give the best result.

In the form of code we can writh it as

import numpy as np
np.random.seed(123)
coin = np.random.randint(0,2)
print(coin)

The 'Seed' is used the generate the random numbers. If we assign
some value to 'seed' then it will generate the same random numbers
everytime we execute the code.'''
## Prints single random Numbers
# Import numpy as np
import numpy as np

# Set the seed
np.random.seed(123)

# Generate and print random float
print(np.random.rand())

###########################################################

#Prints mulitple random Numbers
# Import numpy as np
import numpy as np

# Set the seed
np.random.seed(123)

# Generate and print random float
dice = np.random.rand(1,10)
print(dice)

##########################################################

### Printing Random Numbers twice using the same Values

# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Use randint() to simulate a dice
dice = np.random.randint(1,7)
print(dice)

# Use randint() again
dice = np.random.randint(1,7)
print(dice)

#########################################################
'''
Determine your next move

In the Empire State Building bet, your next move depends on the
number of eyes you throw with the dice.
We can perfectly code this with an if-elif-else construct!

The sample code assumes that you're currently at step 50.
Can you fill in the missing pieces to finish the script?
'''

# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice <= 5 :

