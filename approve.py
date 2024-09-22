import main as m


def approve() -> None:
    knowledge_base: dict = m.load_knowledge_base("knowledgeBase.json")
    approve_base: dict = m.load_knowledge_base("approve.json")

    for entry in approve_base["questions"]:
        print(f'Question {entry["question"]}')
        print(f'Answer: {entry["answer"]}')
        answer: str = input("Is the answer correct? y/n ")
        if answer.lower() == "y":
            knowledge_base["questions"].append({"question": entry["question"], "answer": entry["answer"]})
            m.save_knowledge("knowledgeBase.json", knowledge_base)

    approve_base["questions"].clear()
    m.save_knowledge("approve.json", approve_base)


if __name__ == '__main__':
    approve()
