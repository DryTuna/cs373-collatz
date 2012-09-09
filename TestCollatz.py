#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2012
# Duy Tran
# -------------------------------

"""
To test the program:
    % python TestCollatz.py >& TestCollatz.py.out
    % chmod ugo+x TestCollatz.py
    % TestCollatz.py >& TestCollatz.py.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from Collatz import collatz_read, f, collatz_regular_eval, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        r = StringIO.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 10)

    def test_read_2 (self) :
        r = StringIO.StringIO("999999 1000000\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  999999)
        self.assert_(a[1] == 1000000)

    def test_read_3 (self) :
        r = StringIO.StringIO("2567 5678\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 2567)
        self.assert_(a[1] == 5678)

    # -
    # f
    # -

    def test_f_1 (self) :
        result = f(5)
        self.assert_(result == 8)

    def test_f_2 (self) :
        result = f(215)
        self.assert_(result == 323)

    def test_f_3 (self) :
        result = f(9999)
        self.assert_(result == 14999)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assert_(v == 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assert_(v == 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assert_(v == 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assert_(v == 174)

    def test_eval_5 (self) :
        v = collatz_eval(999998, 999999)
        self.assert_(v == 259)

    def test_eval_6 (self) :
        v = collatz_eval(1, 2)
        self.assert_(v == 2)

    # --------------------
    # collatz_regular_eval
    # --------------------

    def test_reg_eval_1 (self) :
        v = collatz_regular_eval(1, 10)
        self.assert_(v == 20)

    def test_reg_eval_2 (self) :
        v = collatz_regular_eval(100, 200)
        self.assert_(v == 125)

    def test_reg_eval_3 (self) :
        v = collatz_regular_eval(201, 210)
        self.assert_(v == 89)

    def test_reg_eval_4 (self) :
        v = collatz_regular_eval(900, 1000)
        self.assert_(v == 174)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 100, 200, 125)
        self.assert_(w.getvalue() == "100 200 125\n")

    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 201, 210, 89)
        self.assert_(w.getvalue() == "201 210 89\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("1 1\n1 999999\n999998 999999\n244796 493938\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n1 999999 525\n999998 999999 259\n244796 493938 449\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("542554 678807\n628487 879727\n374289 444328\n903801 926705\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "542554 678807 509\n628487 879727 525\n374289 444328 449\n903801 926705 476\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
