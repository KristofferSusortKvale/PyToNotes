from consts import REST, SHORT, HIGH


def remove_starting_rest(key_note_list):
    if key_note_list[0][0] == REST:
        key_note_list.pop(0)
    return key_note_list


def remove_ending_rest(key_note_list):
    if key_note_list[len(key_note_list) - 1][0] == REST:
        key_note_list.pop(len(key_note_list) - 1)

    return key_note_list


def remove_highs(key_note_list):
    newlist = []
    for item in key_note_list:
        if item[0] != HIGH:
            newlist.append(item)

    return newlist


def remove_shorts(key_note_list):
    newlist = []
    for item in key_note_list:
        if item[1] != SHORT:
            newlist.append(item)

    return newlist


def clean_up(key_note_list):
    cleaned_1 = remove_starting_rest(key_note_list)
    cleaned_2 = remove_ending_rest(cleaned_1)
    cleaned_3 = remove_shorts(cleaned_2)
    cleaned_4 = remove_highs(cleaned_3)

    return cleaned_4
