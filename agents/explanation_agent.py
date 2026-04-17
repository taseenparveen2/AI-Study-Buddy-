from utils.llm import get_llm

def explain(query, context):
    llm = get_llm()

    prompt = f"""
    Explain the following topic in simple terms:
    
    Question: {query}
    Context: {context}
    """

    return llm.invoke(prompt).content