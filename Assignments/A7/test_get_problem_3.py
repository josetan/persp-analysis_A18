import pytest
import get_problem_3 as gp3

def test_operate():
	assert gp3.operate(2, 5, '+') == 7
	assert gp3.operate(5, 5, '-') == 0
	assert gp3.operate(2, 3, '*') == 6
	assert gp3.operate(6, 2, '/') == 3
	with pytest.raises(ZeroDivisionError) as excinfo: 
		gp3.operate(6, 0, '/')
	assert excinfo.value.args[0] == "division by zero is undefined"
	with pytest.raises(ValueError) as excinfo:
		gp3.operate(2, 3, 'g') 
	assert excinfo.value.args[0] == "oper must be one of '+', '/', '-', or '*'"
	with pytest.raises(TypeError) as excinfo: 
		gp3.operate(2, 3, 4)
	assert excinfo.value.args[0] == "oper must be a string"