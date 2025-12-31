# Sistema Bancário em Python

Um sistema bancário completo desenvolvido em Python para simular operações básicas de conta corrente, incluindo depósitos, saques e consulta de extrato

## 📋 Sobre o Projeto

Este projeto foi desenvolvido como parte do curso de Back-end da DIO (Digital Innovation One), com o objetivo de praticar e consolidar os fundamentos de programação em Python.
O sistema simula um ambiente bancário real, aplicando boas práticas de código, modularização e lógica de negócio.

##  Funcionalidades

- ** Depósito**: Adicione valores à sua conta
- ** Saque**: Realize saques respeitando limites diários e de valor
- ** Extrato**: Visualize todas as transações realizadas e saldo atual
- ** Validações**: Sistema de segurança com limites configuráveis

## 🎯 Regras de Negócio

- Limite de **3 saques por dia**
- Valor máximo de **R$ 500,00 por saque**
- Validação de saldo antes de realizar saques
- Apenas valores positivos são aceitos
- Tratamento de erros para entradas inválidas

##  Como Executar

### Pré-requisitos

- Python 3.6 ou superior instalado

### Instalação e Execução

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/sistema-bancario.git
cd sistema-bancario
```

2. Execute o programa:
```bash
python sistema_bancario.py
```

##  Exemplo de Uso

```
🏦 Bem-vindo ao Sistema Bancário!

    ================ MENU ================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    ======================================
    => d

Informe o valor do depósito: R$ 1000

✓ Depósito de R$ 1000.00 realizado com sucesso!
```

## 🛠️ Tecnologias Utilizadas

- **Python 3.x** - Linguagem de programação
- **Programação Estruturada** - Organização em funções
- **Tratamento de Exceções** - Validação de entradas

## 📂 Estrutura do Código

```
sistema_bancario.py
├── exibir_menu()          # Exibe o menu de opções
├── depositar()            # Processa depósitos
├── sacar()                # Processa saques com validações
├── exibir_extrato()       # Mostra histórico de transações
└── main()                 # Função principal
```

## 🎓 Conceitos Aplicados

Este projeto demonstra a aplicação prática de diversos conceitos de programação:

- Modularização de código com funções
- Documentação com docstrings
- Tratamento de exceções (try/except)
- Validação de dados de entrada
- Formatação de strings e valores monetários
- Boas práticas de nomenclatura e organização

##  Funcionalidades Futuras

- [ ] Sistema de múltiplos usuários
- [ ] Persistência de dados em arquivo/banco de dados
- [ ] Interface gráfica (GUI)
- [ ] Transferências entre contas
- [ ] Histórico de transações com data/hora
- [ ] Sistema de autenticação

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👤 Autor

**Seu Nome**

- GitHub: [Mateus Leandro Silva](https://github.com/MateusLeandroSilva)
- LinkedIn: [Mateus Leandro Silva](https://www.linkedin.com/in/mateusleandrosilva)

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

1. Fork o projeto
2. Crie sua branch de feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

## ⭐ Mostre seu apoio

Se este projeto te ajudou, deixe uma ⭐!

---

**Desenvolvido com 💙 e ☕ enquanto aprendendo Python**
