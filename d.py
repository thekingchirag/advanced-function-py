# 1. Zip books and counts
books = ["Harry potter", "Gradma's Lost Story", "Constitution of India"]
counts = [2, 0, 4]

inventory = list(zip(books, counts))


# 2. Filter available books
print("Available:")
for book, count in inventory:
    if count > 0:
        print(book)


# 3. Update fees using map
fees = [150,105,300]

def add_one(fee):
    return fee + 1

new_fees = list(map(add_one, fees))
print("New Fees:", new_fees)


# 4. Stop early if count is 0
search = "Gradma's Lost Story"

for book, count in inventory:
    if book == search and count == 0:
        print(search, "is unavailable. Stopping!")
        break