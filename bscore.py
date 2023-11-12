import sys


def retry():
    print("Do you want to try again?\nYes/No ")
    rtr = input().lower()
    if "yes" in rtr:
        use()
    else:
        sys.exit()


def use():
    while True:
        try:
            b_score = float(input("Input your behaviour score here: "))
            if b_score <= 3000:
                print("Your behaviour score is too low for Ranked Matchmaking.")
                retry()
            elif b_score >= 3000 and not b_score >= 8000:
                print("Your behaviour score is enough for Ranked Matchmaking, though not recommended."
                      "\nWe advise you to get your score to 8000.")
                retry()
            elif b_score >= 8000 and not b_score > 12000:
                print("Your behaviour score is good for Ranked Matchmaking")
                retry()
            elif b_score > 12000:
                print("Invalid value, maximum behaviour score is 12000.")
        except ValueError:
            print("Must be a valid number!")


use()




