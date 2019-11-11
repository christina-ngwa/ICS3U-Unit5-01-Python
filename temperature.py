#!/usr/bin/env python3

# Created by: Christina Ngwa
# Created on: November 2019
# This program uses user defined functions


def fahrenheit():
    # calculates temperature from celsius to fahrenheit

    # input
    print("Let's convert temperatures from celsius to fahrenheit! ")
    temp_in_celsius_string = input("What is the temperature? (°C): ")
    print("")

    # process
    try:
        temp_in_celsius = int(temp_in_celsius_string)
        temp_in_fahrenheit = ((9/5) * temp_in_celsius + 32)
        print("The temperature is {0}°F in fahrenheit"
              "."format(temp_in_fahrenheit))
    except Exception:
        print("Wrong input. Try again.")


def main():

    # call function
    fahrenheit()


if __name__ == "__main__":
    main()
