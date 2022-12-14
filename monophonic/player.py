import numpy as np
import re

from vocabulary import FREQ, DUR

from midiutil.MidiFile import MIDIFile

pitch_to_MIDI = {
    "C8": 108,
    "B7": 107,
    "Bb7": 106,
    "A#7": 106,
    "A7": 105,
    "Ab7": 104,
    "G#7": 104,
    "G7": 103,
    "Gb7": 102,
    "F#7": 102,
    "F7": 101,
    "E7": 100,
    "Eb7": 99,
    "D#7": 99,
    "D7": 98,
    "Db7": 97,
    "C#7": 97,
    "C7": 96,
    "B6": 95,
    "Bb6": 94,
    "A#6": 94,
    "A6": 93,
    "Ab6": 92,
    "G#6": 92,
    "G6": 91,
    "Gb6": 90,
    "F#6": 90,
    "F6": 89,
    "E6": 88,
    "Eb6": 87,
    "D#6": 87,
    "D6": 86,
    "Db6": 85,
    "C#6": 85,
    "C6": 84,
    "B5": 83,
    "Bb5": 82,
    "A#5": 82,
    "A5": 81,
    "Ab5": 80,
    "G#5": 80,
    "G5": 79,
    "Gb5": 78,
    "F#5": 78,
    "F5": 77,
    "E5": 76,
    "Eb5": 75,
    "D#5": 75,
    "D5": 74,
    "Db5": 73,
    "C#5": 73,
    "C5": 72,
    "B4": 71,
    "Bb4": 70,
    "A#4": 70,
    "A4": 69,
    "Ab4": 68,
    "G#4": 68,
    "G4": 67,
    "Gb4": 66,
    "F#4": 66,
    "F4": 65,
    "E4": 64,
    "Eb4": 63,
    "D#4": 63,
    "D4": 62,
    "Db4": 61,
    "C#4": 61,
    "C4": 60,
    "B3": 59,
    "Bb3": 58,
    "A#3": 58,
    "A3": 57,
    "Ab3": 56,
    "G#3": 56,
    "G3": 55,
    "Gb3": 54,
    "F#3": 54,
    "F3": 53,
    "E3": 52,
    "Eb3": 51,
    "D#3": 51,
    "D3": 50,
    "Db3": 49,
    "C#3": 49,
    "C3": 48,
    "B2": 47,
    "Bb2": 46,
    "A#2": 46,
    "A2": 45,
    "Ab2": 44,
    "G#2": 44,
    "G2": 43,
    "Gb2": 42,
    "F#2": 42,
    "F2": 41,
    "E2": 40,
    "Eb2": 39,
    "D#2": 39,
    "D2": 38,
    "Db2": 37,
    "C#2": 37,
    "C2": 36,
    "B1": 35,
    "Bb1": 34,
    "A#1": 34,
    "A1": 33,
    "Ab1": 32,
    "G#1": 32,
    "G1": 31,
    "Gb1": 30,
    "F#1": 30,
    "F1": 29,
    "E1": 28,
    "Eb1": 27,
    "D#1": 27,
    "D1": 26,
    "Db1": 25,
    "C#1": 25,
    "C1": 24,
    "B0": 23,
    "Bb0": 22,
    "A#0": 22,
    "A0": 21
}

def music_str_parser(semantic):
    # finds string associated with symb
    found_str = re.compile(r'((note|gracenote|rest|multirest)(\-)(\S)*)'
                           ).findall(semantic)
    music_str = [i[0] for i in found_str]
    # finds the note's alphabets 
    fnd_notes = [re.compile(r'(([A-G](b|#)?[1-6])|rest)'
                    ).findall(note) for note in music_str]
    # stores the note's alphabets
    notes = [m[0][0] for m in fnd_notes]
    found_durs = [re.compile(r'((\_|\-)([a-z]|[0-9])+(\S)*)+'
                    ).findall(note) for note in music_str]
    #split by '_' every other string in list found in tuple of lists 
    durs = [i[0][0][1:].split('_') for i in found_durs]
    return notes, durs


def dur_evaluator(durations):
    note_dur_computed = []
    for dur in durations:
        # if dur_len in DUR dict, get. Else None 
        dur_len = [DUR.get(i.replace('.','').replace('.',''), 
                              None) for i in dur]
        # filter/remove None values, and sum list
        dur_len_actual = sum(list(filter(lambda a: a !=None, 
                                      dur_len)))
        # actual duration * 4 = quadruple
        if 'quadruple' in dur:
            dur_len_actual = dur_len_actual * 4
        # actual duration * 2 = fermata
        elif 'fermata' in dur:
            dur_len_actual = dur_len_actual * 2
        # actual duration + 1/2 of duration = .
        elif '.' in ''.join(dur):
            dur_len_actual = dur_len_actual + (dur_len_actual * 1/2)
        elif '..' in ''.join(dur):
            dur_len_actual = dur_len_actual +(2 *(dur_len_actual * 1/2))
        # if no special duration string
        elif dur[0].isnumeric():
            dur_len_actual = float(dur[0]) * .5
        note_dur_computed.append(dur_len_actual)
    return note_dur_computed

def get_music_note(semantic):
    notes, durations = music_str_parser(semantic)
    print('notes', notes)
    print('durations', durations)
    sample_rate = 44100
    timestep = []
    T = dur_evaluator(durations)
    for i in T:
        # gets timestep for each sample 
        timestep.append(np.linspace(0, i, int(i * sample_rate), 
                                    False))
    def get_freq(notes):
        # get pitchs frequency from dict
        pitch_freq = [FREQ[i] for i in notes]
        return pitch_freq

    ### create midi file
    midi = MIDIFile(1)
    track = 0
    time = 0
    channel = 0
    volume = 100

    midi.addTrackName(track, time, 'Track')
    midi.addTempo(track, time, 110)

    for i in range(len(notes)):
        if(notes[i]=='rest'):
            pitch=108
            volume=0
        else:
            pitch=pitch_to_MIDI[notes[i]]
            volume=100
            ### TODO: add more conditions for durations
        duration=1 #half
        [d]=durations[i]
        duration=DUR[d]

        midi.addNote(track, channel, pitch, time, duration,volume)
        time+=duration
    binfile = open('output/output.mid', 'wb')
    midi.writeFile(binfile)
    binfile.close()

    return timestep, get_freq(notes)


def get_sinewave_audio(semantic):
    audio = []
    timestep, freq = get_music_note(semantic)
    for i in range(len(freq)):
        # calculates the sinewave
        audio.append(np.sin(
            freq[i] * timestep[i] * 2 * np.pi))
    return audio