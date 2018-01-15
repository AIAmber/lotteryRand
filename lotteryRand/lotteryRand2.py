import random
import time

def chooseLotter():
	redRange = range(1, 36)
	blueRande = range(1, 13)

	redChoise = random.sample(redRange, 5)
	blueChoise = random.sample(blueRande, 2)

	redChoise.sort()
	blueChoise.sort()

	lotteyNum = str(redChoise + blueChoise)

	return lotteyNum

lotteyNums = []
i = 0
while i<5:
	lotteyNums.append(chooseLotter())
	time.sleep(0.1)
	i+=1

print(lotteyNums)