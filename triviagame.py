# Define the Question class
class Question:

    # Initialize each Question objects (question text, possible answers, and correct answer)
    def __init__(self, question, answers, correct_answer):
        self.question       = question
        self.answers        = answers
        self.correct_answer = correct_answer

    # Check if the given answer is correct
    def is_correct(self, answer):
        return answer == self.correct_answer

    # Display the question and possible answers
    def display_question(self):
        print(self.question)
        for i, answer in enumerate(self.answers, 1):
            print(f"{i}. {answer}")

# Define the main function to play the trivia game and create a list of trivia questions
def trivia_game():
    questions = [ 
        Question("1. What is the capital of Turkey?"                               , ["London",       "Berlin",            "Istanbul",           "Madrid"],            3),
        Question("2. What is the capital of France?"                               , ["London",       "Berlin",            "Paris",              "Madrid"],            3),
        Question("3. What is the capital of Spain?"                                , ["London",       "Berlin",            "Paris",              "Madrid"],            4),
        Question("4. Which team won the UEFA Cup in 2000?"                         , ["Galatasaray",  "Arsenal",           "Borussia Dortmund",  "Real Madrid"],       3),
        Question("5. Which team won the UEFA Super Cup in 2000?"                   , ["Galatasaray",  "Real Madrid",       "FC Barcelona",       "Manchester United"], 3),
        Question("6. Who is the football player with the most Ballon d'Or titles?" , ["Lionel Messi", "Cristiano Ronaldo", "Ronaldinho",         "Maradona"],          1),
        Question("7. Who painted the Mona Lisa?"                                   , ["Frida Kahlo",  "Vincent Van Gogh",  "Salvador Dali",      "Leonardo da Vinci"], 4),
        Question("8. What is the largest ocean on Earth?"                          , ["Atlantic",     "Pasific",           "Indian",             "Arctic"],            2),
        Question("9. Which planet is closest to our sun?"                          , ["Mercury",      "Venus",             "Saturn",             "Jupiter"],           1),
        Question("10. What year did the Titanic sink?"                             , ["1914",         "1913",              "1919",               "1912"],              4)
    ]

    # Initialize scores for two players
    scores = [0, 0]

    # Loop over two players
    for i in range(2):
        print(f"Player {i + 1}'s turn:")

        # Each player answers all questions
        for question in questions:
            question.display_question()
            answer = int(input("Enter your answer (1-4): "))

            # Check if the answer is correct and update the score
            if question.is_correct(answer):
                scores[i] += 1
                print("Correct!")
            else:
                print("Wrong answer.")

    # Display the final results
    print("\nGame Over!")
    print(f"Player 1's score: {scores[0]}")
    print(f"Player 2's score: {scores[1]}")

    # Determine and announce the winner
    if scores[0] > scores[1]:
        print("Player 1 wins!")
    elif scores[1] > scores[0]:
        print("Player 2 wins!")
    else:
        print("It's a tie!")

# Run the game
if __name__ == "__main__":
    trivia_game()