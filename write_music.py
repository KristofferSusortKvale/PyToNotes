# c' = middle C = C4
# c - b = octave below middle C
# ' - higher
# , - lower
# rest is r, used same as notes
# time signature is set with \time i.e. \time 3/4
# \tempo sets time(bpm and/or name) i.e. \tempo "Presto" 4 = 120 for quarter note at 120 bpm
# clef can be set with \clef treble, \clef bass  (also tenor and alto)
# es - flat, is - sharp

from consts import LILYPOND_NOTES, LILYPOND_DURATIONS, LILYPOND_BASS


def key_w_note_to_lillypond(key_w_note):
    return LILYPOND_NOTES[key_w_note[0]], LILYPOND_DURATIONS[key_w_note[1]], key_w_note[0] in LILYPOND_BASS


def divide_into_bass_and_treble(keys_w_notes):
    bass = []
    treble = []
    for item in keys_w_notes:
        lilypond_note, lilypond_duration, is_bass = key_w_note_to_lillypond(
            item)
        if is_bass:
            bass.append(f"{lilypond_note}{lilypond_duration}")
            treble.append(f"r{lilypond_duration}")
        else:
            bass.append(f"r{lilypond_duration}")
            treble.append(f"{lilypond_note}{lilypond_duration}")

    return bass, treble


def write_lilypond_file(time_measurement, base_note, bpm, keys_w_notes):
    lilypond_base_note = LILYPOND_DURATIONS[base_note]
    bass, treble = divide_into_bass_and_treble(keys_w_notes)

    filepath = "output.ly"
    f = open(filepath, "w")
    f.write('\\version "2.24.1"\n')
    f.write('\n')

    # Write bass notes
    f.write("bassnotes =\n")
    f.write("{\n")
    f.write("   \\set Score.skipBars = ##t\n")
    f.write(f"   \\time {time_measurement}\n")
    f.write(f"   \\tempo {lilypond_base_note} = {bpm}\n")
    f.write("   \\clef bass\n")
    for note in bass:
        f.write(f"{note} ")
    f.write("\n}\n\n")

    # Write treble notes
    f.write("treblenotes =\n")
    f.write("{\n")
    f.write("   \\set Score.skipBars = ##t\n")
    f.write(f"   \\time {time_measurement}\n")
    f.write(f"   \\tempo {lilypond_base_note} = {bpm}\n")
    f.write("   \\clef treble\n")
    for note in treble:
        f.write(f"{note} ")
    f.write("\n}\n\n")

    f.write('<<\n')
    f.write("   \\new Staff \\treblenotes\n")
    f.write("   \\new Staff \\bassnotes\n")
    f.write(">>\n")

    f.close()

    return filepath
