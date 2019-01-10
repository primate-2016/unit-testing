import pytest

@pytest.fixture(scope="session", autouse=True) # session scope means this will get executed once when pytest starts, no matter how many modules (python files) are executed
def setupSession():
    print("\nfixture to setup pytest session")

@pytest.fixture(scope="module", autouse=True) # this will get executed everytime this module (python file) is executed
def setupModule():
    print("\nfixture bound to the scope of this module/file")

@pytest.fixture(scope="class", autouse=True) # this will get executed everytime a test class is initialised (since autouse is true)
def setupClass():
    print ("\nfixture bound to the scope of classes")

@pytest.fixture(scope="function", autouse=True) # this will get executed everytime a test function is called
def setupFunction():
    print ("\nfixture bound to the scope of functions")


def testFunction1():
    print ("\nexecuting Function1")

class TestClass:
    def test_it1(self):
        print("\nexecuting function 1 in TestClass")

    def test_it2(self):
        print("\nexecuting function 2 in TestClass")
