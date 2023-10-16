
def letters_to_halfwidth(text):
    """Convert text to halfwidth letters.
    """
    
    converted_text = ""
    for char in text:
        if 65281 <= ord(char) <= 65374:  # Full-width range in Unicode
            converted_text += chr(ord(char) - 65248)
        else:
            converted_text += char
    return converted_text

def letters_to_fullwidth(text):
    """Converts text to fullwidth letters.
    """

    converted_text = ""
    for char in text:
        if 33 <= ord(char) <= 126:  # Half-width range in ASCII
            converted_text += chr(ord(char) + 65248)
        else:
            converted_text += char
    return converted_text
