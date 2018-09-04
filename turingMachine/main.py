from model.TuringMachine import TuringMachine
from model.Configuration import Configuration

configFile = open('copy.txt', 'r').read().splitlines()

turing = TuringMachine(
    configFile[Configuration.entranceAlphabet],
    configFile[Configuration.tapeAlphabet],
    configFile[Configuration.blankSimbol],
    configFile[Configuration.startState],
    configFile[Configuration.endStates],
    configFile[Configuration.tapeNumber],
    configFile[Configuration.transitions:]
)
turing.turingMachineInfo()
