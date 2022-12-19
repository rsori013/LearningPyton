from Question import Question
questions_prompt = [
    "What is the capital of France? \n(a) Manila \n(b) Madrid \n(c) Paris \n\n",
    "What color is a Banana? \n(a) Red \n(b) Blue \n(c) Yellow \n (d) Pink \n\n",
    "What are the colors of Japan, white and what? \n(a) Red \n(b) Blue \n (c) Green \n (d) Pink \n\n"
]

questions = [
    Question(questions_prompt[0],"c"),
    Question(questions_prompt[1],"c"),
    Question(questions_prompt[2],"a"),
]




def run_test(questions):
    score = 0
    for question in questions:
        answer = input (question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/"  + str(len(questions)) + " correct")
    

run_test(questions)
