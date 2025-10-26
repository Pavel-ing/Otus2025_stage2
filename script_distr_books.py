import json
from csv import DictReader


def distribution_of_books():
    with open("users.json", "r") as f:
        users = json.loads(f.read())
        users_list = []
        for user in users:
            users_list.append({
                "name": user["name"],
                "gender": user["gender"],
                "address": user["address"],
                "age": user["age"],
                "books": [],
            })

    with open("books.csv", newline="") as f:
        books = []
        for row in DictReader(f):
            books.append({
                "title": row["Title"],
                "author": row["Author"],
                "pages": int(row["Pages"]),
                "genre": row["Genre"]
            })

    b, u = 0, 0
    while b < len(books):
        if u < len(users_list):
            users_list[u]["books"].append(books[b])
            u += 1
        else:
            u = 0
        b += 1

    with open("result.json", "w") as final_result:
        final_result.write(json.dumps(users_list, indent=4))


distribution_of_books()
