def find_maximum(numbers):
    """
    Finds the maximum element in a list of numbers.

    Args:
    - numbers (list): A list of numbers.

    Returns:
    - The maximum element in the list.
    """
    if not numbers:
        return None

    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num

    return maximum
