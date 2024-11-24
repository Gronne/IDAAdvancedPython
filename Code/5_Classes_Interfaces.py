from __future__ import annotations
from typing import Any, Dict, Generic, List, Type, TypeVar
import time


class Person:

    def __init__(self, first_name: str, last_name: str, age: int = 25):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self._balance: float = 0.0
        self._job_type: IJob = Unemployed()


    @property
    def job_type(self) -> IJob:
        return self._job_type


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


    def set_job(self, job: IJob) -> None:
        self._job_type = job

    
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

    def __init__(self, name: str):
        self.name = name

        self._persons_in_company: List[Person] = []

        Company._nr_of_companies_created += 1
        self._company_id: int = Company._nr_of_companies_created


    @property
    def company_id(self) -> int:
        return self._company_id



    def hire(self, person: Person, job_type: Type[IJob]) -> None:
        '''
        Hire a person to the company
        '''
        person.set_job(job_type())
        self._persons_in_company += [person]

    
    def pay_salery(self) -> None:
        '''
        Pay salery to personnel
        '''
        for person in self._persons_in_company:
            person.give_salery(person.job_type.salery)


    @staticmethod
    def total_nr_of_created_companies() -> int:
        return Company._nr_of_companies_created
    

    def __len__(self) -> int:
        return len(self._persons_in_company)
    

    def __str__(self) -> str:
        string: str = f"Company\n"
        string += f"  Name: {self.name}\n"
        string += f"  Workers: {len(self)}"
        return string
    
    



class WebshopCompany(Company):
    def __init__(self, name: str, products: List[str]):
        super().__init__(name)
        self._products = products


    @property
    def products(self) -> List[str]:
        return self._products
    

    def __str__(self) -> str:
        string = super().__str__()
        string += f"  Products: {self.products}\n"
        return string



class IJob:
    def __init__(self):
        pass
    
    
    def do_work(self) -> None:
        raise NotImplementedError("do_work() not implemented")


    @property
    def salery(self) -> float:
        raise NotImplementedError("salery() not implemented")    


    

class CEO(IJob):
    def __init__(self):
        self._salery: float = 75_000

    
    @property
    def salery(self) -> float:
        return self._salery
    

    def do_work(self) -> None:
        print("Creating a strategy or something")





class Programmer(IJob):
    def __init__(self):
        self._salery: float = 45_000

    
    @property
    def salery(self) -> float:
        return self._salery
    

    def do_work(self) -> None:
        print("Making some code")




class Unemployed(IJob):
    def __init__(self):
        self._salery: float = 0

    
    @property
    def salery(self) -> float:
        return self._salery
    

    def do_work(self) -> None:
        print("Searching for work")



    
    

ceo = CEO()
print(ceo.salery)
ceo.do_work()

programmer = Programmer()
programmer.do_work()


def earns_to_most(job_a: IJob, job_b: IJob) -> IJob:
    return job_a if job_a.salery > job_b.salery else job_b

top_earner: IJob = earns_to_most(ceo, programmer)
print(type(top_earner))


webshop = WebshopCompany("webshop", ["Pant", "Shirt"])

person_a = Person("Mathias", "Grønne", 29)
webshop.hire(person_a, Programmer)

person_b = Person("Tobias", "Nielsen", 35)
webshop.hire(person_b, CEO)

print(person_a)
print(person_b)

webshop.pay_salery()

print(person_a)
print(person_b)


