import questions_container


def handle_answer(answer,question_id):
    # if question_id > 0:
    #     question_id -= 1
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
                return "хавхваваавххавх лох|true"
            else:
                return ""

        elif question_id == 3:
            if answer == possible_answers[2]:
                return "пиздабол"
            else:
                return ""

        elif question_id == 4:
            if answer == possible_answers[1]:
                return "|true"
            else:
                return ""
        elif question_id == 6:
            if answer == possible_answers[0]:
                return "🥰"
            else:
                return "<a href='https://www.youtube.com/@zlyxa/featured'>жду тебя мой пупсик</a>"

        elif question_id == 8:
            if answer == possible_answers[0]:
                return "Респект"
            else:
                return "Позорище🤮"

        else:
            return "";
