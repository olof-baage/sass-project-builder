from sass_builder import validate_projectname, validate_path
import pytest
import os

def test_validate_projectname():
    assert validate_projectname("helloWorld") == True
    assert validate_projectname("hello_World") == True
    assert validate_projectname("hello-world") == True
    assert validate_projectname("helloWorld_01") == True
    assert validate_projectname("helloWorld.01") == True
    assert validate_projectname("hello world") == False
    assert validate_projectname("hello&world") == False
    assert validate_projectname("he!llo?world") == False


def test_validate_path():
    assert validate_path("./subfolder/") == True
    assert validate_path("../subfolder/") == True
    assert validate_path(".../subfolder/") == False
    assert validate_path("subfolder/") == True
    assert validate_path(".././subfolder/") == False
    assert validate_path("././subfolder/") == False
    assert validate_path("././subfolder&something/") == False
    

    