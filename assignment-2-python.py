# Import libraries
import requests  # To interact with the trivia API
import random  # For random questions
import time  # For adding a time limit to answer questions


# Function to get trivia data from the open trivia database API
def get_trivia_questions():
# API call to open trivia database with specific parameters (20 questions, category 11, medium difficulty, multiple choice)
    response = requests.get("https://opentdb.com/api.php?amount=20&category=11&difficulty=medium&type=multiple")
    data = response.json()
    return data["results"]
 # Extracting the results from the JSON response


# Function to ask questions and check user answers
def ask_question(question_data, question_num):
# Extract the question and correct/incorrect answers from the question data
    question = question_data['question']
    correct_answer = question_data['correct_answer']
    incorrect_answers = question_data['incorrect_answers']

    # combine correct and incorrect answers, then shuffle them for random order
    all_answers = incorrect_answers + [correct_answer]
    random.shuffle(all_answers)

    # Display the question and the shuffled answers
    print(f"\nQuestion {question_num}: {question}")
    for i, answer in enumerate(all_answers, 1):
        print(f"{i}. {answer}")

    # Return the correct answer
    return correct_answer, all_answers


# Function to handle user answer input
def get_user_answer(all_answers):
    try:
         # Input from user (1-4), show that the input is a number
         user_choice = int(input("Enter the number relating to your answer: "))
         return all_answers[user_choice - 1] # return the selected answer
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid number.")
        return get_user_answer(all_answers)


# Function to provide a hint (slicing the correct answer for partial reveal)
def provide_hint(correct_answer):
    # Reveal first half of the correct answer
    hint = correct_answer[:len(correct_answer) // 2] + "..."
    print(f"hint: {hint}")


# Main function to run the trivia game
def play_trivia():
    questions = get_trivia_questions()  # Fetch trivia questions from the API
    score = 0
    hints_used = 0
    total_questions = len(questions)

    for i, question_data in enumerate(questions, 1):
        correct_answer, all_answers = ask_question(question_data, i)
        # Add a time limit of 10 seconds for each question
        start_time = time.time()
        user_input = input("Need a hint? Type 'hint or press Enter to answer: ")

        # if user requests a hint, provide it
        if user_input.lower() == 'hint':
            provide_hint(correct_answer)
            hints_used += 1

        # Ask for the answer after hint or directly
        user_answer = get_user_answer(all_answers)

        # check if answer is correct
        if user_answer == correct_answer:
            print("Correct!")
            score += 1  # Add point for the correct answer
        else:
            print(f"Wrong! The correct answer was: {correct_answer}")

        # Check if the time limit exceeded
        if time.time() - start_time > 10:
            print("Time's up! Moving to the next question.")


    # Define the custom path for trivia_results.txt
    file_path = "/Users/muniramansaray/PycharmProjectscfg-pythoncfg-python/CFG-Assignments/trivia_results.txt"

    # Display final score and hints used
    print(f"\nGame over! Your final score: {score}/{total_questions}")
    print(f"Hints used: {hints_used}")

    # Write the score to a file
    try:
        with open(file_path, "a") as file:
             file.write(f"Score: {score}/{total_questions} | Hints used: {hints_used}\n")
        print(f"Your results have been saved to {file_path}.")
    except Exception as e:
         print(f"An error occurred while writing to the file: {e}")



# Check if user wants to play again
def main():
    play_trivia()  # starting the trivia game
    while True:
        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay == "yes":
            play_trivia()  # replay the game
        else:
            print("Thank you for playing!")
            break
# Main function called
if __name__ == "__main__":
    main()




