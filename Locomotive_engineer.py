"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*wagons):
    """Return a list of wagons, given an arbitrary amount of wagon numbers.

    Parameters:
       An arbitrary number of wagon numbers, unpacked.

    Returns:
        list: A list of wagon numbers.
    """
    l = []
    for wagon in wagons:
        l.append(wagon)

    return l

# print(get_list_of_wagons(1, 7, 12, 3, 14, 8, 5))

def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    Parameters:
        each_wagons_id (list[int]): The list of wagons.
        missing_wagons (list[int]) The list of missing wagons.

    Returns:
        list[int]: The corrected list of wagons.
    """
    final_list = ([each_wagons_id[2]] + missing_wagons + each_wagons_id[3:] + [each_wagons_id[0]] + [each_wagons_id[1]])
    return final_list

# print(fix_list_of_wagons([2, 5, 1, 7, 4, 12, 6, 3, 13], [3, 17, 6, 15])) 


def add_missing_stops(route_dict: dict, **kwargs):
    """Add missing stops to route dict.

    Parameters:
        route (dict): The dict of routing information.
        (dict): arbitrary number of stops.

    Returns:
        dict: The updated route dictionary.
    """
    stops_list = list(kwargs.values())
    route_dict["stops"] = stops_list
    return route_dict

# print(add_missing_stops({"from": "New York", "to": "Miami"},
#                       stop_1="Washington, DC", stop_2="Charlotte", stop_3="Atlanta",
#                       stop_4="Jacksonville", stop_5="Orlando"))


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    Parameters:
        route (dict): The route information.
        more_route_information (dict): The extra route information.

    Returns:
        dict: The extended route information.
    """
    route_info = route | more_route_information
    return route_info

# print(extend_route_information({"from": "Berlin", "to": "Hamburg"}, {"length": "100", "speed": "50"}))


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    Parameters:
        wagons_rows (list[tuple]) The list of rows of wagons.

    Returns:
        list[tuple]: the list of rows of wagons.
    """

    return [list(column) for column in zip(*wagons_rows)]

# print(fix_wagon_depot([
#                     [(2, "red"), (4, "red"), (8, "red")],
#                     [(5, "blue"), (9, "blue"), (13,"blue")],
#                     [(3, "orange"), (7, "orange"), (11, "orange")],
#                     ]))