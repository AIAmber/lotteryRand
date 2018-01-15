import random
import collections as coll

data = {"A":2, "B":2, "C":4, "D":6, "E":3, "F":1}

# 1st random
def list_method():
	all_data = []
	for v, w in data.items():
		temp = []
		for i in range(w):
			temp.append(v)
		all_data.extend(temp)

	n = random.randint(0, len(all_data)-1)
	return all_data[n]

# 2nd random
def iter_method():
	total = sum(data.values())
	rad = random.randint(1, total)

	cur_total = 0
	res = ""
	for k, v in data.items():
		cur_total += v
		if rad <= cur_total:
			res = k
			break
	return res

def test(method):
	dict_num = coll.defaultdict(int)
	for i in range(100):
		dict_num[eval(method)] += 1

	for i, j in dict_num.items():
		print(i, j)

if __name__ == '__main__':
	test("list_method()")
	print("-"*10)
	test("iter_method()")