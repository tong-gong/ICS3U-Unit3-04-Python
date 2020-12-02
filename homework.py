#!/usr/bin/env python3

# Created by Tong Gong
# Created time November 2020
# This is a  "Positive / Negative / 0" program.


def main():
    # This is the function to play the "Positive/Negative/0" program.

    # Input
    userinput = int(input("Enter the number you want check:"))
    print("")

    # Process & output
    if userinput > 0:
        print("It is a positive number")
    elif userinput < 0:
        print("It is a negative number")
    else:
        print("It is 0")


if __name__ == "__main__":
    main()
