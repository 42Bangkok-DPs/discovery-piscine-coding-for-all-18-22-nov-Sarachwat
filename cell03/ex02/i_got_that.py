#!/usr/bin/env python3

def main():
    userinput = input("What you gotta say? : ")
    while True:

        if userinput == "STOP": 
            break 
        else:
            userinput = input("I got that! Anything else? : ")

if __name__ == "__main__":
    main()