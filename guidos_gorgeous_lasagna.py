EXPECTED_BAKE_TIME = 40 #40 minutes is the norm
PREPARATION_TIME = 2 #2 minutes per layer

def bake_time_remaining(elapsed_bake_time):
    """
    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    :param elapsed_bake_time: int - represents the bake time that has passed in minutes.
    :return: int - the expected bake time minus the elapsed bake time.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """
    Function that takes the number of layers and multiplies that by the amount of time each layer 
    takes.
    :param number_of_layers: int - the number of layers.
    :return: int - the number of layers multiplied by the amount of time each layer takes to 
    prepare.
    """
    return number_of_layers * PREPARATION_TIME
    
def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):
    """
    Function that takes the total preparation time and adds that to the elapsed bake time to find 
    out how much time the total cook time has taken.
    :param number_of_layers: int - the number of layers.
    :param elapsed_bake_time: int - represents the bake time that has passed in minutes.
    :return: int - how much time as elapsed, including the preparation and elapsed bake time.
    """
    total_cook_time = number_of_layers * PREPARATION_TIME + elapsed_bake_time
    return total_cook_time
