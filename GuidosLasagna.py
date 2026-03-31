"""Functions used in preparing Guido's gorgeous lasagna.
 
Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum
 
This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""
#TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.
 
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
 
    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    remain_time = EXPECTED_BAKE_TIME - elapsed_bake_time
    return remain_time
#TODO: Define the 'preparation_time_in_minutes()' function below.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.
 
    :param number_of_layers: int - number of layers.
    :return: int - total preparation time of all the layers.
 
    Function that takes the number of layers and returns how much time it will take to prepare all the layers.
    """
    time_layer = number_of_layers * 2
    return time_layer
#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time in minutes.
 
    :param number_of_layers: int - the number of layers added to the lasagna.
    :param elapsed_bake_time: int - the number of minutes the lasagna has been baking in the oven.
    :return: int - remaining bake time (in minutes).
 
    Function that returns the total number of minutes you've been cooking, or the sum of your preparation 
    time and the time the lasagna has already spent baking in the oven
    """
    time_spent = elapsed_bake_time + (number_of_layers * 2)
    return time_spent
# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)