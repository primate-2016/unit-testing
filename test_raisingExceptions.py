from pytest import raises

def raisesValueException():
    pass
    raise ValueError # comment this out to cause the unit test below to fail because this will no longer raise an exception of ValueError type

def test_exception():
    with raises(ValueError):
        raisesValueException()