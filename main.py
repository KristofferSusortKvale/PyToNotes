from record import Record
from play import play
from classify import classify
from notes import durations_to_notes
from cleanup import clean_up
from write_music import write_lilypond_file

if __name__ == '__main__':
    duration_secs = int(input("How many seconds would you like to record? "))
    bpm = int(input("What is the bpm? "))
    time_measure = input("What is the time measure? ")

    basis_note_num = time_measure.split("/")[1]

    if basis_note_num not in ["1", "2", "4", "8"]:
        print("The time measure was not recognized, or is not supported at this time")
        time_measure = input("What is the time measure? ")
        basis_note_num = time_measure.split("/")[1]
        while basis_note_num not in ["1", "2", "4", "8"]:
            print("The time measure was not recognized, or is not supported at this time")
            time_measure = input("What is the time measure? ")
            basis_note_num = time_measure.split("/")[1]

    if basis_note_num == "1":
        basis_note = 'whole'
    elif basis_note_num == "2":
        basis_note = 'half'
    elif basis_note_num == "4":
        basis_note = 'quarter'
    elif basis_note_num == "8":
        basis_note = "eighth"
    else:
        print("Something went wrong while interperting the time measure")
        exit()

    r = Record()
    r.open()
    input("Press enter to start recording")
    f = r.start(duration_secs)
    r.close()

    # play(f)

    keys_w_duration = classify(f, duration_secs)

    keys_w_notes = durations_to_notes(bpm, basis_note, keys_w_duration)

    cleaned_list = clean_up(keys_w_notes)

    filepath = write_lilypond_file(time_measure, basis_note, bpm, cleaned_list)

    print(filepath)
