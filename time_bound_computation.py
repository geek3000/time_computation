# -*- coding: utf-8 -*-

import numpy as np
import time, pickle
import numba as nb

####### Pure Python

def add_python(n):
    start_time=time.time()
    A= np.random.rand(n,n)
    B= np.random.rand(n,n)
    AB=np.zeros((n, n))

    # iterate through rows
    for i in range(len(A)):
       # iterate through columns
       for j in range(len(A[0])):
           AB[i][j] = A[i][j] + B[i][j]
    
    end_time=time.time()
    return end_time-start_time


python_add={}

i=10

while i<=1000:
    python_add[i]=add_python(i)
    i+=10

pickle.dump(python_add, open("./data/python_add_time.data", "wb"))

####### numpy

def add_numpy(n):
    start_time=time.time()
    A= np.random.rand(n,n)
    B= np.random.rand(n,n)
    AB=np.add(A, B)
    end_time=time.time()
    return end_time-start_time

numpy_add={}
i=10
while i<=1000:
  print(i)
  numpy_add[i]=add_numpy(i)
  i+=10

print(numpy_add)
pickle.dump(numpy_add, open("./data/numpy_add_time.data", "wb"))

####### Numba

@nb.jit(nopython=True)
def add_python_nb(n):
    
    A= np.random.rand(n,n)
    B= np.random.rand(n,n)
    AB=np.zeros((n, n))

    # iterate through rows
    for i in range(len(A)):
       # iterate through columns
       for j in range(len(A[0])):
           AB[i][j] = A[i][j] + B[i][j]
    

python_add_nb={}

i=10

while i<=1000:
  print(i)
  start_time=time.time()
  add_python_nb(i)
  end_time=time.time()
  python_add_nb[i]=end_time-start_time
  i+=10

print(python_add_nb)
pickle.dump(python_add_nb, open("./data/python_nb_add_time.data", "wb"))

