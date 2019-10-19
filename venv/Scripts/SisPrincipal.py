print ("**Seja bem vindo ao nosso sistema de notas**")
name = input ("Qual o nome do aluno?\n")

insert_notes = True
registers = []
final_register = []

while True:
    matter = (input ("Digite o nome da matéria, ou enter para sair.\n"))
    insert_notes = True
    if matter != "":
        final_register.append(str(matter))
        while insert_notes:
            note =(input("Digite a nota, ou enter para sair.\n"))
            if note == "":
                insert_notes = False
                some = sum(registers)
                item = len(registers)
                media = float(some/item)
                final_register.append(float(media))
                print("A média de {}, do aluno {}, é: {:.2f}".format(matter, name, media))
            else:
                registers.append(float(note))
    else:
        print ("O boletim do aluno {}, é:\n {}".format(name, final_register))
        print ("sistema encerrado")
        break