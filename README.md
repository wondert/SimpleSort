# SimpleSort

The SimpleSort library contains multiple sorting algorithms implemented with
iteration and recursion. These algorigthms can take an unordered sequence with
no duplicates, and sort them in ascending order or descending (reverse) order.
All algorithms in the SimpleSort library can also sort a sequence based on a
passed in key function.

The simplesort module can sort through a sequence by swapping values between
sequence indexings based on value comparisons. This is a simple scanning
sort and will not be highly performant over longer sequences.

The kindasimplesort module is identical to the simplesort module in basic
functionality, but is implemented as a dictionary sort. Since dictionaries
are not guaranteed to remained ordered after Python 3.6, this module may
become depricated/non-functional in the future.

The rightmemosort module can sort through a sequence with each cycle of
sorting being shorter than the previous (bubblesort algorithm). This will
significantly decrease the number of operations required to sort a sequence
and increase sorting performance over larger sequences.

The popsort module attempts to split the sorting into shorter segments and
with the bubblesort algorithm and a cross-sorting algorithm further reduce
the number of sorting cycles and operations required to sort.

The dupsort module is the only module that can sort unordered sequences with
duplicates and retain the duplicates original order in the unsorted sequence.


TODO - create a sorting algorithm that uses the mergesort algorithm.
TODO - create a sorting algorithm to insert an element to an already sorted
       sequence efficiently.
TODO - create a sorting algorithm to sort inplace while building the sorted
       sequence, basically a buildsort.
TODO - add docstrings to simplesort, kindasimplesort, and testsuite.
TODO - test algorithm performance in jupyter notebook.
