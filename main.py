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
    new_string = re.sub(regularExpression,replaceFirst,original_string.lower()+"~")
    if(new_string[-1] == "~"):
        new_string = new_string[:-1]
    return new_string
def replaceFirst(match):
    new = ""
    for i in match.groups():
        try:
            if(len(i) == 1):
                new+= i[0].upper()
            else:
                new+=i[0].upper() + i[1:]
        except:
            pass
    return new
print(alt_caps("Alternating Capitalization",r"(..)"))
