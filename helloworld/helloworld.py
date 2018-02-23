import datetime


def helloworld(name=None, birthMonthNum=None, Nehabday=None):

    """return hello world, or hello {name}"""

# Print greeting
    if not name:
        print("hello world")
    else:
        print("hello {}".format(name))

# Print birth month.
    if birthMonthNum:
        if birthMonthNum == 12:
            print("You were born during the best month.")
        if birthMonthNum > 12 or birthMonthNum < 0:
            print("Enter in a number between 1 and 12")
        else:
            print("You were born during the worst month.")
        if not birthMonthNum:
            print("You were never born.")

# Print days til Neha's birthday
    if Nehabday:
        neha_bday = datetime.datetime(2018, 12, 2)
        diff = neha_bday - datetime.datetime.now()
        print("There are {} days until Neha's Birthday!".format(diff.days))
