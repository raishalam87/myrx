from typing import List
from datetime import date

# Define an Address class (assuming it's a simple structure)
class Address:
    def __init__(self, street: str, city: str, postal_code: str):
        self._street = street
        self._city = city
        self._postal_code = postal_code

    @property
    def street(self):
        return self._street

    @property
    def city(self):
        return self._city

    @property
    def postal_code(self):
        return self._postal_code

    def __repr__(self):
        return f"Address(street={self._street}, city={self._city}, postal_code={self._postal_code})"

# Define the ImmutableEmployee class
class ImmutableEmployee:
    def __init__(self, name: str, id_: str, date_of_joining: date, addresses: List[Address]):
        self._name = name
        self._id = id_
        self._date_of_joining = date_of_joining
        # Store a copy of the list to prevent external modification
        self._addresses = list(addresses)

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @property
    def date_of_joining(self):
        return self._date_of_joining

    @property
    def addresses(self):
        # Return a copy of the list to prevent external modification
        return list(self._addresses)

    def __repr__(self):
        return f"ImmutableEmployee(name={self._name}, id={self._id}, date_of_joining={self._date_of_joining}, addresses={self._addresses})"

# Example Usage
address1 = Address("123 Main St", "New York", "10001")
address2 = Address("456 Elm St", "San Francisco", "94102")

employee = ImmutableEmployee("John Doe", "E12345", date(2020, 5, 15), [address1, address2])

print(employee)
print(employee.addresses)

# Attempting to modify the object's attributes will raise an error:
# employee.name = "Jane Doe"  # This will raise an AttributeError
# employee.addresses.append(Address("789 Pine St", "Los Angeles", "90001"))  # This will not change the original list