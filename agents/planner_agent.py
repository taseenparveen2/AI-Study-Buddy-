def decide_task(user_input):
    if "quiz" in user_input:
        return "quiz"
    elif "summary" in user_input:
        return "summary"
    elif "doubt" in user_input:
        return "doubt"
    else:
        return "explain"