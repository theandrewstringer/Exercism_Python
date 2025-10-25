def response(hey_bob):
    """
    Determine what Bob will say when given an input.
    """
    
   # remove leading/trailing whitespace to standardize the string 
    stripped_input = hey_bob.strip()

    # check if the input is empty or only contains whitespace
    if not stripped_input:
        return "Fine. Be that way!"

    # create variables for questions and yelling
    is_question = stripped_input.endswith('?')
    is_yelling = stripped_input.isupper()
    
    # determine if it's yelling and a question
    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    
    # determine if it's a question
    elif is_question:
        return "Sure."
    
    # determine if it's yelling
    elif is_yelling:
        return "Whoa, chill out!"
        
    # for anything else
    else:
        return "Whatever."
