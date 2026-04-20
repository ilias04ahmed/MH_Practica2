import numpy as np
import pandas as pd
import random

def generar_instancia(n_exams=200, n_students=4000, n_rooms=20, n_slots=100, seed=42):
    random.seed(seed)
    np.random.seed(seed)

    student_exam = []
    for s in range(n_students):
        k = random.randint(3, 6)
        exams = np.random.choice(n_exams, size=k, replace=False)
        for e in exams:
            student_exam.append([s, e])

    student_exam = pd.DataFrame(student_exam, columns=["student", "exam"])
    exam_students = student_exam.groupby("exam").size()

    capacities = np.random.randint(30, 200, size=n_rooms)
    rooms = pd.DataFrame({
        "room": range(n_rooms),
        "capacity": capacities
    })

    exams = pd.DataFrame({
        "exam": exam_students.index,
        "n_students": exam_students.values
    })

    return student_exam, exams, rooms, n_slots