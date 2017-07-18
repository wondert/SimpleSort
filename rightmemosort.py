"""The rightmemosort module contains functions to sort lists and dicts."""

unsorted1 = [29, 15, 32, 1, 19, 72, 35, 7, 81, 6, 14]
unsorted2 = ['sixteen', 'one', 'eighteen', 'seven', 'five', 'twelve']


def rmemosort(randomseq, key=None, reverse=False):
	"""Iteratively sort a sequence by shifting the higher values right.

rmemosort takes three arguments, a list or dict containing items to be sorted,
an optional key function to modify the values of each item in the list and sort
by the key function return values, and an optional flag reverse which indicates
if the sorted sequence should be returned in descending order. By default,
rmemosort returns a list containing the sorted sequence in ascending order.

rmemosort implements a rudimentary bubblesort algorithm to account for each
full sort iteration moving the highest value to the end. The result being that
the final index is sorted and no longer needs to be considered in future sorts.

rmemosort(mutable sequence, function, boolean) -> sorted sequence

:param randomseq: container with elements to sort.
:type randomseq: mutable sequence; list or dict. must support slicing/insert.
:param key: (optional) function to modify elements of list to custom sort.
:type key: function, default = None.
:param reverse: (optional) flag to indicate if the return sequence is in
descending order.
:type reverse: boolean, default=False.
"""
	# loop = 0
	if key:
		# create dict to hold original index:value relationship
		memoized = {key(element):index
									for index, element in enumerate(randomseq)}
		# create sequence with values modified by key function
		seq = [key(element) for element in randomseq]

		# set length as constant value, decr to ensure index starts in range
		max = len(seq)
		decr = 1

		# create global counter to track if any elements were sorted each loop
		compares = 0

		# loop through sequence and sort, with each loop progressively smaller
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
		# create sequence sorted by key where memoized is used to remap key
		# values to the original value in the sequence
		seq = [randomseq[memoized[element]] for element in seq]

	else:
		# create a copy of the original sequence
		seq = [element for element in randomseq]

		# set length as constant value, decr to ensure index starts in range
		max = len(seq)
		decr = 1

		# create global counter to track if any elements were sorted each loop
		compares = 0

		# loop through sequence and sort, with each loop progressively smaller
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
		seq.reverse()
		return seq
	else:
		return seq
