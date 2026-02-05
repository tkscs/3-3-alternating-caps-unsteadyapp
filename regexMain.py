import re
def alt_caps(original_string,regularExpression):
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
    # YOUR CODE HERE
    return new_string
print(re.findall("(.).","hello"))
print(re.sub("(.).",r"\1.upper()"))
print(re.findall(".(.)","hello"))
print(alt_caps("Alternating Capitalization",""))
