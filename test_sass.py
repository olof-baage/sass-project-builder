from sass_builder import validate_projectname, validate_path, has_folder_true_files
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
    assert validate_path("sub_folder/") == True
    assert validate_path("sub-folder/") == True
    assert validate_path("sub.folder/") == True



def test_has_folder_true_files():
    arr_pages =  [
            [ "_home.scss", False, False],
            [ "_contact.scss", False, False ] 
    ]
    arr_abstracts =  [
            [ "_variables.scss", True, True, "var" ],
            [ "_functions.scss", False, True, "func" ],
            [ "_mixins.scss", True, True, "mix" ],
            [ "_placeholders.scss", False, True, "plc" ] 
    ]    
    assert has_folder_true_files(arr_pages) == False
    assert has_folder_true_files(arr_abstracts) == True



    

    