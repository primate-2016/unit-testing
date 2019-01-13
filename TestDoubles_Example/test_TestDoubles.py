from mock import MagicMock
from pytest import raises
from LineReader import *



"""
Below is my first pass - I made this use a class for practice

***Also, I opened a real file rather than a mocked one, which is inappropriate for a unit test since this is dependency external to the test.
I should have used mock for the file as shown beneath this

def test_canCallReadfromFile():
    readFromFile()

def test_ReturnsCorrectString():
    f = readFromFile()
    fileContents = f.readFile('C:\\Users\\Richard\\Documents\\Python Notes\\unit-testing\\TestDoubles_Example\\testfile.txt')
    assert fileContents[0] == "This is the first line\n"

def test_ReturnsExceptioIfFileDoesNotExist():
    f = readFromFile()
    with raises(ValueError):
        fileContents = f.readFile('C:\\Users\\Richard\\Documents\\Python Notes\\unit-testing\\TestDoubles_Example\\doesntexist.txt')
    
"""



#def test_canCallReadfromFile(): # not needed anymore since the below validates a file can be opened. Also this would need mocking too once we've added the actual functionality to read a file to the readFromFile() function
#    readFromFile()

def test_returnsCorrectString(monkeypatch):
    mock_file = MagicMock() # set up an instance of the MagicMock class called mock_file to mock a file
    mock_file.readline = MagicMock(return_value="This is the first line\n") # make the readline builtin method return "This is the first line\n")
    mock_open = MagicMock(return_value=mock_file) # set up another instance of the MagicMock class called mock_open and set the return value to be the mock_file instance of the class
    monkeypatch.setattr("builtins.open", mock_open) # make the builtin file open function return the mock_open instance, which itself returns the mock_file
    result = readFromFile("fake_path_to_file")
    mock_open.assert_called_once_with("fake_path_to_file", "r") # since mock open replaces the file open function, we see how often it was called by a call to our readFromFile() function
    assert result == "This is the first line\n"
