def exibir_menu():
    """Exibe o menu de opções do sistema bancário."""
    menu = """
    ================ MENU ================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    ======================================
    => """
    return input(menu).lower().strip()


def depositar(saldo, extrato):
    """
    Realiza um depósito na conta.
    
    Args:
        saldo: Saldo atual da conta
        extrato: Histórico de transações
    
    Returns:
        Tupla com (novo_saldo, novo_extrato)
    """
    try:
        valor = float(input("Informe o valor do depósito: R$ "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito:  R$ {valor:>10.2f}\n"
            print(f"\n✓ Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("\n✗ Operação falhou! O valor deve ser positivo.")
    
    except ValueError:
        print("\n✗ Operação falhou! Valor inválido.")
    
    return saldo, extrato


def sacar(saldo, extrato, numero_saques, limite, limite_saques):
    """
    Realiza um saque da conta.
    
    Args:
        saldo: Saldo atual da conta
        extrato: Histórico de transações
        numero_saques: Número de saques realizados hoje
        limite: Valor máximo por saque
        limite_saques: Número máximo de saques diários
    
    Returns:
        Tupla com (novo_saldo, novo_extrato, novo_numero_saques)
    """
    try:
        valor = float(input("Informe o valor do saque: R$ "))
        
        if valor <= 0:
            print("\n Operação falhou! O valor deve ser positivo.")
        elif valor > saldo:
            print("\n Operação falhou! Saldo insuficiente.")
        elif valor > limite:
            print(f"\n Operação falhou! O limite por saque é R$ {limite:.2f}.")
        elif numero_saques >= limite_saques:
            print(f"\n Operação falhou! Limite de {limite_saques} saques diários atingido.")
        else:
            saldo -= valor
            extrato += f"Saque:     R$ {valor:>10.2f}\n"
            numero_saques += 1
            print(f"\n Saque de R$ {valor:.2f} realizado com sucesso!")
    
    except ValueError:
        print("\n Operação falhou! Valor inválido.")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, extrato, numero_saques, limite_saques):
    """
    Exibe o extrato da conta.
    
    Args:
        saldo: Saldo atual da conta
        extrato: Histórico de transações
        numero_saques: Número de saques realizados
        limite_saques: Limite de saques diários
    """
    print("\n" + "="*50)
    print(" "*18 + "EXTRATO")
    print("="*50)
    
    if extrato:
        print(extrato)
    else:
        print("Não foram realizadas movimentações.")
    
    print("-"*50)
    print(f"Saldo atual:        R$ {saldo:>10.2f}")
    print(f"Saques realizados:  {numero_saques}/{limite_saques}")
    print("="*50)


def main():
    """Função principal que executa o sistema bancário."""
    # Constantes
    LIMITE_POR_SAQUE = 500
    LIMITE_SAQUES_DIARIOS = 3
    
    # Variáveis de estado
    saldo = 0
    extrato = ""
    numero_saques = 0
    
    print("\n Bem-vindo ao Sistema Bancário!")
    
    while True:
        opcao = exibir_menu()
       
        
        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)
        
        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(
                saldo, extrato, numero_saques, 
                LIMITE_POR_SAQUE, LIMITE_SAQUES_DIARIOS
            )
        
        elif opcao == "e":
            exibir_extrato(saldo, extrato, numero_saques, LIMITE_SAQUES_DIARIOS)
        
        elif opcao == "q":
            print("\n👋 Obrigado por usar nosso sistema. Até logo!")
            break
        
        else:
            print("\n✗ Operação inválida! Por favor, selecione uma opção válida.")


if __name__ == "__main__":
    main()