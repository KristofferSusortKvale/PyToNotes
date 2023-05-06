import librosa

from itertools import groupby

from consts import NOTE_FREQUENCIES


def find_frequencies(file):
    y, sr = librosa.load(file)
    f0, voiced_flag, voiced_probs = librosa.pyin(
        y, fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C7'))
    return f0


def map_to_tuples(lst, duration_per_sample):
    grouped = groupby(lst)
    result = [(k, sum(duration_per_sample for _ in g)) for k, g in grouped]
    return result


def find_closest_key(num):
    closest_freq = min(NOTE_FREQUENCIES.keys(), key=lambda x: abs(x - num))
    closest_name = NOTE_FREQUENCIES[closest_freq]
    return closest_name


def classify(file, duration):
    frequencies = find_frequencies(file)
    keys = []
    for frequency in frequencies:
        keys.append(find_closest_key(frequency))

    duration_per_sample = duration / len(frequencies)

    return map_to_tuples(keys, duration_per_sample)
