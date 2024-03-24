fake_db = [
    {
        "email": "someemail@gmail.com", 
        "firstName": "Иван", 
        "secondName": "Иванович", 
        "lastName": "Иванов"
    },
    {
        "email": "serpetr@gmail.com", 
        "firstName": "Пётр", 
        "secondName": "Сергеев", 
        "lastName": "Павлович"
    },
    {
        "email": "almosh@gmail.com", 
        "firstName": "Александр", 
        "secondName": "Мошников", 
        "lastName": "Петрович"
    },
    {
        "email": "kravulya@gmail.com", 
        "firstName": "Юлия", 
        "secondName": "Кравченко", 
        "lastName": "Дмитриевна"
    },
    {
        "email": "dimon@gmail.com", 
        "firstName": "Дмитрий", 
        "secondName": "Михайлов", 
        "lastName": "Сергеевич"
    },
    {
        "email": "memeamam@gmail.com", 
        "firstName": "Олег", 
        "secondName": "Смешной", 
        "lastName": None
    },

    {
        "email": "petrivanov@gmail.com", 
        "firstName": "Пётр", 
        "secondName": "Васильевич", 
        "lastName": "Иванов"
    },
]


def get_users_from_db():
    users_from_db = fake_db.copy()
    return users_from_db

def get_full_name_and_email(user):
    return " ".join([value for key, value in  user.items() if value is not None and key in ["firstName", "secondName", "lastName", "email"]])

def word_in_user(fullNameAndEmail, word):
    return word.lower().replace("ё","е") in fullNameAndEmail.lower().replace("ё","е")

def filter_users(inputString):
    users = get_users_from_db()
    splitted_input = inputString.split(" ")
    filtered_users = []
    for user in users:
        passing_flag = True
        fullNameAndEmail = get_full_name_and_email(user)
        for word in splitted_input:
            if not word_in_user(fullNameAndEmail, word):
                passing_flag = False
                break
        if passing_flag:
            filtered_users.append(user)
    return filtered_users


example_inputs = [
    "Иванов Петр Васильевич", 
    "Петр Васильевич Иванов", 
    "Петр Иванов", 
    "Иванов Петр",
    "Ивано"
]

for example in example_inputs:
    print (f"По запросу : '{example}' фильтр вернёт")
    print(filter_users(example))
filter_users("Иванов Петр Васильевич")