# Assignment 1 written by - Praneeth Rayasam  # UCID- phr2

def convert_seconds(seconds):
    input_seconds = seconds

    # Convert seconds to days and update the remaining seconds
    days = int(seconds/86400)
    seconds = seconds%86400

    # Convert seconds to hours and update the remaining seconds
    hours = int(seconds/3600)
    seconds = seconds%3600

    # Convert seconds to minutes and update the remaining seconds
    minutes = int(seconds/60)
    seconds = seconds%60

    print(input_seconds, "seconds is: ")
    print(days, "days")
    print(hours, "hours")
    print(minutes,"minutes")
    print(seconds,"seconds")

seconds = input("Enter time in seconds:")
convert_seconds(int(seconds))