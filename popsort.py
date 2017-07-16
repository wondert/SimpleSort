"""The popsort module contains functions to recursively sort a sequence."""

# test sequences for validation of sorting
unsorted1 = [29, 15, 32, 1, 19, 72, 35, 7, 81]
unsorted2 = ['sixteen', 'one', 'eight', 'seven', 'five', 'twelve']


def recursivesort(sequence, slidingstart=0, switch=0):
    """Recursively sort a sequence to shift the higher value right.

    recursivesort takes three argument, and returns a tuple containing the
    sorted sequence with the highest value shifted to the right end and a
    flag, switch, which indicates if any value shifted during the function
    call.

    recursivesort(mutable sequence, int, int) -> mutated sequence, int

    :param sequence: container with elements to sort.
    :type sequence: mutable sequence; list or dict. must support .insert.
    :param slidingstart: (optional) index to start right shifting values.
    :type slidingstart: int, default = 0.
    :param switch: (optional) flag to indicate if function shifted a value.
    :type switch: int, default=0.
    """
    # return sequence once final two values compared
    if not (len(sequence) - slidingstart - 1):
        return sequence, switch

    # right shift larger value if it is to the left in the sequence
    elif sequence[slidingstart] > sequence[slidingstart+1]:
        sequence[slidingstart], sequence[slidingstart+1] = (
            sequence[slidingstart+1], sequence[slidingstart])
        switch = 1
        return recursivesort(sequence, slidingstart+1, switch)

    # recursive call to the next value in sequence
    else:
        return recursivesort(sequence, slidingstart+1, switch)


def popsort(randomseq, key=None, reverse=False):
    """Sort a sequence by shifting values in ascending order to the right.

    popsort takes three arguments, and returns sorted sequence with the
    items ordered in ascending value based on default type comparison.
    The sequence must be mutable. popsort uses two default arguments, a flag
    reverse to indicate if the return sequence should be in descending
    order, and a key function to modify the values to be sorted.

    popsort(sequence, int, int) -> sorted sequence, int

    :param sequence: container with elements to sort.
    :type sequence: mutable sequence; list or dict. must support .insert.
    :param key: (optional) function to modify the values to be sorted.
    :type key: function, default = None.
    :param reverse: (optional) flag to indicate if sorted sequence to be
    returned in reverse or descending order.
    :type reverse: boolean, default = False.
    """
    if key and reverse:
        memoized = {key(value):index for index, value in enumerate(randomseq)}
        keyedseq = [key(element) for element in randomseq]
        seq1 = keyedseq[:len(keyedseq)//2]
        seq2 = keyedseq[(len(keyedseq)//2):]
        # swap = 0
        switch1 = 0
        switch2 = 0
        # looper = 0
        while True:
            # print("This is loop {}".format(looper))
            # looper += 1
            if not switch1:
                seq1, switch1 = recursivesort(seq1)
                seq2, switch2 = recursivesort(seq2)
                # print("seq1: {}/nswitch1: {}/nseq2: {}/nswitch2:
                # {}".format(seq1, switch1, seq2, switch2))

            elif switch1:
                seq1, switch1 = recursivesort(seq1)
                seq2, switch2 = recursivesort(seq2)

            else:
                seq2, switch2 = recursivesort(seq2)
                # print("..seq2: {}/nswitch2: {}".format(seq2, switch2))

            if seq1[-1] > seq2[0]:
                seq2[0], seq1[-1] = seq1[-1], seq2[0]
                # swap = 1
                # print("swap!")

            # else:
                # swap = 0
                # remove refs to swap if no use case found

            if not (switch1 or switch2):
                break

        seq1 = [randomseq[memoized[element]] for element in seq1]
        seq2 = [randomseq[memoized[element]] for element in seq2]

    elif key and not reverse:
        memoized = {key(value):index for index, value in enumerate(randomseq)}
        keyedseq = [key(element) for element in randomseq]
        seq1 = keyedseq[:len(keyedseq)//2]
        seq2 = keyedseq[(len(keyedseq)//2):]
        # swap = 0
        switch1 = 0
        switch2 = 0
        # looper = 0
        while True:
            # print("This is loop {}".format(looper))
            # looper += 1
            if not switch1:
                seq1, switch1 = recursivesort(seq1)
                seq2, switch2 = recursivesort(seq2)
                # print("seq1: {}/nswitch1: {}/nseq2: {}/nswitch2:
                # {}".format(seq1, switch1, seq2, switch2))

            elif switch1:
                seq1, switch1 = recursivesort(seq1)
                seq2, switch2 = recursivesort(seq2)

            else:
                seq2, switch2 = recursivesort(seq2)
                # print("..seq2: {}/nswitch2: {}".format(seq2, switch2))

            if seq1[-1] > seq2[0]:
                seq2[0], seq1[-1] = seq1[-1], seq2[0]
                # swap = 1
                # print("swap!")

            # else:
                # swap = 0
                # remove refs to swap if no use case found

            if not (switch1 or switch2):
                break

        seq1 = [randomseq[memoized[element]] for element in seq1]
        seq2 = [randomseq[memoized[element]] for element in seq2]

    else:
        seq = [element for element in randomseq]
        seq1 = seq[:len(seq)//2]
        seq2 = seq[(len(seq)//2):]
        # swap = 0
        switch1 = 0
        switch2 = 0
        # looper = 0
        while True:
            # print("This is loop {}".format(looper))
            # looper += 1
            if not switch1:
                seq1, switch1 = recursivesort(seq1)
                seq2, switch2 = recursivesort(seq2)
                # print("seq1: {}/nswitch1: {}/nseq2: {}/nswitch2:
                # {}".format(seq1, switch1, seq2, switch2))

            elif switch1:
                seq1, switch1 = recursivesort(seq1)
                seq2, switch2 = recursivesort(seq2)

            else:
                seq2, switch2 = recursivesort(seq2)
                # print("..seq2: {}/nswitch2: {}".format(seq2, switch2))

            if seq1[-1] > seq2[0]:
                seq2[0], seq1[-1] = seq1[-1], seq2[0]
                # swap = 1
                # print("swap!")

            # else:
                # swap = 0
                # remove refs to swap if no use case found

            if not (switch1 or switch2):
                break

    if reverse:
        return (seq1+seq2).reverse()
    else:
        # print((seq1+seq2), "-- sort complete!!!")
        return seq1 + seq2
