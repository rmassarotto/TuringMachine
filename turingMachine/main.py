from model.TuringMachine import TuringMachine
from model.Tape import Tape
from model.State import State
from config.TuringMachine import MachineConfig
from config.State import StateConfig

configFile = open('wwSimpler.txt', 'r').read().splitlines()
tapeData = list('bbBBX')

tape = Tape(tapeData, 0, tapeData[0])
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

transitions = []
listOfStates = []
listOfStatesToExecute = []

for val in turing.transitions:
    transitions.append(val.split())

for t in transitions:
    state = State(
        t[StateConfig.atState],
        t[StateConfig.toState],
        t[StateConfig.read],
        t[StateConfig.write],
        t[StateConfig.move]
    )
    listOfStates.append(state)
    #state.stateInfo()

listOfStatesToExecute.append(turing.startState)

while listOfStatesToExecute:
    #print(listOfStatesToExecute)
    for listExecute in listOfStatesToExecute:
        for statesList in listOfStates:
            if listExecute == statesList.state and tape.headData == statesList.read:
                print('Estado de execução:', listExecute)
                print('Conteudo Fita: ',tape.headData)
                statesList.stateInfo()
                tape.data[tape.head] = statesList.write
                tape.headMove(statesList.move)
                listOfStatesToExecute.append(statesList.toState)
                tape.tapeInfo()
            #else:
            #    print('Estado de execução:', listExecute)
            #    print('Conteudo Fita: ',tape.headData)
            #    statesList.stateInfo()
            #    print('pass')


        listOfStatesToExecute.remove(listExecute)

        #print(listOfStatesToExecute)
