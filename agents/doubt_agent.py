from utils.llm import get_llm

def solve_doubt(question, context):
    llm = get_llm()

    prompt = f"""
    Answer the doubt clearly:

    Question: {question}
    Context: {context}
    """

    return llm.invoke(prompt).content

