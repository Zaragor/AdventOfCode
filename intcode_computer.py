
import copy
import math

def processInstructions(instructionAddress, stack):
    instructionCommand = stack[instructionAddress]
    opcode = int(str(instructionCommand)[-2:])
    if instructionCommand < 100:
        parameter_modes = ''
    else:
        parameter_modes = str(instructionCommand)[-3::-1]

    def read_parameters(parameter_mode, parameter):
        if parameter_mode == '0':
            return stack[parameter]
        elif parameter_mode == '1':
            return parameter
        

    def multiply(number_one, number_two, position):
        stack[position] = number_one * number_two
    def sum(number_one, number_two, position):
        stack[position] = number_one + number_two
    def write(to_write, position):
        stack[position] = to_write
    def read(position):
        return stack[position]
    if (opcode == 99):
        return (0, instructionAddress)
    elif (opcode == 1):
        while len(parameter_modes) < 2:
            parameter_modes = parameter_modes + '0'
        parameters_to_sum = list(map(read_parameters, parameter_modes, stack[instructionAddress + 1: instructionAddress + 3])) + [stack[instructionAddress + 3]]
        sum(*parameters_to_sum)
        instructionAddress = instructionAddress + 4
    elif (opcode == 2):
        while len(parameter_modes) < 2:
            parameter_modes = parameter_modes + '0'
        parameters_to_multiply = list(map(read_parameters, parameter_modes, stack[instructionAddress + 1: instructionAddress + 3])) + [stack[instructionAddress + 3]]
        multiply(*parameters_to_multiply)
        instructionAddress = instructionAddress + 4
    elif (opcode == 3):
        read_input = input("Enter input:")
        write_address = stack[instructionAddress + 1] 
        stack[write_address] = int(read_input)
        instructionAddress = instructionAddress + 2
    elif (opcode == 4):
        printAddress = stack[instructionAddress + 1]
        print(stack[printAddress])
        instructionAddress = instructionAddress + 2
    elif (opcode == 5):
        while len(parameter_modes) < 2:
            parameter_modes = parameter_modes + '0'
        parameters_for_if = list(map(read_parameters, parameter_modes, stack[instructionAddress + 1: instructionAddress + 3]))
        if parameters_for_if[0] != 0:
            stack[instructionAddress] = parameters_for_if[1]
            instructionAddress = parameters_for_if[1]
        else:
            instructionAddress += 3
    elif (opcode == 6):
        while len(parameter_modes) < 2:
            parameter_modes = parameter_modes + '0'
        parameters_for_if = list(map(read_parameters, parameter_modes, stack[instructionAddress + 1: instructionAddress + 3]))
        if parameters_for_if[0] == 0:
            stack[instructionAddress] = parameters_for_if[1]
            instructionAddress = parameters_for_if[1]
        else:
            instructionAddress += 3
    elif (opcode == 7):
        while len(parameter_modes) < 2:
            parameter_modes = parameter_modes + '0'
        parameters_for_comparison = list(map(read_parameters, parameter_modes, stack[instructionAddress + 1: instructionAddress + 3])) + [stack[instructionAddress + 3]]
        if parameters_for_comparison[0] < parameters_for_comparison[1]:
            stack[parameters_for_comparison[2]] = 1
        else:
            stack[parameters_for_comparison[2]] = 0
        instructionAddress += 4
    elif (opcode == 8):
        while len(parameter_modes) < 2:
            parameter_modes = parameter_modes + '0'
        parameters_for_comparison = list(map(read_parameters, parameter_modes, stack[instructionAddress + 1: instructionAddress + 3])) + [stack[instructionAddress + 3]]
        if parameters_for_comparison[0] == parameters_for_comparison[1]:
            stack[parameters_for_comparison[2]] = 1
        else:
            stack[parameters_for_comparison[2]] = 0
        instructionAddress += 4
    
    else:
        raise Exception("Instruction not expected" + str(instruction) + "_" + str(instructionCommand))   
    
    return (None, instructionAddress)

def calculate(stack):
    returnValue = None
    instruction_pointer = 0
    while instruction_pointer <= len(stack) - 1:
        returnValue, instruction_pointer = processInstructions(instruction_pointer, stack)
        if returnValue is not None: break
    
    return returnValue