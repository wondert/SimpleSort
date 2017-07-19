"""testsuite module unit testing for SimpleSort library."""

import simplesort as ss
import kindasimplesort as kss
import rightmemosort as rms
import popsort as ps
import dupsort as tps


print("simplesort function test. sequences must be fully sorted.")
print(ss.unsorted1)
sequence1 = ss.simplesort(ss.unsorted1)
print(sequence1, "\n")

print(ss.unsorted1)
sequence2 = ss.simplesort(ss.unsorted2)
print(sequence1, "\n")


print("kindasimplesort function test. sequences must be fully sorted.")
print(kss.unsorted1)
sequence3 = kss.simplesort(kss.unsorted1)
print(sequence3, "\n")

print(kss.unsorted2)
sequence4 = kss.simplesort(kss.unsorted2)
print(sequence4, "\n")

print(kss.unsorted2)
sequence5 = kss.simplesort(kss.unsorted2, key=len)
print(sequence5, "\n")


print("rmemosort function test. sequences must be fully sorted.")
print(rms.unsorted1)
sequence6 = rms.rmemosort(rms.unsorted1)
print(sequence6, "\n")

print(rms.unsorted2)
sequence7 = rms.rmemosort(rms.unsorted2)
print(sequence7, "\n")

print(rms.unsorted2)
sequence8 = rms.rmemosort(rms.unsorted2, key=len)
print(sequence8, "\n")

print(rms.unsorted2)
sequence9 = rms.rmemosort(rms.unsorted2, key=len, reverse=True)
print(sequence9, "\n")


print("recursivesort function test. single pass through a sequence")
print(ps.unsorted1)
sequence10 = ps.recursivesort(ps.unsorted1)
print(sequence10, "\n")

print("popsort function test. sequences must be fully sorted.")
print(ps.unsorted1)
sequence11 = ps.popsort(ps.unsorted1)
print(sequence11, "\n")

print(ps.unsorted2)
sequence12 = ps.popsort(ps.unsorted2)
print(sequence12, "\n")

print(ps.unsorted2)
sequence13 = ps.popsort(ps.unsorted2, key=len)
print(sequence13, "\n")

print(ps.unsorted2)
sequence14 = ps.popsort(ps.unsorted2, key=len, reverse=True)
print(sequence14, "\n")


print("recursivesort function test. single pass through a sequence")
print(tps.unsorted1)
sequence15 = tps.recursivesort(tps.unsorted1)
print(sequence15, "\n")

print("popsort function test. sequences must be fully sorted.")
print(tps.unsorted1)
sequence16 = tps.popsort(tps.unsorted1)
print(sequence16, "\n")

print(tps.unsorted2)
sequence17 = tps.popsort(tps.unsorted2)
print(sequence17, "\n")

print(tps.unsorted2)
sequence18 = tps.popsort(tps.unsorted2, key=len)
print(sequence18, "\n")

print(tps.unsorted2)
sequence19 = tps.popsort(tps.unsorted2, key=len, reverse=True)
print(sequence19, "\n")

print(tps.dupseq1)
sequence20 = tps.popsort(tps.dupseq1)
print(sequence20, "\n")

print(tps.dupseq1)
sequence21 = tps.popsort(tps.dupseq1, reverse=True)
print(sequence21, "\n")

print(tps.dupseq2)
sequence22 = tps.popsort(tps.dupseq2, key=len)
print(sequence22, "\n")

print(tps.dupseq2)
sequence23 = tps.popsort(tps.dupseq2, key=len, reverse=True)
print(sequence23, "\n")
