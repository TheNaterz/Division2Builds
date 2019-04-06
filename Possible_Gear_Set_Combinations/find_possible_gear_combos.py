branded_sets = {
	"5.11": ["chest", "backpack", "gloves"],
	"airaldi": ["holster", "backpack", "gloves", "knees"],
	"alps": ["chest", "backpack", "gloves"],
	"badger": ["mask", "backpack", "gloves"],
	"china": ["mask", "gloves", "knees"],
	"douglas": ["mask", "holster", "knees"],
	"fenris": ["chest", "holster", "knees"],
	"gila": ["mask", "chest", "holster", "backpack", "gloves", "knees"],
	"murakami": ["mask", "chest", "holster", "backpack", "gloves", "knees"],
	"overlord": ["chest", "gloves", "knees"],
	"petrov": ["chest", "holster", "backpack"],
	"providence": ["mask", "chest", "holster", "backpack", "gloves", "knees"],
	"richter": ["mask", "holster", "backpack"],
	"sokolov": ["mask", "chest", "knees"],
	"wyvern": ["mask", "holster", "backpack", "knees"],
	"yaahl": ["mask", "chest", "gloves"]
}

sixes = []
five_ones = []
four_twos = []
four_one_ones = []
three_threes = []
three_two_ones = []
three_one_one_ones = []
two_two_twos = []
two_two_one_ones = []
two_one_one_one_ones = []
one_one_one_one_one_ones = []

gear = ["mask", "chest", "holster", "backpack", "gloves", "knees"]

possibles = {
	"mask": [],
	"chest": [],
	"holster": [],
	"backpack": [],
	"gloves": [],
	"knees": []
}

for g in gear:
	for k in branded_sets:
		if g in branded_sets[k]:
			possibles[g].append([k, g])

import itertools
all_combos = list(itertools.product(*possibles.values()))

for c in all_combos:
	bflag = False
	unique = set([z[0] for z in c])
	combo_count = []
	for u in unique:
		tmp = [z[0] for z in c]
		combo_count.append(tmp.count(u))

	combo_count.sort(reverse=True)
	if combo_count == [6]:
		sixes.append(c)
	elif combo_count == [5,1]:
		five_ones.append(c)
	elif combo_count == [4,2]:
		four_twos.append(c)
	elif combo_count == [4,1,1]:
		four_one_ones.append(c)
	elif combo_count == [3,3]:
		three_threes.append(c)
	elif combo_count == [3,2,1]:
		three_two_ones.append(c)
	elif combo_count == [3,1,1,1]:
		three_one_one_ones.append(c)
	elif combo_count == [2,2,2]:
		two_two_twos.append(c)
	elif combo_count == [2,2,1,1]:
		two_two_one_ones.append(c)
	elif combo_count == [2,1,1,1,1]:
		two_one_one_one_ones.append(c)
	elif combo_count == [1,1,1,1,1,1]:
		one_one_one_one_one_ones.append(c)

a = open('combo_gear_6.txt', 'w')
for c in sixes:
	a.write(str(c)+"\n")
a.close()

a = open('combo_gear_5_1.txt', 'w')
for c in five_ones:
	a.write(str(c)+"\n")
a.close()

a = open('combo_gear_4_2.txt', 'w')
for c in four_twos:
	a.write(str(c)+"\n")
a.close()

a = open('combo_gear_4_1_1.txt', 'w')
for c in four_one_ones:
	a.write(str(c)+"\n")
a.close()

a = open('combo_gear_3_3.txt', 'w')
for c in three_threes:
	a.write(str(c)+"\n")
a.close()

a = open('combo_gear_3_2_1.txt', 'w')
for c in three_two_ones:
	a.write(str(c)+"\n")
a.close()

a = open('combo_gear_3_1_1_1.txt', 'w')
for c in three_one_one_ones:
	a.write(str(c)+"\n")
a.close()

a = open('combo_gear_2_2_2.txt', 'w')
for c in two_two_twos:
	a.write(str(c)+"\n")
a.close()

a = open('combo_gear_2_2_1_1.txt', 'w')
for c in two_two_one_ones:
	a.write(str(c)+"\n")
a.close()

a = open('combo_gear_2_1_1_1_1.txt', 'w')
for c in two_one_one_one_ones:
	a.write(str(c)+"\n")
a.close()

a = open('combo_gear_1_1_1_1_1_1.txt', 'w')
for c in one_one_one_one_one_ones:
	a.write(str(c)+"\n")
a.close()
