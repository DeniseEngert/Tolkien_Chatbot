import json


def load_json(filepath: str) -> dict:
    with open(filepath, 'r') as file:
        data: dict = json.load(file)
    return data

def save_knowledge(filepath: str, data: dict):
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=2)

def approve() -> None:
    knowledge_base: dict = load_json("knowledgeBase.json")
    approve_base: dict = load_json("approve.json")

    for entry in approve_base["questions"]:
        print(f'Question {entry["question"]}')
        print(f'Answer: {entry["answer"]}')
        answer: str = input("Is the answer correct? y/n ")
        if answer.lower() == "y":
            knowledge_base["questions"].append({"question": entry["question"], "answer": entry["answer"]})
            save_knowledge("knowledgeBase.json", knowledge_base)

    approve_base["questions"].clear()
    save_knowledge("approve.json", approve_base)


if __name__ == '__main__':
    approve()