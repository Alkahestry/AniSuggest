def apply_function_list(list : list, function) -> list:
    """Applies a function to each element of a list.

    Args:
        list (list): The target list to apply a function to.
        function (function): Function to be applied to the every single parameter in the list.

    Returns:
        list: A list with the same length as the input list, but with the function applied to every single parameter.
    """
    return [function(item) for item in list]

def remove_end_period(string : str) -> str:
    if string[-1] == '.':
        return string[:-1]
    return string

def remove_end_period_list(list : list) -> list:
    return [remove_end_period(item) for item in list]

def remove_none_value_list(lst : list) -> list:
    return [item for item in lst if item is not None]