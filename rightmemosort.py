unsorted1 = [29, 15, 32, 1, 19, 72, 35, 7, 81, 6, 14]
unsorted2 = ['sixteen', 'one', 'eight', 'seven', 'five', 'twelve']


def rmemosort(randomseq, key=None, reverse=False):
	# loop = 0
	if key and reverse:
		memoized = {key(element):index for index, element in enumerate(randomseq)}
		seq = [key(element) for element in randomseq]
		max = len(seq)
		decr = 1
		compares = 0
		while (max):
			# print("{}: ".format(compares), seq)
			for i in range(max-decr):
				if seq[i] > seq[i+1]:
					compares += 1
					seq[i], seq[i+1] = seq[i+1], seq[i]
					# print("{}: ".format(compares), seq)
				# else:
					# print('.')
			max -= 1
			# print("At loop {} we have performed
			# {} comparisons".format(loop, compares))
			# loop += 1
			if (compares < 2):
				# print('BREAK!!!')
				break
			else:
				compares = 0
		seq = [randomseq[memoized[element]] for element in seq]

	elif key and not reverse:
		memoized = {key(element):index for index, element in enumerate(randomseq)}
		seq = [key(element) for element in randomseq]
		max = len(seq)
		decr = 1
		compares = 0
		while (max):
			# print("{}: ".format(compares), seq)
			for i in range(max-decr):
				if seq[i] > seq[i+1]:
					compares += 1
					seq[i], seq[i+1] = seq[i+1], seq[i]
					# print("{}: ".format(compares), seq)
				# else:
					# print('.')
			max -= 1
			# print("At loop {} we have performed
			# {} comparisons".format(loop, compares))
			# loop += 1
			if (compares < 2):
				# print('BREAK!!!')
				break
			else:
				compares = 0
		seq = [randomseq[memoized[element]] for element in seq]

	else:
		seq = [element for element in randomseq]
		max = len(seq)
		decr = 1
		compares = 0
		while (max):
			# print("{}: ".format(compares), seq)
			for i in range(max-decr):
				if seq[i] > seq[i+1]:
					compares += 1
					seq[i], seq[i+1] = seq[i+1], seq[i]
					# print("{}: ".format(compares), seq)
				# else:
					# print('.')
			max -= 1
			# print("At loop {} we have performed
			# {} comparisons".format(loop, compares))
			# loop += 1
			if (compares < 2):
				# print('BREAK!!!')
				break
			else:
				compares = 0

	if reverse:
		return seq.reverse()
	else:
		return seq
