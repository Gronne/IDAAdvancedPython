from __future__ import annotations
from typing import Dict, List
import time


class TimeDecorator:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        """
        Descriptor method to ensure the function is bound to the instance.
        This allows `self` to be passed automatically.
        """
        return lambda *args, **kwargs: self(instance, *args, **kwargs)

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        print(f"Time: {end_time - start_time:.4f} seconds")
        return result
    


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)  # Pass all arguments to the wrapped function
        end_time = time.time()
        print(f"Time: {end_time - start_time:.4f} seconds")
        return result
    return wrapper



class Person:

    def __init__(self, first_name: str, last_name: str, age: int = 25):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self._balance: float = 0.0


    @property
    def full_name(self) -> str:
        '''
        Get the person's full name
        '''
        return f"{self.first_name} {self.last_name}"


    @property
    def balance(self) -> float:
        '''
        Get how much money the person got in the bank
        '''
        return self._balance
    

    @TimeDecorator
    def spend_money(self, amount: float) -> None:
        '''
        The person used this amount of money
        '''
        if amount > 0:
            self._balance -= amount


    def give_salery(self, amount: float) -> None:
        '''
        The Person recieved the given amount of salery
        '''
        if amount > 0:
            self._balance += amount 

    
    @property
    def is_adult(self) -> bool:
        '''
        Check if the person is an adult
        '''
        return self.age > 0
    

    @property
    def info_as_string(self) -> str:
        '''
        Get info as a string
        '''
        string: str = f"Person\n"
        string += f"  Name: {self.full_name}\n"
        string += f"  Age: {self.age}\n"
        string += f"  Balance: {self.balance}\n"
        return string
    

    def __str__(self) -> str:
        return self.info_as_string
    

    def __eq__(self, ref_person: Person) -> bool:
        return self.full_name == ref_person.full_name and self.age == ref_person.age
    

    def __gt__(self, ref_person: Person) -> bool:
        return self.age > ref_person.age
    

    def __hash__(self) -> hash:
        return hash(self.full_name)
    




class Company:
    _nr_of_companies_created: int = 0

    def __init__(self, name: str, salery: float):
        self.name = name
        self._salery = salery

        self._persons_in_company: List[Person] = []

        Company._nr_of_companies_created += 1
        self._company_id: int = Company._nr_of_companies_created


    @property
    def company_id(self) -> int:
        return self._company_id


    @property
    def given_salery(self) -> float:
        return self._salery
    

    def hire(self, person: Person) -> None:
        '''
        Hire a person to the company
        '''
        self._persons_in_company += [person]

    
    def pay_salery(self) -> None:
        '''
        Pay salery to personnel
        '''
        for person in self._persons_in_company:
            person.give_salery(self._salery)


    @staticmethod
    def total_nr_of_created_companies() -> int:
        return Company._nr_of_companies_created
    

    def __len__(self) -> int:
        return len(self._persons_in_company)
    

    def __hash__(self) -> hash:
        return hash(self.company_id)
    


person_a = Person(
    first_name="Mathias",
    last_name="Grønne",
    age=29
)

print(person_a)


person_b = Person(
    first_name="Tobias",
    last_name="Nielsen",
    age=35
)

print(person_a == person_a)
print(person_a == person_b)
print(person_a > person_b)
print(person_a < person_b)


company_a = Company(name="Nice Company Aps", salery=45000)
company_a.hire(person_a)
company_a.hire(person_b)

print(f"Nr. of persons hired: {len(company_a)}")

person_to_age: Dict[Person, int] = {}
person_to_age[person_a] = person_a.age

print(person_to_age[person_a])


person_a.spend_money(50)
person_a.spend_money(-50)



class AddMoreEachTime:
    def __init__(self, adder: int):
        self._adder: int = adder
        self._call_counter: int = 0

    def __call__(self, number:float) -> float:
        self._call_counter += 1
        return number + (self._adder*self._call_counter)
    

adder_10 = AddMoreEachTime(10)

print(adder_10(0))
print(adder_10(0))
print(adder_10(0))
print(adder_10(0))
print(adder_10(0))


