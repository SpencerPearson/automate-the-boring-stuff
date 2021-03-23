# I have not come up with a proper solution for this problem yet.
# The answer should be close to 3.125%
# I am having trouble with only adding +1 to the number of streaks when a streak of six is discovered then moving on to the next round of 100 flips

import random
numberOfStreaks = 0
streak = 0
headsOrTails = []
for experimentNumber in range(10000):
    for coinFlips in range(100):
        headsOrTails.append(random.randint(0, 1))
    if str(headsOrTails).__contains__('0, 0, 0, 0, 0, 0') or str(headsOrTails).__contains__('1, 1, 1, 1, 1, 1'):
        numberOfStreaks += 1

    headsOrTails = []

print('Chance of streak: %s%%' % (numberOfStreaks / 10000))