import sqlite3

connect = sqlite3.connect ("answers.db")

kursor = connect.cursor ()

# kursor.execute ("""DROP TABLE IF EXISTS que""")
# kursor.execute ("""DROP TABLE IF EXISTS zwjazok""")
# kursor.execute ("""DROP TABLE IF EXISTS qui""")

kursor.execute ("""CREATE TABLE IF NOT EXISTS que (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    que TEXT NOT NULL,
    right_answer TEXT NOT NULL,
    wrong_answer1 TEXT NOT NULL,
    wrong_answer2 TEXT NOT NULL,
    wrong_answer3 TEXT NOT NULL
)
""")

kursor.execute ("""CREATE TABLE IF NOT EXISTS qui (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    years_old_from INTEGER NOT NULL,
    years_old_to INTEGER NOT NULL
)
""")

kursor.execute ("""CREATE TABLE IF NOT EXISTS zwjazok (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    que INTEGER NOT NULL,
    qui INTEGER TEXT NOT NULL,
    FOREIGN KEY (que) REFERENCES que(id),
    FOREIGN KEY (qui) REFERENCES qui(id)
)
""")

category = (
    ("Укр. мова", 10, 13),
    ("Природничі науки", 10, 20),
    ("Факти", 9, 50),
    ("Основи здоров'я", 4, 14),
    ("Математика", 10, 13)
)

category_add = ("""INSERT INTO qui (name, years_old_from, years_old_to)
    VALUES (?, ?, ?)
""")

zwjazok_add = ("""INSERT INTO zwjazok (que, qui)
    VALUES (?, ?)
""")

answers1 = (("Яке найбрудніше місто в Україні?", "Київ", "Одеса", "Запоріжжя", "Львів"),
    ("Скільки буде 3³", "27", "9", "6", "99"),
    ("Яким членом речення виражається звертання?", "Воно не є членом речення", "Підмет", "Означення", "Додаток"),
    ("Скільки годин на добу рослини фотосинтезуються?", "7 год.", "12 год.", "24 год.", "Вони фотосинтезуються увесь час, поки є світло"),
    ("Який заповідник в Україні найбільший?", "Аскания-Нова", "Канівський заповідник", "Карпатський заповідник", "Ґорґани"),
    ("Які з цього переліку є легкозаймистими речовинами?", "Папір", "Залізо", "Тканина", "Дерево"),
    ("Скільки всього областей в Україні (з автономною республікою Крим)?", "25", "20", "24", "40"),
    ("Що таке віла?", "Степова русалка", "Роскішний будинок за містом", "Знаряддя праці", "Прилад для їжі"),
    ("Який літак виготовлено в Україні?", "Мрія", "Антей", "Військово-Транспортний літак Ан-12", "Пасажирський літак Ан-24"),
    ("Який це зв'язок словосполучення?\nвстати зі стільця.", "Керування", "Узгодження", "Прилягання", "Це не словосполучення"),
    ("Одна з природничих наук.", "Хімія", "Математика", "Істоія", "Українська література")
)

#choice = int(input("Оберіть вікторину яку ви, хотіли би пройти:\n>>>"))
# kursor.execute("""
#     SELECT
#     que.que,
#     que.right_answer,
#     que.wrong_answer1,
#     que.wrong_answer2,
#     que.wrong_answer3
#     FROM zwjazok, que
#     WHERE zwjazok.qui == (?)
#     AND que.id == zwjazok.id
# """, [3])
# data = kursor.fetchall()
# print(data)

# kursor.execute ("""INSERT INTO que (que, right_answer, wrong_answer1, wrong_answer2, wrong_answer3)
#     VALUES ("Скільки буде 3³", "27", "9", "6", "99")
# """)

zapyt = ("""INSERT INTO que (que, right_answer, wrong_answer1, wrong_answer2, wrong_answer3)
    VALUES (?, ?, ?, ?, ?)
""")

# kursor.executemany (zapyt, answers1)

# kursor.executemany (category_add, category)

# kursor.execute ("""SELECT * FROM que WHERE id = 1 ORDER BY que""")

# kursor.execute ("""SELECT * FROM zwjazok""")

# data = kursor.fetchall ()

# for i in data:
#     print (i)

# kursor.execute ("""SELECT * FROM qui""")

# data = kursor.fetchall ()

# for i in data:
#     print (i)

# for args in zip (range (1, 12), (3, 5, 1, 2, 3, 4, 3, 3, 3, 1, 2)):
#     kursor.execute (zwjazok_add, list(args))

# kursor.execute ("""SELECT * FROM que""")

# data = kursor.fetchall ()

# for i in data:
#     print (i)

def get_all (quis_id):
    kursor.execute ("""SELECT * FROM que
    WHERE id quiz = (?)
    """, [quis_id])
    ids = kursor.fetchall ()
    print (ids)

get_all (1)

connect.commit ()

kursor.close ()
connect.close ()