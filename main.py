# This is a sample Python script.
import requests as req
import html
import random


# Use html.unescape to remove &quot; HTML codes
def get_questions():
    """Get questions from opentdb.com api and parse it Array[Dictionary {}, Dictionary {}]"""
    response = req.get("https://opentdb.com/api.php?amount=10")
    response = response.json()
    if response["response_code"] == 0:
        print("Response OK!")
        return response["results"]
    else:
        raise Exception("Reponse not 0: " + response["response_code"])


def main():
    score = 0
    questions = get_questions()
    for question in questions:
        print("\nThis question is from the " + str(
            html.unescape(question["category"])) + " category.\nDifficulty:  " + str(
            html.unescape(question["difficulty"])).title() + "\n\n" + str(html.unescape(question["question"])) + "\n")
        length = len(question["incorrect_answers"]) + 2
        random_position = random.randint(1, length)
        inserted_correct = False
        for x in range(1, length):
            if x == random_position:
                print(str(x) + ".  " + html.unescape(question["correct_answer"]))
            else:
                if inserted_correct:
                    print(str(x) + ".  " + html.unescape(question["incorrect_answers"][x - 1]))
                else:
                    print(str(x) + ".  " + html.unescape(question["incorrect_answers"][x - 2]))
        inp = input("\nAnswer: ")
        while 1:  # input validation
            if int(inp) in list(range(1, length)):
                inp = int(inp)
                break
            else:
                inp = input("\nAnswer: ")
        if inp == random_position:  # Is correct?
            score += 1
        else:
            pass
    print("\n\n Your final score is: " + str(score))
    yn = input("Play Again?\n>: ").upper()
    if yn == "YES" or yn == "Y":
        main()
    else:
        raise Exception("Game Ended")
    return ""


if __name__ == '__main__':
    main()
