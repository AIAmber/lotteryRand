import random

# red = range(1, 36)
# blue = range(1, 13)

# print(red[1], "\n", blue)
redChoice = []
blueChoice = []
lotteryNums = []
i, j, k =0, 0, 0
# print(j)

# while k<5:
# 	while i<5:
# 		chooseRed = random.randint(1, 35)
# 		redChoice.append(chooseRed)
# 		i+=1

# 	while j<2:
# 		chooseBlue = random.randint(1, 12)
# 		blueChoice.append(chooseBlue)
# 		j+=1

# 	k+=1
# 	lotteryNum = str(redChoice + blueChoice)
# 	lotteryNums.append(lotteryNum)

# print(lotteryNums)

# ------------------------------

while i<5:
	chooseRed = random.randint(1, 35)
	redChoice.append(chooseRed)
	i+=1

while j<2:
	chooseBlue = random.randint(1, 12)
	blueChoice.append(chooseBlue)
	j+=1

redChoice.sort()
blueChoice.sort()
# print(redChoice)
lotteryNum = str(redChoice + blueChoice)
print(lotteryNum)