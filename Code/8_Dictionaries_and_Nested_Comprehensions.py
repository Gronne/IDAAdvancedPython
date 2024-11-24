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




person_list: List[Person] = [
    Person("Mathias", "Grønne", 29),
    Person("Tobias", "Nielsen", 35),
    Person("Rasmus", "Pedersen", 24),
    Person("Frank", "Olesen", 32)
]


name_to_age: Dict[str, int] = {
    person_list[0].full_name: person_list[0].age,
    person_list[1].full_name: person_list[1].age,
    person_list[2].full_name: person_list[2].age,
    person_list[3].full_name: person_list[3].age,
}

name_to_age_a: Dict[str, int] = { person.full_name: person.age for person in person_list if person.age > 30 }
print(name_to_age_a)

allowed_names: List[str] = ["Mathias", "Tobias"]

name_to_age_b: Dict[str, int] = { person.full_name: person.age for person in person_list if person.first_name in allowed_names }
print(name_to_age_b)

name_to_age_c: Dict[str, int] = { person.full_name: person.age for person in person_list if person.first_name in allowed_names and person.age > 30 }
print(name_to_age_c)

name_to_age_d: Dict[str, int] = { person.full_name: person.age for person in person_list if  34 > person.age > 25 }
print(name_to_age_d)


person_list[0].set_job(CEO())
person_list[1].set_job(Programmer())
person_list[2].set_job(Programmer())

name_to_age_e: Dict[str, int] = { person.full_name: person.age for person in person_list if isinstance(person.job_type, Programmer) }
print(name_to_age_e)

name_to_age_f: Dict[str, int] = { person.full_name: person.age for person in person_list if isinstance(person.job_type, Unemployed) }
print(name_to_age_f)

print("-----------------")

for index, (name, age) in enumerate(name_to_age.items()):
    print(f"({index}) {name}: {age}")


oldest_name_age = max(name_to_age.items(), key=lambda name_age: name_age[1])
print(oldest_name_age)

print("-----------------")

webshop_a = WebshopCompany("Company A", ["Pant", "Shirt"])
webshop_b = WebshopCompany("Company B", ["Dog", "Cat"])
webshop_c = WebshopCompany("Company C", ["Red", "Blue"])
webshop_d = WebshopCompany("Company D", ["Python", "C++"])
webshop_e = WebshopCompany("Company E", [])

webshop_a.hire(person_list[0], CEO)
webshop_a.hire(person_list[1], Programmer)
webshop_b.hire(person_list[2], CEO)
webshop_d.hire(person_list[1], Programmer)

webshop_list: List[WebshopCompany] = [webshop_a, webshop_b, webshop_c, webshop_d, webshop_e]

webshop_filtered_list = [webshop for webshop in webshop_list if webshop.products]
for webshop in webshop_filtered_list:
    print(webshop.name)
    
print("-----------------")


all_company_products: List[str] = [webshop.products for webshop in webshop_list]
print(all_company_products)

all_company_products: List[str] = [product for webshop in webshop_list for product in webshop.products]
print(all_company_products)

all_company_products: List[str] = [product for webshop in webshop_list for product in webshop.products if len(webshop)]
print(all_company_products)










