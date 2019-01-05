import pytest

@pytest.fixture(params=[1,25,56])
def setup(request):
    retVal = request.param # the param value passed into the function by the .fixture decorator
    print("\nsetup function returning retVal of {}".format(retVal))
    return retVal # this setup fixture returns the value passed in from params to a test function, once for each execution of that test function

def test1(setup):
    print("\nvalue received from setup fixture = {}".format(setup))
    assert True