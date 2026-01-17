from src.math_operation import add,sub,multiply


def test_add():
    assert add(0,2)==2
    assert add(0,-2)==-2

def test_sub():
    assert sub(0,2)==-2
    assert sub(4,-2)==6

def test_multiply():
    assert multiply(0,2)==0
    assert multiply(4,-2)==-8