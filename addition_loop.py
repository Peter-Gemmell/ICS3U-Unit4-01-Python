# Copyright (c) 2022 Peter Gemmell All rights reserved
# Created by Peter Gemmell
# Created on April 2022
# This program uses a loop to add sum


def main():
    # this function uses a loop to add sum
    loop_counter = 0
    total = 0

    # input
    integer_input_string = input("Enter a positive integer : ")

    # process & output
    try:
        integer_input = int(integer_input_string)
        while loop_counter < integer_input:
            loop_counter = loop_counter + 1
            total = total + loop_counter
        else:
            print(
                "The sum of all positive numbers from 1 to {0} is {1}.".format(
                    integer_input, total
                )
            )
    except Exception:
        print("Invalid integer entered, please try again.")

    print("Done.")


if __name__ == "__main__":
    main()
