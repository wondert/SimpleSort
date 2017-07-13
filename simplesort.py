unsorted1 = [29, 15, 32, 1, 19, 72, 35, 7, 81]
unsorted2 = ['sixteen', 'one', 'eight', 'seven', 'five', 'twelve']


def simplesort(randomseq, key=None, reverse=False):
	if key and reverse:
		seq = [key(element) for element in randomseq]
		count = len(seq)-1
		compares = 0
		while count != compares:
			compares = count
			for i in range(count):
				if seq[i] > seq[i+1]:
					seq[i], seq[i+1] = seq[i+1], seq[i]
					compares += 1

	elif key and not reverse:
		seq = [key(element) for element in randomseq]
		count = len(seq)-1
		compares = 0
		while count != compares:
			compares = count
			for i in range(count):
				if seq[i] > seq[i+1]:
					seq[i], seq[i+1] = seq[i+1], seq[i]
					compares -= 1

	else:
		seq = [element for element in randomseq]
		count = len(seq)-1
		compares = 0
		while count != compares:
			compares = count
			for i in range(count):
				if seq[i] > seq[i+1]:
					seq[i], seq[i+1] = seq[i+1], seq[i]
					compares -= 1

	return seq
