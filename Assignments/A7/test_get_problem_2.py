import get_problem_2 as gp2

def test_month_length1():
	assert gp2.month_length("September") == 30, "expect 30" 	

def test_month_length2():
	assert gp2.month_length("January") == 31, "expect 31"

def test_month_length3():
	assert gp2.month_length("February") == 28, "expect 28"

def test_month_length4():
	assert gp2.month_length("February", leap_year=True) == 29, "expect 29" 

def test_month_length5():
	assert gp2.month_length(1) == None 
	