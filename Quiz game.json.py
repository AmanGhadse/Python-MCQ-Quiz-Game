import json

with open('questions.json') as f:
    questions = json.load(f)

score = 0

for q in questions:
    print(q['question'])

    for i, option in enumerate(q['options']):
        print(f"{chr(97 + i)}) {option}")

    answer = input("Your answer (a/b/c/d): ")

    if answer == q['answer']:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {q['answer']}.")

print(f"Your score is {score}/{len(questions)}")
print("You got "+ str((score/7)*100)+" %.")

