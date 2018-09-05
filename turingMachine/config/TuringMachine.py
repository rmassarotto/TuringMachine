from enum import IntEnum

class MachineConfig(IntEnum):
    entranceAlphabet = 0
    tapeAlphabet = 1
    blankSimbol = 2
    states = 3
    startState = 4
    endStates = 5
    tapeNumber = 6
    transitions = 7
