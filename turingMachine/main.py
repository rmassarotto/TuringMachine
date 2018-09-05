from model.TuringMachine import TuringMachine
from model.Tape import Tape
from config.TuringMachine import MachineConfig
from config.State import StateConfig

configFile = open('ww.txt', 'r').read().splitlines()
tapeData = list('AabbaAX')

tape = Tape(tapeData)
turing = TuringMachine(
    configFile[MachineConfig.entranceAlphabet],
    configFile[MachineConfig.tapeAlphabet],
    configFile[MachineConfig.blankSimbol],
    configFile[MachineConfig.states],
    configFile[MachineConfig.startState],
    configFile[MachineConfig.endStates],
    configFile[MachineConfig.tapeNumber],
    configFile[MachineConfig.transitions:]
)
turing.turingMachineInfo()
tape.tapeInfo()
