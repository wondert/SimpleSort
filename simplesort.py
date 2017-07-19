unsorted1 = [29, 15, 32, 1, 19, 72, 35, 7, 81]
unsorted2 = ['sixteen', 'one', 'eightteen', 'seven', 'five', 'twelve']


def simplesort(randomseq, key=None, reverse=False):
	if key:
		seq = [key(element) for element in randomseq]
		count = len(seq)-1
		compares = 0
		while count != compares:
			compares = count
			for i in range(count):
				if seq[i] > seq[i+1]:
					seq[i], seq[i+1] = seq[i+1], seq[i]
					compares += 1

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

	if reverse:
		seq.reverse()

	return seq
