from rules import check_rules
from llm import ask_llm

print("================================")
print(" HYBRID AI CHATBOT ")
print("================================")

while True:

    user = input("You: ")

    clean_input = user.lower().strip()

    if clean_input in ["exit", "quit", "bye"]:
        print("Bot: Goodbye!")
        break

    # Rule Engine First
    rule_response = check_rules(clean_input)

    if rule_response:
        print("Bot:", rule_response)

    else:
        print("Bot:", ask_llm(user))