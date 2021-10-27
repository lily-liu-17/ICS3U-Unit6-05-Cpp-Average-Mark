#!/usr/bin/env python3

# Created by: Lily Liu
# Created on: Oct 2021
# This program finds the average of the user's marks using lists


def marks_average(marks):
    # This function calculates the average
    average = 0

    for counter in marks:
        average = average + counter

    average = round(average / len(marks), 2)

    return average


def main():
    # this is the main funstion

    mark_list = []
    mark = 0

    print("Please enter 1 mark at a time. Enter -1 to end.\n")

    while True:
        user_marks = input("What is your mark? (as %): ")
        try:
            user_marks = int(user_marks)
            if user_marks > 0 and user_marks < 101:
                mark_list.append(user_marks)
            elif user_marks == -1:
                average = marks_average(mark_list)
                print("\nThe average is {0}%".format(average))
                break
            else:
                print("\nInvalid Input.")
                break
        except (Exception):
            print("\nInvalid Input.")
            break

    print("\nDone.")


if __name__ == "__main__":
    main()
