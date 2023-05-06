import math
from consts import SHORT, NOTES


def get_note_durations(bpm, basis_note):
    beat_duration_secs = 60 / bpm
    basis_note_duration = NOTES[basis_note]

    durations = {}

    for name in NOTES:
        durations[name] = beat_duration_secs * \
            (NOTES[name] / basis_note_duration)

    durations[SHORT] = 0

    return durations


def map_duration_to_note_name(key_duration, note_duration_dict):
    result = []
    for key, duration in key_duration:
        for name in note_duration_dict:
            note_length = note_duration_dict[name]
            if duration >= note_length:
                result.append((key, name))
                break
    return result


def closest_duration(num, durations):
    closest_note = 'something is wrong'
    closest_diff = math.inf
    for note in durations:
        diff = abs(num - durations[note])
        if diff < closest_diff:
            closest_diff = diff
            closest_note = note

    return closest_note


def durations_to_notes(bpm, basis_note, key_duration_tuples):
    note_durations = get_note_durations(bpm, basis_note)
    # return map_duration_to_note_name(key_duration_tuples, note_durations)
    keys_w_notes = []
    for key, duration in key_duration_tuples:
        keys_w_notes.append(
            (key, closest_duration(duration, note_durations)))

    return keys_w_notes
