
# 9:00 - 10:00 ~15 min~ 10:15 - 11:15 ~15 min~  11:30 - 12:30 --- 3 horários
# 14:00 - 15:00 ~15 min~ 15:15 - 16:15 ~15 min~  16:30 - 17:30 ~15 min~  17:45 - 18:45 --- 4 horários

# assumi que os pacientes e o doutor podem a qualquer momento dos dias em que estão disponíveis
# nada foi especificado a respeito de horários de atendimento

horarios = ["9:00 - 10:00 ", "10:15 - 11:15", "11:30 - 12:30",
            "14:00 - 15:00", "15:15 - 16:15", "16:30 - 17:30", "17:45 - 18:45"]

dr_etoupe_disponivel = {
    "Segunda-Feira": [],
    "Terça-Feira": [],
    "Quarta-Feira": [],
}

infos_pacientes = {
    "Roberto Dias": {
        "Contato": 99999998,
        "Restrição de horário": ["Quarta-Feira", "Quinta-Feira"],
        "Queixa": " Pedra no rim"
    },
    "Cristina Berge": {
        "Contato": 99999944,
        "Restrição de horário": [],
        "Queixa": " Cisto"
    },
}

for nome_do_paciente in infos_pacientes.keys():
    dias_indisponives_pacientes = infos_pacientes[nome_do_paciente]["Restrição de horário"]

    dias_disponiveis_pacientes = [dia for dia in dr_etoupe_disponivel.keys(
    ) if dia not in dias_indisponives_pacientes]

    for dia_disponivel in dias_disponiveis_pacientes:
        horarios_marcados_no_dia = len(dr_etoupe_disponivel[dia_disponivel])
        if horarios_marcados_no_dia < 7:

            horios_da_consulta = horarios[horarios_marcados_no_dia]

            infos_consulta = {
                "Paciente": nome_do_paciente,
                "Horário": horios_da_consulta,
                "Contato": infos_pacientes[nome_do_paciente]["Contato"],
                "Queixa": infos_pacientes[nome_do_paciente]["Queixa"]
            }

            dr_etoupe_disponivel[dia_disponivel].append(infos_consulta)
            break

print(dr_etoupe_disponivel)

# {'Segunda-Feira':
#   [
#       {'Paciente': 'Roberto Dias', 'Horário': '9:00 - 10:00 ', 'Contato': 99999998, 'Queixa': ' Pedra no rim'},
#       {'Paciente': 'Cristina Berge', 'Horário': '10:15 - 11:15', 'Contato': 99999944, 'Queixa': ' Cisto'}
#   ],
# 'Terça-Feira': [],
# 'Quarta-Feira': []}
