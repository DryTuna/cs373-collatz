#!/usr/bin/env python

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2012
# Duy Tran
# ---------------------------

#------------
#Eager_Caches
#------------
"""
cycle_cache stores the max cycle length of every 10000 numbers
num_cache stores the corresponding number of the highest cycle length
"""

cycle_cache = [262, 279, 308, 324, 314, 340, 335, 351, 333, 333,
354, 349, 344, 344, 375, 383, 370, 347, 365, 360,
373, 386, 368, 443, 368, 363, 407, 407, 389, 371,
371, 384, 384, 366, 441, 379, 410, 423, 436, 405,
405, 449, 418, 400, 369, 387, 444, 382, 413, 426,
426, 470, 408, 377, 452, 421, 421, 390, 434, 403,
403, 447, 509, 416, 416, 429, 442, 385, 398, 442,
504, 411, 411, 424, 393, 424, 468, 437, 406, 468,
406, 450, 450, 525, 419, 419, 388, 432, 445, 370,
445, 476, 476, 507, 383, 414, 414, 458, 427, 396]

num_cache = [6171, 17647, 26623, 35655, 45127, 52527, 60975, 77031, 87087, 91463,
106239, 115547, 129991, 135111, 142587, 156159, 160411, 173321, 180463, 195465,
206847, 216367, 225023, 230631, 240617, 254911, 263103, 270271, 288489, 298843,
300030, 312318, 324551, 336199, 345947, 351359, 360361, 376603, 389191, 394655,
405407, 410011, 423679, 438699, 448265, 450651, 461262, 474121, 480481, 492571,
502137, 511935, 525543, 532715, 546681, 554143, 564905, 576978, 583787, 591983,
601327, 615017, 626331, 635519, 640641, 656761, 665215, 675969, 686985, 691894,
704623, 712683, 720722, 735679, 740306, 753206, 767903, 775035, 788315, 796095,
801769, 818943, 820022, 837799, 847358, 854191, 865401, 871915, 886953, 894623,
906175, 910107, 927003, 939497, 940257, 950943, 960962, 970599, 980905, 998969]



# ------------
# collatz_read
# ------------

def collatz_read (r, a) :
    """
    reads two ints into a[0] and a[1]
    r is a  reader
    a is an array of int
    return true if that succeeds, false otherwise
    """
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    a[0] = int(l[0])
    a[1] = int(l[1])
    assert a[0] > 0
    assert a[1] > 0
    return True

# ------------
# cycle_length
# ------------

def cycle_length (n) :
    """
    computing cycle length of integer n
    n must be greater than 0
    """
    assert n > 0
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n / 2)
            c += 1
        else :
            n += (n >> 1) + 1
            c += 2
    assert c > 0
    return c
    

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    this function attempts to use the cache before having to perform a cycle calculation
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    index_a points to the value in num_cache that is closest to i
    index_b points to the value in num_cache that is closest to j
    max_a is the highest cycle length between i and num_cache[index_a] inclusive
    max_b is the highest cycle length between num_cache[index_b] and j inclusive
    temp stores the current highest cycle length
    return the max cycle length
    """
    assert i > 0
    assert j > 0

    if(i > j):
        temp = j
        j = i
        i = temp    

    assert i <= j

    index_a = int(i/10000)
    index_b = int((j-1)/10000)

    if (index_a == index_b) :
        if (i > num_cache[index_a] or j < num_cache[index_a]) :
            return collatz_regular_eval (i, j)

    max_a = cycle_cache[index_a]
    max_b = cycle_cache[index_b]

    if (i > num_cache[index_a]) :
        index_a += 1
        max_a = collatz_regular_eval (i, index_a*10000 - 1)
    if (j < num_cache[index_b]) :
        max_b = collatz_regular_eval (10000*index_b, j)
    if (max_a < max_b) :
        max_a = max_b

    temp = 1
    for x in range(index_a, index_b):
        if(temp < cycle_cache[int(x)]):
            temp = cycle_cache[int(x)]

    if (temp < max_a) :
        temp = max_a
    
    return temp

# --------------------
# collatz_regular_eval
# --------------------

def collatz_regular_eval (i, j) :
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    return the max cycle length in the range [i, j]
    """
    assert i > 0
    assert j > 0
    v = 1

    if(i <= j/2):
        i = j/2 + 1

    for x in range(i, j+1) :
        curr_length = cycle_length(int(x))		    
        if(curr_length > v):
            v = curr_length
  
    assert v > 0
    return v
    

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    prints the values of i, j, and v
    w is a writer
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    v is the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    a = [0, 0]
    count = 1
    while collatz_read(r, a) :
        v = collatz_eval(a[0], a[1])
        collatz_print(w, a[0], a[1], v)
