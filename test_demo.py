import pytest

@pytest.mark.foo
@pytest.mark.bar
def test_one():
    print('im passing')
    pass


@pytest.mark.foo
@pytest.mark.failing
def test_two():
    """
    fist doc line

    after doc empty line
    dome new description line
    lorem :)
    """
    print('im failing')
    assert False
