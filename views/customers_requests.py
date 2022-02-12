import sqlite3
import json
from models import Customer

CUSTOMERS = [
    {
        "id": 2,
        "name": "Jordan Nelson",
        "email": "jordan@nelson.com",
        "employee": True
    },
    {
        "id": 3,
        "name": "Zoe LeBlanc",
        "email": "zoe@leblanc.com",
        "employee": True
    },
    {
        "name": "Meg Ducharme",
        "email": "meg@ducharme.com",
        "id": 4,
        "employee": True
    },
    {
        "name": "Hannah Hall",
        "email": "hannah@hall.com",
        "id": 5,
        "employee": True
    },
    {
        "name": "Emily Lemmon",
        "email": "emily@lemmon.com",
        "id": 6,
        "employee": True
    },
    {
        "name": "Jordan Castelloe",
        "email": "jordan@castelloe.com",
        "id": 7,
        "employee": True
    },
    {
        "name": "Leah Gwin",
        "email": "leah@gwin.com",
        "id": 8,
        "employee": True
    },
    {
        "name": "Caitlin Stein",
        "email": "caitlin@stein.com",
        "id": 9,
        "employee": True
    },
    {
        "name": "Greg Korte",
        "email": "greg@korte.com",
        "id": 10,
        "employee": True
    },
    {
        "name": "Charisse Lambert",
        "email": "charisse@lambert.com",
        "id": 11,
        "employee": True
    },
    {
        "name": "Madi Peper",
        "email": "madi@peper.com",
        "id": 12,
        "employee": True
    },
    {
        "name": "Jenna Solis",
        "email": "jenna@solis.com",
        "id": 14,
        "employee": True
    },
    {
        "id": 15,
        "name": "Ryan Tanay",
        "email": "ryan@tanay.com",
        "employee": False
    },
    {
        "id": 16,
        "name": "Emma Beaton",
        "email": "emma@beaton.com",
        "employee": False
    },
    {
        "id": 17,
        "name": "Dani Adkins",
        "email": "dani.adkins.com",
        "employee": False
    },
    {
        "id": 18,
        "name": "Adam Oswalt",
        "email": "adam@oswalt.com",
        "employee": False
    },
    {
        "id": 19,
        "name": "Fletcher Bangs",
        "email": "flangs@bangs.com",
        "employee": False
    },
    {
        "id": 20,
        "name": "Angela Lee",
        "email": "lee@lee.com",
        "employee": False
    },
    {
        "name": "mike mike",
        "email": "m@m.com",
        "employee": False,
        "id": 21
    },
    {
        "name": "Eric \"Macho Man\" Taylor",
        "email": "macho@man.com",
        "employee": True,
        "id": 22
    },
    {
        "name": "jake f",
        "email": "jake@gmail.com",
        "employee": False,
        "id": 23
    },
    {
        "name": "Jacob  Folley",
        "email": "jacob@gmail.com",
        "employee": True,
        "id": 24
    },
    {
        "name": "jake Folley",
        "email": "jake@gmail.com",
        "employee": False,
        "id": 25
    }
]


def create_customer(customer):
    # Get the id value of the last customer in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    customer["id"] = new_id

    # Add the customer dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer


def get_all_customers():
    return CUSTOMERS

    # Function with a single parameter


def get_single_customer(id):
    # Variable to hold the found customer, if it exists
    requested_customer = None

    # Iterate the CUSTOMERS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer


def get_customers_by_email(email):

    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        from Customer c
        WHERE c.email = ?
        """, ( email, ))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['id'], row['name'], row['address'], row['email'] , row['password'])
            customers.append(customer.__dict__)

    return json.dumps(customers)
