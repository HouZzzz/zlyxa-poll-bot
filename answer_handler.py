import questions_container
def handle_answer(answer,question_id):
    #last question
    if (len(questions_container.questions) - 1 <= question_id):
        return "Ты уже закончил тест|-1"
    
    possible_answers = questions_container.answers[question_id]
    possible_emotions = questions_container.emotions[question_id];
    print("possible answers:", possible_answers)

    # incorrect answer
    if answer not in possible_answers:
        return "Выбирай номрально😡|-1";

    # question don't have possible emotions
    if (len(possible_emotions) == 0):
        return ""

    # find and return emotion
    for i in range(len(possible_answers)):
        if (answer == possible_answers[i]):
            return possible_emotions[i]

    return "";