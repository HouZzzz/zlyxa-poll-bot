import questions_container
def handle_answer(answer,question_id):
    possible_answers = questions_container.answers[question_id]
    print("possible answers:", possible_answers)

    if answer not in possible_answers:
        return "Выбирай номрально😡";
    else:
        if question_id == 0:
            return ""

        elif question_id == 1:
            if answer == possible_answers[0]:
                return "бош малявка"
            else:
                return ""

        elif question_id == 2:
            if answer == possible_answers[1]:
                return "хавхваваавххавх лох|1"
            else:
                return ""

        elif question_id == 3:
            if answer == possible_answers[2]:
                return "пиздабол"
            else:
                return ""

        elif question_id == 4:
            if answer == possible_answers[1]:
                return "|1"
            else:
                return ""
        elif question_id == 5:
            return "|1";
        elif question_id == 7:
            if answer == possible_answers[0]:
                return "🥰"
            else:
                return "<a href='https://www.youtube.com/@zlyxa/featured'>жду тебя мой пупсик</a>"

        elif question_id == 8:
            if answer == possible_answers[0]:
                return "Респект"
            else:
                return "Позорище🤮"

        elif question_id == 9:
            if answer == possible_answers[2]:
                return "<a href='https://youtu.be/CzBP3i_7KYg'>узнать</a>"
            else:
                return ""

        else:
            return "";
