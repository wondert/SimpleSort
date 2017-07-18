unsorted1 = [29, 15, 32, 1, 19, 72, 35, 7, 81]
unsorted2 = ['sixteen', 'one', 'eighteen', 'seven', 'five', 'twelve']


def simplesort(randomseq, key=None, reverse=False):
	if key and reverse:
		seq = {index:[key(element), element] for index, element in enumerate(randomseq)}
		count = len(seq)-1
		compares = 0
		while count != compares:
			compares = count
			for i in range(count):
				if seq[i][0] > seq[i+1][0]:
					seq[i], seq[i+1] = seq[i+1], seq[i]
					compares += 1
		seq = [seq[i][1] for i in range(len(randomseq))]

	elif key and not reverse:
		seq = {index:[key(element), element] for index, element in enumerate(randomseq)}
		count = len(seq)-1
		compares = 0
		while count != compares:
			compares = count
			for i in range(count):
				if seq[i][0] > seq[i+1][0]:
					seq[i], seq[i+1] = seq[i+1], seq[i]
					compares -= 1
		seq = [seq[i][1] for i in range(len(randomseq))]

	else:
		seq = {index:element for index, element in enumerate(randomseq)}
		count = len(seq)-1
		compares = 0
		while count != compares:
			compares = count
			for i in range(count):
				if seq[i] > seq[i+1]:
					seq[i], seq[i+1] = seq[i+1], seq[i]
					compares -= 1
		seq = [seq[i] for i in range(len(seq.keys()))]

	if reverse:
		return seq.reverse()
	else:
		return seq
