from datetime import datetime
import pytz

usuario = "Guilherme F"
saldo = 0
saques = 0
data_atual = datetime.now()
extrato = []

def deposit(valor):
    global  saldo, extrato 
    saldo += valor
    extrato.append(f"Deposito de {valor} Reais na data {data_atual}") 

    

def withdrawal(valor):
    global saques
    global extrato
    global saldo
    if(saques <= 3 and valor <= 500):
        
        saldo -= valor
        extrato.append(f"Saque de {valor} Reais na data {data_atual}") 
        saques += 1
    elif(valor > 500):
        print("Sanque maximo permitido R$500,00")
    elif(valor > saldo):
        print("Saldo insuficiente")
    else:
        print("Limite de saques diários excedidos")
    

    
def statement():
    global extrato
    global saldo
    if extrato:
        print(f"""
              ------------------------------
                        EXTRATO
              ------------------------------
                
              """)
        for transacao in extrato:
            print(transacao)
        print("SALDO EM CONTA: R${:,.2f}".format(saldo))
    else:
        print("Não foram realizadas movimentações")

print("""
      ------------------------------------------------
                INICIANDO OPERAÇÃO BANCARIA
      -------------------------------------------------
          MENU
          1 = DEPOSITAR
          2 = SACAR
          3 = EXTRATO
          4 = SAIR 
      
      """)


while True:
    opr = int(input("Digite a opção desejada: "))

    if opr == 1:
        valor = float(input("Digite o valor para depósito: "))
        deposit(valor)
    elif opr == 2:
        valor = float(input("Digite o valor para saque: "))
        withdrawal(valor)
    elif opr == 3:
        statement()
    elif opr == 4:
        print("Saindo...")
        break
    else:
        print("Digite uma opção válida")