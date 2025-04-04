from functions import get_formatted_name

def test_first_last_name():
    """Do names like 'Alireza Khajehvandi' work?"""
    formatted_name = get_formatted_name("alireza", "khajehvandi")
    assert formatted_name == "Alireza Khajehvandi"

def test_first_last_middle_name():
    """Do names like 'Wolfgang Amadeus Mozart' workd?"""
    formatted_name = get_formatted_name("wolfgang", "mozart", "amadeus")
    assert formatted_name == "Wolfgang Amadeus Mozart"


# def test_second_first_last_name():
#     """Do names like 'Alireza Khajehvandi' work?"""
#     formatted_name = get_formatted_name("alireza", "khajehvandi")
#     assert formatted_name == "Alireza Khajehvandi"


