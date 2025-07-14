import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Constantes
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
PANEL_COLOR = (35, 35, 35)       
BORDER_COLOR = (60, 60, 60)      

BUTTON_COLOR = (180, 50, 50) 
BUTTON_HOVER_COLOR = (220, 70, 70)
BUTTON_TEXT_COLOR = (255, 255, 255)

TEXT_COLOR = (200, 200, 200)     
SUCCESS_COLOR = (50, 180, 50)    
ERROR_COLOR = (220, 50, 50)      
HEADER_COLOR = (255, 200, 0)     

ITEM_CARD_BG = (50, 50, 50)      
ITEM_CARD_BORDER_SELECTED = (255, 200, 0) 
ITEM_CARD_BORDER_UNSELECTED = (80, 80, 80) 

# Fontes
font_title = pygame.font.Font(None, 64)
font_header = pygame.font.Font(None, 36)
font_medium = pygame.font.Font(None, 28)
font_small = pygame.font.Font(None, 22)
font_tiny = pygame.font.Font(None, 18)

class Item:
    def _init_(self, name: str, weight: int, value: int, icon: str):
        self.name = name
        self.weight = weight
        self.value = value
        self.icon = icon
        self.selected = False

class KnapsackGame:
    def _init_(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Heist Backpack - O Assalto Perfeito")
        
        self.items = [
            Item("Joias de Diamante", 1, 5000, "💎"),
            Item("Relógio de Ouro", 2, 3500, "⌚"),
            Item("Notebook Premium", 3, 4000, "💻"),
            Item("Smartphone Top", 1, 2000, "📱"),
            Item("Câmera Profissional", 4, 6000, "📷"),
            Item("Tablet de Luxo", 2, 2500, "📱"),
            Item("Dinheiro em Espécie", 3, 8000, "💰"),
            Item("Cartões de Crédito", 1, 1500, "💳"),
            Item("Obras de Arte Pequenas", 5, 10000, "🖼"),
            Item("Documentos Valiosos", 1, 3000, "📄")
        ]
        
        self.max_weight = 20  
        self.current_weight = 0
        self.current_value = 0
        self.error_message = ""
        self.show_solution = False
        self.dp_table = []
        self.optimal_items = []
        self.optimal_value = 0
        self.optimal_weight = 0
        self.game_started = False
        self.game_ended = False
        self.time_limit = 300  
        self.time_remaining = self.time_limit
        self.start_time = 0
        
        # Botões
        self.item_buttons = []
        self.solve_button = None
        self.reset_button = None
        self.start_game_button = None
        
        self.create_buttons()
def create_buttons(self):
        # Botões para adicionar/remover itens
        self.item_buttons = []
        item_card_width = 250
        item_card_height = 180
        padding_x = 20
        padding_y = 20
        start_x = 50
        start_y = 150

        for i, item in enumerate(self.items):
            row = i // 3  # 3 items per row
            col = i % 3
            x_pos = start_x + col * (item_card_width + padding_x)
            y_pos = start_y + row * (item_card_height + padding_y)
            button_rect = pygame.Rect(x_pos + 25, y_pos + 140, 200, 30) # Adjusted button position
            self.item_buttons.append((button_rect, i))
        
        # Botão de resolver
        self.solve_button = pygame.Rect(50, WINDOW_HEIGHT - 60, 250, 40)
        
        # Botão de reset
        self.reset_button = pygame.Rect(320, WINDOW_HEIGHT - 60, 200, 40)

        # Botão de iniciar jogo
        self.start_game_button = pygame.Rect(WINDOW_WIDTH // 2 - 125, WINDOW_HEIGHT // 2 + 50, 250, 60)
    
def handle_click(self, pos):
        if not self.game_started and not self.game_ended:
            if self.start_game_button.collidepoint(pos):
                self.start_game()
                return

        if self.game_started and not self.game_ended:
            # Verificar cliques nos botões dos itens
            for button_rect, item_index in self.item_buttons:
                if button_rect.collidepoint(pos):
                    self.toggle_item(item_index)
                    return
            
            # Verificar clique no botão de resolver
            if self.solve_button.collidepoint(pos):
                self.solve_knapsack()
                return
        
        # Verificar clique no botão de reset
        if self.reset_button.collidepoint(pos):
            self.reset_game()
            return
    
def start_game(self):
        self.game_started = True
        self.start_time = pygame.time.get_ticks()  # Tempo em milissegundos

def toggle_item(self, item_index):
        item = self.items[item_index]
        
        if item.selected:
            # Remover item
            item.selected = False
            self.current_weight -= item.weight
            self.current_value -= item.value
            self.error_message = ""
        else:
            # Tentar adicionar item
            if self.current_weight + item.weight <= self.max_weight:
                item.selected = True
                self.current_weight += item.weight
                self.current_value += item.value
                self.error_message = ""
            else:
                self.error_message = "Peso excedido! Não é possível adicionar este item."
                # Adiciona um timer para a mensagem de erro desaparecer
                pygame.time.set_timer(pygame.USEREVENT + 1, 3000) # 3 segundos
def solve_knapsack(self):
        """Resolve o problema usando Programação Dinâmica"""
        n = len(self.items)
        w = self.max_weight
        
        # Criar tabela DP
        self.dp_table = [[0 for _ in range(w + 1)] for _ in range(n + 1)]
        
        # Preencher tabela DP
        for i in range(1, n + 1):
            for weight in range(1, w + 1):
                item = self.items[i - 1]
                
                if item.weight <= weight:
                    # Pode incluir o item
                    include_value = item.value + self.dp_table[i - 1][weight - item.weight]
                    exclude_value = self.dp_table[i - 1][weight]
                    self.dp_table[i][weight] = max(include_value, exclude_value);
                else:
                    # Não pode incluir o item
                    self.dp_table[i][weight] = self.dp_table[i - 1][weight]
        
        # Reconstruir solução
        self.optimal_value = self.dp_table[n][w]
        self.optimal_items = []
        self.optimal_weight = 0
        
        weight = w
        for i in range(n, 0, -1):
            if self.dp_table[i][weight] != self.dp_table[i - 1][weight]:
                item = self.items[i - 1]
                self.optimal_items.append(item)
                self.optimal_weight += item.weight
                weight -= item.weight
        
        self.show_solution = True
        self.game_ended = True # Jogo termina ao calcular a solução