from ideas import show_ideas, add_idea

ideas = [
    {
        "name": "Трекер привычек",
        "topic": "Консольное приложение",
        "difficulty": "Средняя"
    },
    {
        "name": "Космическая викторина",
        "topic": "Игра",
        "difficulty": "Лёгкая"
    },
    {
        "name": "Планировщик задач",
        "topic": "Организация времени",
        "difficulty": "Средняя"
    }
]

print("===")
print("Программирование на Python")
print("Каталог идей для Python-проектов")
print("===")

show_ideas(ideas)

answer = input("Добавить новую идею? ")

if answer.lower() == "да":
    name = input("Название: ")
    topic = input("Тема: ")
    difficulty = input("Сложность: ")
    add_idea(ideas, name, topic, difficulty)
    print("Идея добавлена!")
    print("=== Каталог идей для Python-проектов ===")
    show_ideas(ideas)
