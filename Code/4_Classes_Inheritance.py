from __future__ import annotations
from typing import Any, Dict, Generic, List, TypeVar
import time


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
    

    def __str__(self) -> str:
        string: str = f"Company\n"
        string += f"  Name: {self.name}\n"
        string += f"  Salery: {self.given_salery}\n"
        return string
    
    



class WebshopCompany(Company):
    def __init__(self, name: str, salery: float, products: List[str]):
        super().__init__(name, salery)
        self._products = products


    @property
    def products(self) -> List[str]:
        return self._products
    

    def __str__(self) -> str:
        string = super().__str__()
        string += f"  Products: {self.products}\n"
        return string
    

    
webshop = WebshopCompany("New Company", 20000, ["Shirt", "Pants", "NFTs"])
print(webshop)
print(webshop.products)

Company("Test Company", 42)
print(webshop.total_nr_of_created_companies())



T = TypeVar("T")
class FirstInFirstOut(Generic[T]):
    def __init__(self):
        self._element_list: List[T] = []

    
    def __len__(self) -> int:
        return len(self._element_list)
    

    def add(self, element: T) -> None:
        self._element_list += [element]

    
    def get(self) -> T:
        if len(self) == 0:
            return None
        first_element: T = self._element_list[0]
        self._element_list = self._element_list[1:]
        return first_element
    



queue_in_tivoli = FirstInFirstOut[Person]()

print(f"N Persons in queye: {len(queue_in_tivoli)}")

queue_in_tivoli.add(Person("Mathias", "Grønne", 29))
queue_in_tivoli.add(Person("Tobias", "Nielsen", 35))

print(f"N Persons in queye: {len(queue_in_tivoli)}")

next_person_in_queue = queue_in_tivoli.get()
print(next_person_in_queue)

print(f"N Persons in queye: {len(queue_in_tivoli)}")

print(queue_in_tivoli.get())
print(queue_in_tivoli.get())




class PersonFIFO(FirstInFirstOut[Person]):
    def __init__(self):
        pass

person_queue_in_tivoli = PersonFIFO()
person_queue_in_tivoli.get()