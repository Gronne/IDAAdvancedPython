

from typing import List


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
    


print(f"Nr. of companies: {Company.total_nr_of_created_companies()}")

company_a = Company(name="Nice Company Aps", salery=45000)
print(f"Nr. of companies: {Company.total_nr_of_created_companies()}")

company_b = Company(name="Nice Company Aps", salery=25000)
print(f"Nr. of companies: {Company.total_nr_of_created_companies()}")

print(f"Company A Id: {company_a.company_id}")

person_a = Person("Mathias", "Grønne", 29)
print(person_a.balance)

company_a.hire(person_a)
company_a.pay_salery()

print(person_a.balance)

