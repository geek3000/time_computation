# time_computation

![Graph](https://github.com/geek3000/time_computation/blob/master/graph.png)

in blue Pure python
In green numba module
and the last one is numpy

## Explanation

The graph show us that numpy and git are so fast than python loop

### Firstly
Is because, numpy is written in C (A low level language) or looping over lists in Python is slow because the language itself is dynamically typed. This means that you do not have to specify a variables data type but every time Python uses a variable it has to check data type. Even though Python is also written in C, this bookkeeping makes it much slower than other low-level languages.

### secondly,

Operations in Numpy are much faster because they take advantage of parallelism (which is the case of Single Instruction Multiple Data (SIMD)), while traditional for loop can't make use of it.
