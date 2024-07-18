class Person():
  __cpf = ""
  _phone = ""
  name = ""

  @property
  def cpf(self):
    return f"O cpf de {self.name}: {self.__cpf}"
  
  @cpf.setter
  def cpf(self, value):
    self.__cpf = value

  @property
  def phone(self):
    return self._phone

  @phone.setter
  def phone(self, value):
    self._phone = value

class Medic(Person):
  specialization = "" 

class Patient(Person):
  __id = 0

  @property
  def id(self):
    return self.__id
  
  @id.setter
  def id(self, value):
    self.__id = value
