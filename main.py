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

class Teste():    
  
  def testar_pessoa():
    pessoa = Person()
    pessoa.cpf = "794.456.123-18"
    pessoa.name = "Josué"
    pessoa.phone = "(84)98164-9028"
    print (f"Seu nome é {pessoa.name} seu CPF é {pessoa.cpf} e seu numero é {pessoa.phone} ")
  
  def testar_medico():
    medico = Medic()
    medico.cpf = "744.452.133-13"
    medico.name = "José"
    medico.phone = "(84)98364-9258"
    medico.specialization = "Urologista"
    print (f"Seu nome é {medico.name} seu CPF é {medico.cpf} e seu numero é {medico.phone} e você é {medico.specialization} ")
  
  def testar_paciente():
    paciente = Patient()
    paciente.cpf = "944.859.133-22"
    paciente.name = "José"
    paciente.phone = "(84)91464-9458"
    paciente.id = "9"
    print (f"Seu nome é {paciente.name} seu CPF é {paciente.cpf} e seu numero é {paciente.phone} e seu identificador é {paciente.id} ")
  
  




Teste.testar_pessoa()
Teste.testar_medico()
Teste.testar_paciente()

  