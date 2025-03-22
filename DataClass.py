from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional
import json


@dataclass
class Adress():
  street : str
  city : str
  state : str
  zip_code : str
  country : str = "Pakistan"

@dataclass
class Contact():
  email : str
  phone : Optional[str] = None 

@dataclass
class Person():
  name : str
  age : int
  # Nested dataclass as a field
  adress : Adress
  # Another nested dataclass
  contact : Contact
  skills : List[str] = field(default_factory=list)
 
  def to_json(self) -> str:
    return json.dumps(asdict(self), indent=2)
  
  def add_skill(self, skill: str):
    if skill not in self.skills:
      self.skills.append(skill)
  
def hasnain():
  address = Adress("123 main st" , "Karachi" , "Sindh" , "00332")
  contact = Contact("hasnain@gmail.com" , "03022299-1")
  person = Person("Hasnain" , 18 , address , contact , ["python" , "crewai", "fastapi"])
  print(person.to_json())


def ahmed():
  address = Adress("123e main st" , "Karachi" , "Sindh" , "003321")
  contact = Contact("ahmed@gmail.com" , "03022299e-1")
  person = Person("Ahmed ALi" , 20 , address , contact , ["python" , "crewai","fastapi"])
  person.add_skill("Django")
  print(person.to_json())

hasnain()  
ahmed()
