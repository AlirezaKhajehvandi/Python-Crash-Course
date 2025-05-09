# def get_formatted_name(first_name, last_name):
#     """Generate a neatly formatted full name"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()


# def get_formatted_name(first_name, middle_name, last_name):
#     """Generate a neatly formatted full name"""
#     full_name = f"{first_name} {middle_name} {full_name}"
#     return full_name.title()


def get_formatted_name(first_name, last_name, middle_name=''):
    """Generate a neatly formatted full name."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()







