import pytest

@pytest.fixture
def setup1():
    print("\nsetup 1")
    yield    # execute stuff after yield when the fixture goes out of scope
    print("\nteardown 1")

@pytest.fixture
def setup2(request):
    print("\nsetup 2")

    def teardown_a(): # these teardown functions get called by the addfinalizer method below, after the test function that calls it does its stuff
        print("\nteardown a")
    
    def teardown_b():
        print("\nteardown b")

    request.addfinalizer(teardown_a)
    request.addfinalizer(teardown_b)


def test1(setup1): # I can use test fixture setup 1 by passing it in here
    print("\nExecuting test 1")
    assert True

@pytest.mark.usefixtures("setup2") # I can also use a decorator to execute a testfixture
def test2():
    print ("\nExecuting test2")
    assert True


