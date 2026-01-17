from src.math_operation import add,sub


def test_add():
    assert add(0,2)==2
    assert add(0,-2)==-2

def test_sub():
    assert sub(0,2)==-2
    assert sub(4,-2)==6