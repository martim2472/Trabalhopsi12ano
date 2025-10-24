from abc import ABC, abstractmethod
from typing import List


class Pessoa(ABC):
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, v: str):
        if not v:
            raise ValueError("Nome vazio.")
        self._nome = v

    @property
    def idade(self) -> int:
        return self._idade

    @idade.setter
    def idade(self, v: int):
        if v <= 0:
            raise ValueError("Idade deve ser positiva.")
        self._idade = v

    @abstractmethod
    def exibir_informacoes(self):
        pass


class Paciente(Pessoa):
    def __init__(self, nome: str, idade: int, numero_utente: str):
        super().__init__(nome, idade)
        self.numero_utente = numero_utente
        self.historico: List[str] = []

    @property
    def numero_utente(self) -> str:
        return self._numero_utente

    @numero_utente.setter
    def numero_utente(self, v: str):
        if not v:
            raise ValueError("Número inválido.")
        self._numero_utente = v

    def adicionar_registro(self, d: str):
        self.historico.append(d)

    def mostrar_historico(self):
        if not self.historico:
            print("Sem histórico.")
        else:
            for r in self.historico:
                print("-", r)

    def exibir_informacoes(self):
        print(f"Paciente: {self.nome}, Idade: {self.idade}, Nº Utente: {self.numero_utente}")


class Funcionario(Pessoa):
    def __init__(self, nome: str, idade: int, cargo: str, salario):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.salario = salario

    @property
    def salario(self) -> float:
        return self._salario

    @salario.setter
    def salario(self, v):
        try:
            v = float(v)
        except (ValueError, TypeError):
            raise ValueError("Salário deve ser um número.")
        if v < 0:
            raise ValueError("Salário inválido.")
        self._salario = v

    def mostrar_informacoes(self):
        print(f"{self.cargo}: {self.nome}, Salário: €{self.salario:.2f}")

    def aplicar_aumento(self, p: float):
        self.salario += self.salario * p / 100


class Medico(Funcionario):
    def __init__(self, nome: str, idade: int, salario_base: float, especialidade: str):
        super().__init__(nome, idade, "Médico", salario_base)
        self.especialidade = especialidade
        self.pacientes: List[Paciente] = []

    @property
    def especialidade(self) -> str:
        return self._especialidade

    @especialidade.setter
    def especialidade(self, v: str):
        if not v:
            raise ValueError("Especialidade vazia.")
        self._especialidade = v

    def adicionar_paciente(self, p: Paciente):
        if not isinstance(p, Paciente):
            raise ValueError("Deve ser um Paciente.")
        self.pacientes.append(p)

    def listar_pacientes(self):
        if not self.pacientes:
            print("Sem pacientes.")
        else:
            for p in self.pacientes:
                print("-", p.nome)

    def calcular_pagamento(self) -> float:
        return self.salario + len(self.pacientes) * 50

    def exibir_informacoes(self):
        print(f"Médico: {self.nome}, Esp: {self.especialidade}, Pacientes: {len(self.pacientes)}")


class Enfermeiro(Funcionario):
    def __init__(self, nome: str, idade: int, salario_base: float, turno: str):
        super().__init__(nome, idade, "Enfermeiro", salario_base)
        self.turno = turno
        self.pacientes: List[Paciente] = []

    @property
    def turno(self) -> str:
        return self._turno

    @turno.setter
    def turno(self, v: str):
        if v not in ("dia", "noite"):
            raise ValueError("Turno inválido.")
        self._turno = v

    def adicionar_paciente(self, p: Paciente):
        if not isinstance(p, Paciente):
            raise ValueError("Deve ser um Paciente.")
        self.pacientes.append(p)

    def listar_pacientes(self):
        if not self.pacientes:
            print("Sem pacientes.")
        else:
            for p in self.pacientes:
                print("-", p.nome)

    def calcular_pagamento(self) -> float:
        return self.salario + (200 if self.turno == "noite" else 100)

    def exibir_informacoes(self):
        print(f"Enfermeiro: {self.nome}, Turno: {self.turno}, Pacientes: {len(self.pacientes)}")


class Administrativo(Funcionario):
    def __init__(self, nome: str, idade: int, salario_base: float, setor: str):
        super().__init__(nome, idade, "Administrativo", salario_base)
        self.setor = setor
        self.horas = 0

    @property
    def setor(self) -> str:
        return self._setor

    @setor.setter
    def setor(self, v: str):
        if not v:
            raise ValueError("Setor inválido.")
        self._setor = v

    def registrar_horas(self, h: int):
        self.horas += h

    def calcular_pagamento(self) -> float:
        return self.salario + self.horas * 10

    def exibir_informacoes(self):
        print(f"Administrativo: {self.nome}, Setor: {self.setor}, Horas: {self.horas}")



class EnfermeiroChefe(Funcionario):
    def __init__(self, nome: str, idade: int, salario_base: float, turno: str, setor: str, bonus_chefia: float):
        super().__init__(nome, idade, "Enfermeiro Chefe", salario_base)
        self.turno = turno
        self.setor = setor
        self.bonus_chefia = bonus_chefia
        self.pacientes: List[Paciente] = []
        self.horas = 0

    @property
    def turno(self) -> str:
        return self._turno

    @turno.setter
    def turno(self, v: str):
        if v not in ("dia", "noite"):
            raise ValueError("Turno inválido.")
        self._turno = v

    @property
    def setor(self) -> str:
        return self._setor

    @setor.setter
    def setor(self, v: str):
        if not v:
            raise ValueError("Setor inválido.")
        self._setor = v

    @property
    def bonus_chefia(self) -> float:
        return self._bonus_chefia

    @bonus_chefia.setter
    def bonus_chefia(self, v: float):
        if v < 0:
            raise ValueError("Bônus inválido.")
        self._bonus_chefia = v

    def adicionar_paciente(self, p: Paciente):
        if not isinstance(p, Paciente):
            raise ValueError("Deve ser um Paciente.")
        self.pacientes.append(p)

    def registrar_horas(self, h: int):
        self.horas += h

    def calcular_pagamento(self) -> float:
        return self.salario + (200 if self.turno == "noite" else 100) + self.horas * 10 + self.bonus_chefia

    def exibir_informacoes(self):
        print(f"Enf. Chefe: {self.nome}, Turno: {self.turno}, Setor: {self.setor}, Pacientes: {len(self.pacientes)}")


class Sala(ABC):
    def __init__(self, numero: int, capacidade: int):
        self.numero = numero
        self.capacidade = capacidade

    @property
    def numero(self) -> int:
        return self._numero

    @numero.setter
    def numero(self, v: int):
        if v <= 0:
            raise ValueError("Número inválido.")
        self._numero = v

    @property
    def capacidade(self) -> int:
        return self._capacidade

    @capacidade.setter
    def capacidade(self, v: int):
        if v <= 0:
            raise ValueError("Capacidade inválida.")
        self._capacidade = v

    @abstractmethod
    def detalhar_sala(self):
        pass


class SalaConsulta(Sala):
    def __init__(self, numero: int, capacidade: int, medico_responsavel: Medico):
        super().__init__(numero, capacidade)
        self.medico_responsavel = medico_responsavel
        self.pacientes: List[Paciente] = []

    @property
    def medico_responsavel(self) -> Medico:
        return self._medico_responsavel

    @medico_responsavel.setter
    def medico_responsavel(self, v: Medico):
        if not isinstance(v, Medico):
            raise ValueError("Responsável inválido.")
        self._medico_responsavel = v

    def agendar_consulta(self, p: Paciente):
        if not isinstance(p, Paciente):
            raise ValueError("Deve ser um Paciente.")
        if len(self.pacientes) >= self.capacidade:
            print("Sala cheia.")
        else:
            self.pacientes.append(p)
            self.medico_responsavel.adicionar_paciente(p)
            print(f"Consulta marcada para {p.nome} na sala {self.numero}.")

    def detalhar_sala(self):
        print(f"Sala {self.numero} (Consulta) - Médico: {self.medico_responsavel.nome}, Capacidade: {self.capacidade}")


class SalaCirurgia(Sala):
    def __init__(self, numero: int, capacidade: int):
        super().__init__(numero, capacidade)
        self.equipamentos: List[str] = []

    def adicionar_equipamento(self, e: str):
        self.equipamentos.append(e)

    def detalhar_sala(self):
        print(f"Sala {self.numero} (Cirúrgica) - Capacidade: {self.capacidade}")
        if self.equipamentos:
            print("Equipamentos:", ", ".join(self.equipamentos))
        else:
            print("Nenhum equipamento registrado.")
