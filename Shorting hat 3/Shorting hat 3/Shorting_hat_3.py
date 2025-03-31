import tkinter as tk
import random

# Kérdések definíciója
questions = [
    {
        "question": "Do you like Dawn or Dusk?",
        "answers": {
            "Dawn": {"gryffindor": 1, "ravenclaw": 1},
            "Dusk": {"hufflepuff": 1, "slytherin": 1}
        }
    },
    {
        "question": "When I am dead, I want people to remember me as:",
        "answers": {
            "The Good": {"hufflepuff": 2},
            "The Great": {"slytherin": 2},
            "The Wise": {"ravenclaw": 2},
            "The Bold": {"gryffindor": 2}
        }
    },
    {
        "question": "Which kind of instrument most pleases your ear?",
        "answers": {
            "The violin": {"slytherin": 4},
            "The trumpet": {"hufflepuff": 4},
            "The piano": {"ravenclaw": 4},
            "The drum": {"gryffindor": 4}
        }
    }
]

# Házpontok
scores = {"gryffindor": 0, "ravenclaw": 0, "hufflepuff": 0, "slytherin": 0}

# Keverjük a kérdések sorrendjét
random.shuffle(questions)

# Alap GUI beállítás
current_question = 0

root = tk.Tk()
root.geometry("600x400")
root.eval('tk::PlaceWindow . center')
root.configure(bg="#1e1e2e")  # Sötét varázslós háttér
root.title("Sorting Hat Quiz")

question_label = tk.Label(
    root,
    text="",
    font=("Georgia", 18, "bold"),
    fg="#ffdd00",       # Arany betű
    bg="#1e1e2e",       # Háttér egyezzen
    wraplength=500
)
question_label.pack(pady=20)

button_frame = tk.Frame(root, bg="#1e1e2e")
button_frame.pack()

result_label = tk.Label(
    root,
    text="",
    font=("Times New Roman", 20, "italic"),
    fg="#50fa7b",
    bg="#1e1e2e"
)
result_label.pack(pady=20)

def answer_clicked(answer):
    global current_question
    house_points = questions[current_question]["answers"][answer]
    for house, point in house_points.items():
        scores[house] += point

    current_question += 1
    if current_question < len(questions):
        show_question()
    else:
        show_result()

def show_question():
    for widget in button_frame.winfo_children():
        widget.destroy()

    q = questions[current_question]
    question_label.config(text=q["question"])
    
    for answer_text in q["answers"]:
        btn = tk.Button(
    button_frame,
    text=answer_text,
    font=("Georgia", 14),
    width=30,
    height=2,
    bg="#44475a",
    fg="#f8f8f2",
    activebackground="#6272a4",
    relief="raised",
    command=lambda a=answer_text: answer_clicked(a)
)
        btn.pack(pady=5)


def show_result():
    for widget in button_frame.winfo_children():
        widget.destroy()

    max_points = max(scores.values())
    top_houses = [house for house, points in scores.items() if points == max_points]
    chosen_house = random.choice(top_houses)  # döntetlen esetén véletlenszerű

    emojis = {
        "gryffindor": "🦁",
        "ravenclaw": "🦅",
        "hufflepuff": "🦡",
        "slytherin": "🐍"
    }

    result_text = f"The Sorting Hat has decided...\nYou are in {chosen_house.capitalize()}! {emojis[chosen_house]}"
    result_label.config(text=result_text)

# Indító kérdés
show_question()
root.mainloop()

