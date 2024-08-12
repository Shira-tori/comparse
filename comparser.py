#!/bin/python3
import sys
import inspect

arguments = []
descriptions = []

#TODO: find a way to parse the arguments

def addArgument(argument, description):
    arguments.append(argument)
    descriptions.append(description)

def printUsage():
    stack = inspect.stack()
    caller_frame = stack[1]
    filename = caller_frame.filename.split("./")
    print(f'usage: ./{filename[1]} ', end="")
    for i,j in zip(arguments, descriptions):
        if j != '':
            print(f"[{i} {j}]", end=" ")
        else:
            print(f"[{i}]", end=" ")
    print("")

if __name__ == '__main__':
    addArgument('-b', '-start a server')
    addArgument('destination', '-ip address')
    addArgument('port', '')
    printUsage();
