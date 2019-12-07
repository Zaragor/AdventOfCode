
import copy
import math

def processInstructions(instructionAddress, inputOneAddress, inputTwoAddress, inputThreeAddress, stack):
    instructionCommand = stack[instructionAddress]
    inputOneValue = stack[inputOneAddress]
    inputTwoValue = stack[inputTwoAddress]
    inputThreeValue = stack[inputThreeAddress]
    if (instructionCommand == 1):
        stack[inputThreeValue] = stack[inputOneValue] + stack[inputTwoValue]
        #print("adding {} and {} and putting to position {}".format(inputOneValue, inputTwoValue, inputThreeValue))
    elif (instructionCommand == 2):
        stack[inputThreeValue] = stack[inputOneValue] * stack[inputTwoValue]
        #print("multiplying {} and {} and putting to position {}".format(inputOneValue, inputTwoValue, inputThreeValue))
    elif (instructionCommand == 99):
        print("The answer is {}".format(stack[0]))
        return stack[0]
    else:
        raise Exception("Instruction not expected" + str(instruction) + "_" + str(instructionCommand))   
    
    return 0

    
if __name__ == "__main__":
    originalStack = list([1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,9,19,23,1,6,23,27,1,10,27,31,1,5,31,35,2,6,35,39,1,5,39,43,1,5,43,47,2,47,6,51,1,51,5,55,1,13,55,59,2,9,59,63,1,5,63,67,2,67,9,71,1,5,71,75,2,10,75,79,1,6,79,83,1,13,83,87,1,10,87,91,1,91,5,95,2,95,10,99,2,9,99,103,1,103,6,107,1,107,10,111,2,111,10,115,1,115,6,119,2,119,9,123,1,123,6,127,2,127,10,131,1,131,6,135,2,6,135,139,1,139,5,143,1,9,143,147,1,13,147,151,1,2,151,155,1,10,155,0,99,2,14,0,0])
    
    returnValue = None
    for i in range(100 * 100):
        stack = copy.deepcopy(originalStack)
        stack[1] = int(i / 100)
        stack[2] = i % 100
        print("Trying {}, {}".format(stack[1], stack[2]))
        for j in range(0, len(stack) - 1, 4):
            returnValue = processInstructions(j, j + 1, j + 2, j + 3, stack)
        
        if (returnValue == 19690720):
            break
    
    print("Position 1: {} Position 2: {}".format(i / 100, i % 100))