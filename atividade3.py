def avaliar_proposicoes(P, Q, M):
    R = (P and Q) or (P or Q) or (not P and M)
    return R

def avaliar_proposicoes(P, Q, M):
    R = (P and Q) or (P or Q) or (not P and M)
    return R

def gerar_tabela_verdade():
    print(f"{'P':<5} {'Q':<5} {'M':<5} {'R':<5}")
    print("P: Ana vai à festa.")
    print("Q: Bruno vai à festa.")
    print("M: Bruno traz música.")
    print("R: A festa é animada.")
    print("-" * 30)  # Linha separadora

    # Gera todas as combinações de valores para P, Q e M
    for P in [True, False]:
        for Q in [True, False]:
            for M in [True, False]:
                R = avaliar_proposicoes(P, Q, M)
                print(f"{int(P):<5} {int(Q):<5} {int(M):<5} {int(R):<5}")  # Exibe os valores

# Função principal com interação para definir um caso específico
def main():
    resposta = input("Deseja ver a tabela verdade completa? (s/n): ").strip().lower()

    if resposta == 's':
        gerar_tabela_verdade()
    else:
        # Receber valores específicos do usuário
        P_input = input("Ana vai à festa? (s/n): ").strip().lower()
        Q_input = input("Bruno vai à festa? (s/n): ").strip().lower()
        M_input = input("Bruno traz música? (s/n): ").strip().lower()

        # Converter entradas para valores booleanos
        P = P_input == 's'
        Q = Q_input == 's'
        M = M_input == 's'

        # Exibir resultado para o caso específico fornecido pelo usuário
        print("\nResultado:")
        print(f"{'P':<5} {'Q':<5} {'M':<5} {'R':<5}")
        print("P: Ana vai à festa.")
        print("Q: Bruno vai à festa.")
        print("M: Bruno traz música.")
        print("R: A festa é animada.")
        print("-" * 30)  # Linha separadora

        R = avaliar_proposicoes(P, Q, M)
        print(f"{int(P):<5} {int(Q):<5} {int(M):<5} {int(R):<5}")  # Exibe os valores

# Executar a função principal
if __name__ == "__main__":
    main()
