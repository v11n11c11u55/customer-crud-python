import json
from pathlib import Path

FOLDER = Path(__file__).parent
FILE = FOLDER / "customers.json"


def load_customers():
    if FILE.exists():
        # UTF-8 encoding allows special characters to be stored correctly.
        with open(FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return []


def save_customers(customers):
    with open(FILE, "w", encoding="utf-8") as file:
        json.dump(customers, file, indent=4, ensure_ascii=False)


customers = load_customers()

print("===== CUSTOMER LIST =====")

while True:

    print("\n[1] ADD")
    print("[2] VIEW")
    print("[3] DELETE")
    print("[4] EXIT")

    option = input("\nSelect an option: ")

    match option:

        case "1":

            new_id = max((customer["id"] for customer in customers), default=0) + 1

            name = input("Name: ")

            while True:
                try:
                    age = int(input("Age: "))
                    break
                except ValueError:
                    print("PLEASE ENTER NUMBERS ONLY!")

            product = input("Product: ")

            customers.append(
                {
                    "id": new_id,
                    "name": name,
                    "age": age,
                    "product": product,
                }
            )

            save_customers(customers)

            print("\nCustomer added successfully!")

        case "2":

            if not customers:
                print("\nNo customers registered.")
            else:

                print()

                for customer in customers:
                    print(f"ID: {customer['id']}")
                    print(f"NAME: {customer['name'].upper()}")
                    print(f"AGE: {customer['age']}")
                    print(f"PRODUCT: {customer['product'].title()}")
                    print("-" * 30)

        case "3":

            name = input("Customer full name: ").upper()

            for index, customer in enumerate(customers):

                if customer["name"].upper() == name:

                    del customers[index]
                    save_customers(customers)

                    print("Customer removed successfully!")
                    break

            else:
                print("Customer not found.")

        case "4":

            print("System closed.")
            break

        case _:

            print("Invalid option.")
