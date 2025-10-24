from trabalhofinalpsi import *

def main():
    pacientes, medicos, funcionarios, salas = [], [], [], []

    # Funcionários iniciais
    m1 = Medico("João Rocha", 45, 3000, "Cardiologia")
    e1 = Enfermeiro("Maria Silva", 32, 1200, "noite")
    a1 = Administrativo("Carla Sousa", 40, 1000, "Recursos Humanos")
    ec1 = EnfermeiroChefe("Ana Costa", 38, 1500, "dia", "Urgência", 300)
    medicos.append(m1)
    funcionarios.extend([m1, e1, a1, ec1])

    # Salas
    sala1 = SalaConsulta(101, 2, m1)
    sala2 = SalaCirurgia(202, 1)
    sala2.adicionar_equipamento("Bisturi elétrico")
    sala2.adicionar_equipamento("Monitor cardíaco")
    salas.extend([sala1, sala2])

    while True:
        print("\n--- SISTEMA HOSPITALAR ---")
        print("1. Adicionar paciente")
        print("2. Listar pacientes e histórico")
        print("3. Listar médicos")
        print("4. Agendar consulta")
        print("5. Listar salas")
        print("6. Atualizar funcionário")
        print("7. Adicionar registro ao histórico")
        print("0. Sair")
        opcao = input("Opção: ").strip()

        if opcao == "1":
            nome = input("Nome do paciente: ").strip()
            try:
                idade = int(input("Idade: "))
            except ValueError:
                print("Idade inválida."); continue
            num = input("Nº Utente: ").strip()
            pacientes.append(Paciente(nome, idade, num))
            print(f"Paciente {nome} adicionado.")

        elif opcao == "2":
            if not pacientes: print("Nenhum paciente."); continue
            for p in pacientes:
                p.exibir_informacoes()
                p.mostrar_historico()

        elif opcao == "3":
            for m in medicos:
                m.exibir_informacoes()
                m.listar_pacientes()

        elif opcao == "4":
            if not pacientes: print("Nenhum paciente."); continue
            salas_consulta = [s for s in salas if isinstance(s, SalaConsulta)]
            if not salas_consulta: print("Nenhuma sala de consulta."); continue
            for s in salas_consulta: s.detalhar_sala()
            try:
                num_sala = int(input("Número da sala: "))
            except ValueError: print("Número inválido."); continue
            sala = next((s for s in salas_consulta if s.numero == num_sala), None)
            if not sala: print("Sala não encontrada."); continue
            for i, p in enumerate(pacientes, 1): print(f"{i}. {p.nome}")
            try:
                escolha = int(input("Escolha paciente: "))
                paciente = pacientes[escolha-1]
            except: print("Escolha inválida."); continue
            sala.agendar_consulta(paciente)
            paciente.adicionar_registro(f"Consulta na sala {sala.numero} com {sala.medico_responsavel.nome}")

        elif opcao == "5":
            for s in salas: s.detalhar_sala()

        elif opcao == "6":
            nome = input("Nome do funcionário: ").strip()
            f = next((x for x in funcionarios if x.nome.lower() == nome.lower()), None)
            if not f: print("Funcionário não encontrado."); continue
            if isinstance(f, (Enfermeiro, EnfermeiroChefe)):
                t = input("Novo turno (dia/noite, enter para manter): ").strip().lower()
                if t in ("dia","noite"): f.turno = t
            try:
                a = input("Percentual aumento (enter para manter): ").strip()
                if a: f.aplicar_aumento(float(a))
            except: print("Aumento inválido.")
            if isinstance(f, (Administrativo, EnfermeiroChefe)):
                try:
                    h = input("Horas a registrar (enter para manter): ").strip()
                    if h: f.registrar_horas(int(h))
                except: print("Horas inválidas.")
            print(f"Pagamento total: €{f.calcular_pagamento():.2f}")

        elif opcao == "7":
            if not pacientes: print("Nenhum paciente."); continue
            for i, p in enumerate(pacientes, 1): print(f"{i}. {p.nome}")
            try:
                paciente = pacientes[int(input("Escolha paciente: "))-1]
            except: print("Escolha inválida."); continue
            r = input("Digite o registro: ").strip()
            if r: paciente.adicionar_registro(r)
            print("Registro adicionado.")

        elif opcao == "0":
            print("Saindo..."); break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
