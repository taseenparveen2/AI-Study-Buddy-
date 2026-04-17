from utils.llm import get_llm

def summarize(text):
    llm = get_llm()

    prompt = f"Summarize this:\n{text}"

    return llm.invoke(prompt).content