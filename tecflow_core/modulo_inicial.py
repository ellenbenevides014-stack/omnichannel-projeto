
# ============================================================
# PROJETO TECHFLOW CORE
# Modulo de Autenticacao e Requisicoes
# Padrao de codigo: PEP 8
# ============================================================

def executar_sistema():
    print("--- SISTEMA TECHFLOW CORE ---")

    tentativas_maximas = 3
    tentativas_atuais = 0
    usuario_autenticado = False

    usuario_correto = "admin_techflow"
    senha_correta = "senha123"

    while tentativas_atuais < tentativas_maximas and not usuario_autenticado:
        print(
            f"\n[Tentativa {tentativas_atuais + 1} "
            f"de {tentativas_maximas}]"
        )

        usuario_input = input("Informe o usuario: ").strip()
        senha_input = input("Informe a senha: ").strip()

        if not usuario_input or not senha_input:
            print("Aviso: Nenhum campo pode ficar em branco!")
            tentativas_atuais += 1

        elif (
            usuario_input == usuario_correto
            and senha_input == senha_correta
        ):
            usuario_autenticado = True
            print("\nSucesso: Acesso concedido!")
            print("Bem-vindo ao TechFlow Core.")

        else:
            print("Erro: Usuario ou senha incorretos.")
            tentativas_atuais += 1

    if usuario_autenticado:
        executar_menu_principal(senha_correta)
    else:
        print("\nBloqueio: Numero maximo de tentativas excedido.")


def executar_menu_principal(senha_correta):
    executando = True

    while executando:
        print("\n=== MENU TECHFLOW CORE ===")
        print("1 - Registrar Novo Chamado")
        print("2 - Listar Chamados Ativos")
        print("3 - Sair do Sistema")
        print("4 - Alterar Senha")

        opcao = input("Selecione uma opcao (1-4): ").strip()

        if opcao == "1":
            titulo_chamado = input(
                "Digite o titulo do chamado: "
            ).strip()

            if len(titulo_chamado) >= 5:
                print(
                    f"Sucesso: Chamado '{titulo_chamado}' registrado!"
                )
            else:
                print(
                    "Aviso: O titulo deve ter pelo menos "
                    "5 caracteres."
                )

        elif opcao == "2":
            print("\nCarregando lista de chamados...")

            for i in range(1, 4):
                print(
                    f" -> Chamado #00{i}: [Em Andamento]"
                )

        elif opcao == "3":
            print(
                "Encerrando sessao no TechFlow Core. Ate breve!"
            )
            executando = False

        elif opcao == "4":
            senha_atual = input(
                "Informe sua senha atual: "
            ).strip()

            if senha_atual == senha_correta:
                nova_senha = input(
                    "Digite a nova senha: "
                ).strip()

                confirmar_senha = input(
                    "Confirme a nova senha: "
                ).strip()

                if not nova_senha:
                    print("Erro: A nova senha nao pode ficar vazia.")

                elif nova_senha == confirmar_senha:
                    senha_correta = nova_senha
                    print("Sucesso: Senha alterada!")
                else:
                    print("Erro: As senhas nao coincidem.")

            else:
                print("Erro: Senha atual incorreta.")

        else:
            print(
                "Aviso: Opcao invalida! Escolha entre 1 e 4."
            )

    return senha_correta


# Execucao do programa
if __name__ == "__main__":
    executar_sistema()
