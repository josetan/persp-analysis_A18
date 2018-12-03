import get_problem_1 as gp1

def test_smallest_factor1():
	assert gp1.smallest_factor(1) == 1

def test_smallest_factor2():
	assert gp1.smallest_factor(2) == 2

def test_smallest_factor3():
	assert gp1.smallest_factor(3) == 3

def test_smallest_factor4():
	assert gp1.smallest_factor(4) == 2

def test_smallest_factor5():
	assert gp1.smallest_factor(5.7) == None, "expect None"

def test_smallest_factor6():
	assert gp1.smallest_factor(0) == None, "expect None"