def is_palindrome(string):
    """
    Checks if a given string is a palindrome.

    Args:
        string (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Remove spaces and convert to lowercase
    string = string.replace(" ", "").lower()

    # Check if the string is equal to its reverse
    if string == string[::-1]:
        return True
    else:
        return False
