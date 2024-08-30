class Cliente():
    # Inicializa a classe Cliente com atributos nome, email e plano
    def __init__(self, nome, email, plano):
        self.nome = nome  # Atributo para armazenar o nome do cliente
        self.email = email  # Atributo para armazenar o email do cliente
        self.lista_planos = ["basic", "premium"]  # Lista de planos válidos

        # Verifica se o plano fornecido está na lista de planos válidos
        if plano in self.lista_planos:
            self.plano = plano  # Atribui o plano ao cliente se for válido
        else:
            raise Exception("Plano inválido")  # Levanta uma exceção se o plano for inválido

    # Método para mudar o plano do cliente
    def mudar_plano(self, novo_plano):
        # Verifica se o novo plano está na lista de planos válidos
        if novo_plano in self.lista_planos:
            self.plano = novo_plano  # Atribui o novo plano ao cliente se for válido
        else:
            print("plano invalido")  # Exibe uma mensagem se o novo plano for inválido

    # Método para o cliente ver um filme
    def ver_filme(self, filme, plano_filme):
        # Verifica se o plano do cliente é igual ao plano necessário para o filme
        if self.plano == plano_filme:
            print(f"ver filme {filme}")  # Permite ver o filme se os planos forem iguais
        # Verifica se o plano do cliente é "premium"
        elif self.plano == "premium":
            print(f"ver filme {filme}")  # Permite ver o filme se o plano do cliente for "premium"
        # Verifica se o plano do cliente é "basic" e o plano necessário para o filme é "premium"
        elif self.plano == "basic" and plano_filme == "premium":
            print("Faça um upgrade para ver esse filme")  # Solicita upgrade para ver o filme
        else:
            print("plano inválido")  # Exibe uma mensagem se o plano for inválido

# Criação de um objeto Cliente com nome, email e plano
cliente = Cliente("Nik", "testetetet@teste", "basic")

# Exibe o plano atual do cliente
print(cliente.plano)

# Tenta ver o filme "Harry Potter" que requer plano "premium"
cliente.ver_filme("Harry Potter", "premium")

# Muda o plano do cliente para "premium"
cliente.mudar_plano("premium")

# Exibe o novo plano do cliente
print(cliente.plano)

# Tenta ver o filme "Harry Potter" novamente com o plano atualizado
cliente.ver_filme("Harry Potter", "premium")
