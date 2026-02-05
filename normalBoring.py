import re
import string
def alt_caps(original_string):
    """Convert a string to Alternating Caps

    Args:
        original_string (str): A given string with any kind of capitalization
    Returns:
        str: A new string with alternating capitalization
    Examples:
        >>> print(alt_caps("Alternating Capitalization"))
        aLtErNaTiNg CaPiTaLiZaTiOn
    """
    new_string = ""
    alternate = 0
    for i in original_string:
        new_string += ((alternate%2) * i.upper()) + ((not(alternate%2)) * i.lower()) 
        alternate +=1
    # YOUR CODE HERE

    return new_string
print(re.findall("(.).","hello"))
print(alt_caps("Alternating Capitalization"))