import pretty_midi
import math
#Midi parser for TI Innovator Hub
#David Lafleur
#7/18/2021

##########################
# USER DEFINED VARIABLES #
##########################

#IMPORTANT!!!!
#this is the time interval between it checking for notes (in seconds)
#lower number means more lag, but more fidelity, 0.05 works for me
DIVISION = 0.05

#either track indexes or track names
#example: [1,2,3] or ["Track 1", "Drums"]
INSTRUMENT_OMIT_LIST = []
#use the print of the track names and indexes to determine which to remove
#sometimes track numbers from audacity arent the same as track numbers
#that are printed out (most of the time they are though)

#name of the midi file you want to use
#you can add a file path, or if its in the same folder as the script
#you can just write the name without the path ex: "fur_elise.mid"
MIDI_FILE_NAME = ""

########
# CODE #
########

#get midi data from file
midi_data = pretty_midi.PrettyMIDI(MIDI_FILE_NAME)

#big dictionary with that converts midi notes to TI innovator notes
pitch_to_note = {
  21: "A0",
  22: "AS0",
  23: "B0",
  24: "C1",
  25: "CS1",
  26: "D1",
  27: "DS1",
  28: "E1",
  29: "F1",
  30: "FS1",
  31: "G1",
  32: "GS1",
  33: "A1",
  34: "AS1",
  35: "B1",
  36: "C2",
  37: "CS3",
  38: "D2",
  39: "DS2",
  40: "E2",
  41: "F2",
  42: "FS2",
  43: "G2",
  44: "GS2",
  45: "A2",
  46: "AS2",
  47: "B2",
  48: "C3",
  49: "CS3",
  50: "D3",
  51: "DS3",
  52: "E3",
  53: "F3",
  54: "FS3",
  55: "G3",
  56: "GS3",
  57: "A3",
  58: "AS3",
  59: "B3",
  60: "C4",
  61: "CS4",
  62: "D4",
  63: "DS4",
  64: "E4",
  65: "F4",
  66: "FS4",
  67: "G4",
  68: "GS4",
  69: "A4",
  70: "AS4",
  71: "B4",
  72: "C5",
  73: "CS5",
  74: "D5",
  75: "DS5",
  76: "E5",
  77: "F5",
  78: "FS5",
  79: "G5",
  80: "GS5",
  81: "A5",
  82: "AS5",
  83: "B5",
  84: "C6",
  85: "CS6",
  86: "D6",
  87: "DS6",
  88: "E6",
  89: "F6",
  90: "FS6",
  91: "G6",
  92: "GS6",
  93: "A6",
  94: "AS6",
  95: "B6",
  96: "C7",
  97: "CS7",
  98: "D7",
  99: "DS7",
  100: "E7",
  101: "F7",
  102: "FS7",
  103: "G7",
  104: "GS7",
  105: "A7",
  106: "AS7",
  107: "B7",
  108: "C8",
}

#calculates the number of divisions in the song
number_of_divisions = math.ceil(midi_data.get_end_time()/DIVISION)

#creates an array for each divison there will be in the song
note_list = {}
for i in range(number_of_divisions):
    note_list[i] = []

#prints instrument index and their name to be able to identify them
#to add them to the omit list.
for idx, instrument in enumerate(midi_data.instruments):
    print(f"{idx+1}: \"{instrument.name}\"")

for time_slice_index in range(number_of_divisions):
    for idx, instrument in enumerate(midi_data.instruments):
        #removes the ommited instruments
        if instrument.name not in INSTRUMENT_OMIT_LIST and idx+1 not in INSTRUMENT_OMIT_LIST:
            for note in instrument.notes:
                currentTime = time_slice_index*DIVISION
                #checks if a note is being played in the current
                #time slice of the song we are looking at (very inneficient)
                if currentTime >= note.start and currentTime <= note.end:
                    #converts the notes and adds them to the dictionary
                    note_list[time_slice_index].append(pitch_to_note[note.pitch])

#prints out the list to the user
print("\nCopy from the \"{\" to the \"}\" and paste it after the \"note_dict =\" line in the TI Innovator Hub program")
print(note_list)
input("Press enter to exit")
