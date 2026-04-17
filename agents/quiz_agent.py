from utils.llm import get_llm

def generate_quiz(topic, total_questions):
    llm = get_llm()
    all_questions = []

    batch_size = 10  # generate 10 at a time

    for i in range(0, total_questions, batch_size):
        prompt = f"""
        Generate {batch_size} MCQ questions on {topic}.

        STRICT FORMAT:

        Q1: Question
        A) Option
        B) Option
        C) Option
        D) Option
        Answer: Correct option

        Q2: Question
        A) Option
        B) Option
        C) Option
        D) Option
        Answer: Correct option

        IMPORTANT:
        - Answer must be on a NEW LINE
        - Do NOT mix answer with options
        - Each question should follow the exact format
        - Do not repeat questions
        """

        response = llm.invoke(prompt).content
        all_questions.append(response)

    return "\n\n".join(all_questions)