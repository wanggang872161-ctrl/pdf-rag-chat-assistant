def retrieve_answer(db, llm, question):

    docs = db.similarity_search(question, k=3)

    context = "\n\n".join([d.page_content for d in docs])

    answer = llm(context, question)

    return answer