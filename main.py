# This is a sample Python script.
import requests as req
import html
import random


# Use html.unescape to remove HTML codes such as &quot;
def get_questions():
    """Get questions from opentdb.com api and parse it Array[Dictionary {}, Dictionary {}]"""
    response = req.get("https://opentdb.com/api.php?amount=10") # send request for data to the URL
    response = response.json() # Convert the JSON data from the request to a dictionary
    if response["response_code"] == 0: # Inspect the dictionary for a response code, and if it is good then continue, else raise an exeption
        print("Response OK!")
        return response["results"]
    else:
        raise Exception("Reponse not 0: " + response["response_code"])


def main():
    score = 0
    questions = get_questions()
    for question in questions: # index through the 10 questions gained from the get_questions sub
        print("\nThis question is from the " + str(
            html.unescape(question["category"])) + " category.\nDifficulty:  " + str(
            html.unescape(question["difficulty"])).title() + "\n\n" + str(html.unescape(question["question"])) + "\n") # Print info about the question and the actual question
        length = len(question["incorrect_answers"]) + 2 # add 2 for correct question and indexing
        random_position = random.randint(1, length)
        inserted_correct = False
        for x in range(1, length):
            if x == random_position:
                print(str(x) + ".  " + html.unescape(question["correct_answer"]))
            else:
                if inserted_correct: # indexing will change depending on if the correct answer has been inserted or not
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
        if inp == random_position:
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
