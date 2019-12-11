import pytest
from travel_bot_functions import * 
import sys, io

#test functions from A3
def test_remove_punctuation():
    #test funtion for remove puntuation function
    assert callable(remove_punctuation)
    assert isinstance(remove_punctuation(['hello,world']), str)
    assert remove_punctuation(prepare_text(test_string)) == 'startbot'
    
def test_string_concatenator():
    #test function for string concatenator funtion
    assert callable(string_concatenator)
    assert isinstance(string_concatenator('start', 'bot', '!'), str)
    assert string_concatenator('start', 'bot', '!') == test_string

def test_list_to_string():
    #test function for list to string function
    assert callable(list_to_string)
    assert isinstance(list_to_string(['hello world'],' '), str)
    assert list_to_string(['hello world'], ' ') == 'hello world'
    
def test_prepare_text():
    #test function for prepare text function
    assert callable(prepare_text)
    assert isinstance(prepare_text(test_string), list)
    assert prepare_text(test_string) == ['startbot']
    
def test_end_chat():
    #Tests end_chat function in few cases
    assert end_chat(compare_list) == False
    assert isinstance(end_chat(compare_list),bool)
    assert callable(end_chat)
    
#original tests created for travel_bot functions
def test_korea():

    # redirect sys.stdout to a buffer
    stdout = sys.stdout
    sys.stdout = io.StringIO()
    find_topic('korea')

    # get output and restore sys.stdout
    captured = sys.stdout.getvalue()
    sys.stdout = stdout
    expected_answer = response_dict['korea'][0] + '\n' + "Some foods to try here are: " + food_dict['korea'] + '\n' + "What other location do you want to hear more about?" + '\n'
    assert captured == expected_answer, "Expected answer is not the same as the actual answer"

test_korea()
    
def test_travel_bot(self):
        # Override the Python built-in input method 
        module.input = lambda: 'some_input'
        # Call the travel_bot function (which uses input)
        output = travel_bot()  
        assert output == 'expected_output'