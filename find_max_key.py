def find_max_key(data: dict):
    """
    Return the maximum int or float key in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum key in the dictionary.
    """
    a=0
    x=0
    for i in data.keys():
        if i>x:
            x=i
    return x
print(find_max_key({
    1: 'a', 
    2: 'b', 
    3: 'c'
  })) 