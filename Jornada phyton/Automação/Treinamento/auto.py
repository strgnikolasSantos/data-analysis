import pyautogui  # Importa a biblioteca pyautogui para automação de GUI
import time  # Importa a biblioteca time para gerenciar atrasos
import pandas  # Importa a biblioteca pandas para manipulação de dados

pyautogui.PAUSE = 0.5  # Define um tempo de pausa padrão entre os comandos do pyautogui

# Abre o navegador Edge
pyautogui.press("win")  # Pressiona a tecla Windows
pyautogui.write("edge")  # Digita "edge" para procurar o navegador
pyautogui.press("enter")  # Pressiona Enter para abrir o navegador
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")  # Digita a URL do site
pyautogui.press("enter")  # Pressiona Enter para navegar até a URL

time.sleep(1)  # Aguarda 1 segundo para garantir que a página carregue

# Fazendo login
pyautogui.click(x=285, y=380)  # Clica no campo de e-mail (coordenadas específicas)
pyautogui.hotkey("Ctrl", "a")  # Seleciona todo o texto no campo de e-mail
pyautogui.write("teste@teste.teste.teste")  # Digita o e-mail de teste
pyautogui.press("tab")  # Pressiona Tab para ir para o campo de senha
pyautogui.write("123456789")  # Digita a senha
pyautogui.click(x=467, y=525)  # Clica no botão de login (coordenadas específicas)

time.sleep(1)  # Aguarda 1 segundo para garantir que o login seja realizado

# Importando a base de dados
tabela = pandas.read_csv("produtos.csv")  # Lê o arquivo CSV contendo os produtos e armazena em um DataFrame

# Cadastrando produtos
for linha in tabela.index:  # Itera sobre cada linha da tabela
    pyautogui.click(x=370, y=265)  # Clica no campo de código do produto (coordenadas específicas)
    
    codigo = str(tabela.loc[linha, "codigo"])  # Obtém o código do produto da tabela
    pyautogui.write(codigo)  # Digita o código do produto
    pyautogui.press("tab")  # Pressiona Tab para ir para o próximo campo

    marca = str(tabela.loc[linha, "marca"])  # Obtém a marca do produto da tabela
    pyautogui.write(marca)  # Digita a marca do produto
    pyautogui.press("tab")  # Pressiona Tab para ir para o próximo campo

    tipo = str(tabela.loc[linha, "tipo"])  # Obtém o tipo do produto da tabela
    pyautogui.write(tipo)  # Digita o tipo do produto
    pyautogui.press("tab")  # Pressiona Tab para ir para o próximo campo

    categoria = str(tabela.loc[linha, "categoria"])  # Obtém a categoria do produto da tabela
    pyautogui.write(categoria)  # Digita a categoria do produto
    pyautogui.press("tab")  # Pressiona Tab para ir para o próximo campo

    precoU = str(tabela.loc[linha, "preco_unitario"])  # Obtém o preço unitário do produto da tabela
    pyautogui.write(precoU)  # Digita o preço unitário do produto
    pyautogui.press("tab")  # Pressiona Tab para ir para o próximo campo

    custo = str(tabela.loc[linha, "custo"])  # Obtém o custo do produto da tabela
    pyautogui.write(custo)  # Digita o custo do produto
    pyautogui.press("tab")  # Pressiona Tab para ir para o próximo campo

    obs = str(tabela.loc[linha, "obs"])  # Obtém as observações do produto da tabela
    if obs != "nan":  # Verifica se há observações para o produto
        pyautogui.write(obs)  # Digita as observações
    pyautogui.press("tab")  # Pressiona Tab para ir para o próximo campo

    pyautogui.press("enter")  # Pressiona Enter para finalizar o cadastro do produto
    pyautogui.scroll(1000)  # Rola a página para cima para visualizar melhor o próximo produto a ser cadastrado
