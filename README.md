# 🎮 Heist Backpack - O Assalto Perfeito (Versão Pygame)

Um jogo simples em Python com interface gráfica (Pygame) que implementa o algoritmo **Knapsack (Problema da Mochila)**, com uma narrativa de assaltantes organizando uma mochila de fuga.
## Alunos
| Matrícula   | Aluno                             |
|------------|-----------------------------------|
| 22/2006196 | Wallyson Paulo Costa Souza        |
| 22/2006893 | Kaio Macedo Santana               |


## 🚀 Como Executar

### Pré-requisitos
- Python 3.x
- Pygame (será instalado automaticamente se não tiver)

### Instalação e Execução

1. **Baixe o arquivo `heist_backpack_pygame.py` e `README_pygame.md`**.
2. **Abra o terminal** na pasta onde você salvou os arquivos.
3. **Instale o Pygame** (se ainda não tiver):
   ```bash
   pip install pygame
   ```
   Se tiver problemas de permissão, tente:
   ```bash
   pip install pygame --user
   ```
4. **Execute o jogo**:
   ```bash
   python3 heist_backpack_pygame.py
   ```

## 🎯 Como Jogar

1. **Clique em "Iniciar Assalto"** para começar o cronômetro.
2. **Selecione os itens** clicando nos botões "Adicionar" ao lado de cada item.
3. **Observe o peso atual** da sua mochila (limite de 20kg).
4. **Maximize o valor** dos itens selecionados antes que o tempo acabe.
5. **Clique em "Calcular Solução Ótima"** para ver a melhor combinação de itens e comparar sua performance.
6. **Clique em "Novo Assalto"** para reiniciar o jogo.

## 💎 Itens Disponíveis

| Item | Peso | Valor |
|------|------|-------|
| 💎 Joias de Diamante | 1kg | R$ 5.000 |
| ⌚ Relógio de Ouro | 2kg | R$ 3.500 |
| 💻 Notebook Premium | 3kg | R$ 4.000 |
| 📱 Smartphone Top | 1kg | R$ 2.000 |
| 📷 Câmera Profissional | 4kg | R$ 6.000 |
| 📱 Tablet de Luxo | 2kg | R$ 2.500 |
| 💰 Dinheiro em Espécie | 3kg | R$ 8.000 |
| 💳 Cartões de Crédito | 1kg | R$ 1.500 |
| 🖼️ Obras de Arte Pequenas | 5kg | R$ 10.000 |
| 📄 Documentos Valiosos | 1kg | R$ 3.000 |

## 🧠 Algoritmo Knapsack

O jogo utiliza o algoritmo de **Programação Dinâmica** para resolver o problema da mochila, calculando a combinação de itens que maximiza o valor total sem exceder o peso máximo.

## 🎨 Recursos Visuais

- Interface gráfica simples e intuitiva.
- Tema escuro com cores de destaque.
- Ícones emoji para representar os itens.
- Feedback visual para peso excedido e tempo.

---

**Desenvolvido para demonstrar o algoritmo Knapsack de forma interativa e divertida.**

