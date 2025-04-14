# from functions import get_formatted_name

# print("Enter 'q' at any time to quit")
# while True:
#     first_name = input("\nPlease Enter Your First Name: ")
#     if first_name == 'q':
#         break
#     last_name = input("\nPlease Enter Your Last Name: ")
#     if last_name == 'q':
#         break

#     formatted_name = get_formatted_name(first_name, last_name)
#     print(f"\n\tNeatly formatted name: {formatted_name}.")

# from classes import AnonymousSurvey

# # Define a question, and make a survey.
# question = "What language did you first learn to speak?"
# language_survey = AnonymousSurvey(question)

# # Show the question, and store responses to the question.
# language_survey.show_question()
# print("Enter 'q' at any time to quit.\n")

# while True:
#     response = input("Language: ")
#     if response == 'q':
#         break
#     language_survey.store_response(response)
    
#     # Show the survey results.
#     print("\nThank you to everyone who participated in the survey!")
#     language_survey.show_results()

def say_hello(func):
    def inner():
        print("Before calling the function...")
        print("Hello...!")
        func()
        print("After calling the function...")
    return inner

@say_hello
def say_hi():
    print("Hi...")



say_hi()  

