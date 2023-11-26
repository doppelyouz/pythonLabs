class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn


book1 = Book("1984", "George Orwell", "1234567890")
book2 = Book("Brave New World", "Aldous Huxley", "0987654321")
print(f"Title: {book1.title}, Author: {book1.author}, ISBN: {book1.isbn}")
print(f"Title: {book2.title}, Author: {book2.author}, ISBN: {book2.isbn}")


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_car(self):
        return f"{self.year} {self.make} {self.model}"


class Car:
    def __init__(self, make, model, year, color, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage

    def display_car(self):
        return f"{self.year} {self.make} {self.model}, Color: {self.color}, Mileage: {self.mileage}"

    def drive(self, km):
        self.mileage += km
        print(f"New mileage: {self.mileage}")


class ElectricCar(Car):
    def __init__(self, make, model, year, color, mileage, battery_size):
        super().__init__(make, model, year, color, mileage)
        self.battery_size = battery_size

    def describe_battery(self):
        return f"Battery size: {self.battery_size}"


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, name, quantity, description):
        self.items.append(
            {"name": name, "quantity": quantity, "description": description}
        )

    def display_inventory(self):
        for item in self.items:
            print(
                f"Name: {item['name']}, Quantity: {item['quantity']}, Description: {item['description']}"
            )

    def change_quantity(self, name, quantity):
        for item in self.items:
            if item["name"] == name:
                item["quantity"] = quantity
                break


inventory = Inventory()
inventory.add_item("Apples", 50, "Fresh green apples")
inventory.add_item("Oranges", 30, "Sweet oranges")
inventory.display_inventory()
inventory.change_quantity("Apples", 45)
inventory.display_inventory()
