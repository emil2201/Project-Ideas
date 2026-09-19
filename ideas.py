def show_ideas(ideas):
    for i, idea in enumerate(ideas, start=1):
        print(f"{i}. {idea['name']}  Тема: {idea['topic']}  Сложность: {idea['difficulty']}")

def add_idea(ideas, name, topic, difficulty):
    new_idea = {
        "name": name,
        "topic": topic,
        "difficulty": difficulty
    }
    ideas.append(new_idea)
