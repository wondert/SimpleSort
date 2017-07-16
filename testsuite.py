"""testsuite module unit testing for SimpleSort library."""

# import simplesort as ss
#
# sequence1 = ss.simplesort(ss.unsorted1)
# sequence2 = ss.simplesort(ss.unsorted2)
#
# print(ss.unsorted1)
# print(sequence1)
#
# print(ss.unsorted1)
# print(sequence1)


# import kindasimplesort as kss
#
# sequence1 = kss.simplesort(kss.unsorted1)
# sequence2 = kss.simplesort(kss.unsorted2)
# sequence3 = kss.simplesort(kss.unsorted2, key=len)
#
# print(kss.unsorted1)
# print(sequence1)
#
# print(kss.unsorted2)
# print(sequence2)
#
# print(kss.unsorted2)
# print(sequence3)


# import rightmemosort as rms
#
# sequence1 = rms.rmemosort(rms.unsorted1)
# print(rms.unsorted1)
# print(sequence1)
#
# sequence2 = rms.rmemosort(rms.unsorted2)
# print(rms.unsorted2)
# print(sequence2)
#
# sequence3 = rms.rmemosort(rms.unsorted2, key=len)
# print(rms.unsorted2)
# print(sequence3)


import popsort as ps

# print(ps.unsorted1)
# sequence0 = ps.recursivesort(ps.unsorted1)
# print(sequence0)
#
# print(ps.unsorted1)
# sequence1 = ps.popsort(ps.unsorted1)
# print(sequence1)
#
# print(ps.unsorted2)
# sequence2 = ps.popsort(ps.unsorted2)
# print(sequence2)
#
sequence3 = ps.popsort(ps.unsorted2, key=len)
print(ps.unsorted2)
print(sequence3)
