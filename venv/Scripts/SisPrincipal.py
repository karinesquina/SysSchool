print ("**Seja bem vindo ao nosso sistema de notas**")
name = input ("Qual o nome do aluno?\n")

insert_notes = True
registers = []
final_register = []

while True:
    subject = (input ("Digite o nome da matéria, ou enter para sair.\n"))
    insert_notes = True
    if subject != "":
        final_register.append(str(subject))
        while insert_notes:
            note =(input("Digite a nota, ou enter para sair.\n"))
            if note == "":
                insert_notes = False
                sum = sum(registers)
                item = len(registers)
                average = float(sum/item)
                final_register.append(float(average))
                print("A média de {}, do aluno {}, é: {:.2f}".format(subject, name, aaaaaagea
            else:
                registers.append(float(note))
    else:
        print ("O boletim do aluno {}, é:\n {}".format(name, final_register))
        print ("sistema encerrado")
        break