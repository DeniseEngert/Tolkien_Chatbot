import json
from difflib import get_close_matches


def load_knowledge_base(filepath: str) -> dict:
    with open(filepath, 'r') as file:
        data: dict = json.load(file)
    return data


def save_knowledge(filepath: str, data: dict):
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=2)


def find_best_match(userQuestion: str, question: list[str]) -> str | None:
    matches: list = get_close_matches(userQuestion, question, n=2, cutoff=0.8)
    return matches[0] if matches else None


def get_answer(question: str, knowledgeBase: dict) -> str | None:
    for q in knowledgeBase["questions"]:
        if q["question"] == question:
            return q["answer"]


def chat_bot():
    knowledge_base: dict = load_knowledge_base("knowledgeBase.json")
    approve: dict = load_knowledge_base("approve.json")

    file = open('resources/banner_big.txt', 'r')
    banner = file.read()
    print(banner)
    print("Note: write 'quit' to close chatbot")
    print()

    while True:
        user_input: str = input("You: ")
        if user_input.lower() == "quit":
            break

        best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])
        if best_match:
            answer: str = get_answer(best_match, knowledge_base)
            print(f'Bot: {answer}')
        else:
            print("Bot: I don't know the answer, can you teach me?")
            new_answer: str = input("You: Type the answer or 'skip' to skip. ")
            if new_answer.lower() != "skip":
                approve["questions"].append({"question": user_input, "answer": new_answer})
                save_knowledge("approve.json", approve)
                print("Bot: Thank you, I learned a new response.")


if __name__ == '__main__':
    chat_bot()
