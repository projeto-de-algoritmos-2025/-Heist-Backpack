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

def reset_game(self):
        """Reset do jogo"""
        for item in self.items:
            item.selected = False
        
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
        self.time_remaining = self.time_limit
        self.start_time = 0
        pygame.time.set_timer(pygame.USEREVENT + 1, 0) # Desativa o timer de erro
    
def draw_text(self, text, font, color, x, y, align="left"):
        """Desenha texto na tela com alinhamento"""
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        if align == "center":
            text_rect.center = (x, y)
        elif align == "right":
            text_rect.right = x
        else:
            text_rect.topleft = (x, y)
        self.screen.blit(text_surface, text_rect)
        return text_surface.get_height()
    
def draw_button(self, rect, text, font, bg_color, text_color, hover=False):
        """Desenha um botão"""
        color = BUTTON_HOVER_COLOR if hover else bg_color
        pygame.draw.rect(self.screen, color, rect, border_radius=8)
        pygame.draw.rect(self.screen, BORDER_COLOR, rect, 2, border_radius=8)
        
        self.draw_text(text, font, text_color, rect.centerx, rect.centery, align="center")

def draw_item_card(self, item, rect, is_hovered):
        bg_color = ITEM_CARD_BG
        border_color = ITEM_CARD_BORDER_SELECTED if item.selected else ITEM_CARD_BORDER_UNSELECTED
        
        pygame.draw.rect(self.screen, bg_color, rect, border_radius=8)
        pygame.draw.rect(self.screen, border_color, rect, 2, border_radius=8)

        # Icon
        icon_font = pygame.font.Font(None, 60)
        self.draw_text(item.icon, icon_font, TEXT_COLOR, rect.centerx, rect.top + 30, align="center")

        # Name
        self.draw_text(item.name, font_medium, HEADER_COLOR, rect.centerx, rect.top + 80, align="center")

        # Weight and Value
        self.draw_text(f"Peso: {item.weight}kg", font_small, TEXT_COLOR, rect.left + 10, rect.top + 110)
        self.draw_text(f"Valor: R$ {item.value:,.0f}", font_small, SUCCESS_COLOR, rect.left + 10, rect.top + 130)

def draw_header(self):
        self.draw_text("Heist Backpack - O Assalto Perfeito", font_title, HEADER_COLOR, WINDOW_WIDTH // 2, 40, align="center")

        if self.game_started and not self.game_ended:
            time_color = SUCCESS_COLOR if self.time_remaining > 60 else ERROR_COLOR
            self.draw_text(f"Tempo Restante: {self.time_remaining // 60:02d}:{self.time_remaining % 60:02d}", font_medium, time_color, 50, 100)
            self.draw_text(f"Peso Atual: {self.current_weight}/{self.max_weight} kg", font_medium, TEXT_COLOR, 350, 100)
            self.draw_text(f"Valor Atual: R$ {self.current_value:,.0f}", font_medium, SUCCESS_COLOR, 650, 100)

            if self.error_message:
                self.draw_text(self.error_message, font_small, ERROR_COLOR, 50, 130)
def draw_item_panel(self):
        panel_rect = pygame.Rect(30, 150, 800, 600) # Adjusted panel size and position
        pygame.draw.rect(self.screen, PANEL_COLOR, panel_rect, border_radius=10)
        pygame.draw.rect(self.screen, BORDER_COLOR, panel_rect, 2, border_radius=10)

        self.draw_text("Itens no Cofre:", font_header, HEADER_COLOR, 50, 170)

        item_card_width = 250
        item_card_height = 180
        padding_x = 20
        padding_y = 20
        start_x = 50
        start_y = 200

        for i, item in enumerate(self.items):
            row = i // 3
            col = i % 3
            x_pos = start_x + col * (item_card_width + padding_x)
            y_pos = start_y + row * (item_card_height + padding_y)
            item_rect = pygame.Rect(x_pos, y_pos, item_card_width, item_card_height)
            self.draw_item_card(item, item_rect, item_rect.collidepoint(pygame.mouse.get_pos()))

            button_rect, _ = self.item_buttons[i]
            button_text = "Remover" if item.selected else "Adicionar"
            button_color = ERROR_COLOR if item.selected else BUTTON_COLOR
            self.draw_button(button_rect, button_text, font_small, button_color, BUTTON_TEXT_COLOR, button_rect.collidepoint(pygame.mouse.get_pos()))

def draw_backpack_panel(self):
        panel_rect = pygame.Rect(850, 150, 320, 600) # Adjusted panel size and position
        pygame.draw.rect(self.screen, PANEL_COLOR, panel_rect, border_radius=10)
        pygame.draw.rect(self.screen, BORDER_COLOR, panel_rect, 2, border_radius=10)

        self.draw_text("Mochila de Fuga:", font_header, HEADER_COLOR, 870, 170)

        # Weight progress bar
        bar_x = 870
        bar_y = 210
        bar_width = 280
        bar_height = 20
        pygame.draw.rect(self.screen, (80, 80, 80), (bar_x, bar_y, bar_width, bar_height), border_radius=5)
        
        fill_width = (self.current_weight / self.max_weight) * bar_width
        fill_color = SUCCESS_COLOR if self.current_weight <= self.max_weight * 0.8 else ERROR_COLOR
        pygame.draw.rect(self.screen, fill_color, (bar_x, bar_y, fill_width, bar_height), border_radius=5)

        self.draw_text(f"{self.current_weight}/{self.max_weight} kg", font_small, TEXT_COLOR, bar_x + bar_width // 2, bar_y + bar_height // 2, align="center")

        # Selected items list
        self.draw_text("Itens na Mochila:", font_medium, TEXT_COLOR, 870, 250)
        y_offset = 280
        if not self.get_selected_items():
            self.draw_text("Mochila vazia", font_small, (150, 150, 150), 870, y_offset)
        else:
            for item in self.get_selected_items():
                self.draw_text(f"{item.icon} {item.name} ({item.weight}kg, R$ {item.value:,.0f})", font_small, TEXT_COLOR, 870, y_offset)
                y_offset += 25
        
        # Total value
        self.draw_text(f"Valor Total: R$ {self.current_value:,.0f}", font_medium, SUCCESS_COLOR, 870, y_offset + 20)

def draw_solution_panel(self):
        if self.show_solution:
            panel_rect = pygame.Rect(30, 680, 790, 100) # Positioned below item panel
            pygame.draw.rect(self.screen, PANEL_COLOR, panel_rect, border_radius=10)
            pygame.draw.rect(self.screen, BORDER_COLOR, panel_rect, 2, border_radius=10)

            self.draw_text("Análise da Solução:", font_header, HEADER_COLOR, 50, 700)

            self.draw_text(f"Valor Ótimo: R$ {self.optimal_value:,.0f}", font_small, SUCCESS_COLOR, 50, 730)
            self.draw_text(f"Peso Ótimo: {self.optimal_weight} kg", font_small, SUCCESS_COLOR, 50, 750)
            
            optimal_items_str = ", ".join([item.name for item in self.optimal_items])
            self.draw_text(f"Itens Ótimos: {optimal_items_str}", font_tiny, TEXT_COLOR, 50, 770)

            efficiency = (self.current_value / self.optimal_value * 100) if self.optimal_value > 0 else 0
            self.draw_text(f"Sua Eficiência: {efficiency:.1f}% da Solução Ótima", font_medium, TEXT_COLOR, 400, 730)
            if efficiency == 100:
                self.draw_text("🎉 Parabéns! Você encontrou a solução ótima!", font_small, SUCCESS_COLOR, 400, 750)
            elif efficiency > 0:
                self.draw_text("💪 Continue tentando! Há espaço para melhoria.", font_small, TEXT_COLOR, 400, 750)
            else:
                self.draw_text("🤔 Adicione alguns itens para começar!", font_small, TEXT_COLOR, 400, 750)

def get_selected_items(self):
        return [item for item in self.items if item.selected]

def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        
        self.draw_header()

        if not self.game_started and not self.game_ended:
            # Initial screen
            self.draw_text("Prepare-se para o maior assalto da história!", font_header, TEXT_COLOR, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50, align="center")
            self.draw_text(f"Você tem {self.time_limit // 60} minutos para organizar sua mochila de fuga.", font_medium, TEXT_COLOR, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 10, align="center")
            self.draw_button(self.start_game_button, "Iniciar Assalto", font_header, BUTTON_COLOR, BUTTON_TEXT_COLOR, self.start_game_button.collidepoint(pygame.mouse.get_pos()))
        else:
            self.draw_item_panel()
            self.draw_backpack_panel()
            self.draw_solution_panel()
             # Action buttons
            self.draw_button(self.solve_button, "Calcular Solução Ótima", font_medium, BUTTON_COLOR, BUTTON_TEXT_COLOR, self.solve_button.collidepoint(pygame.mouse.get_pos()))
            self.draw_button(self.reset_button, "Novo Assalto", font_medium, BUTTON_COLOR, BUTTON_TEXT_COLOR, self.reset_button.collidepoint(pygame.mouse.get_pos()))
            
            if self.game_ended and not self.show_solution:
                # Game over screen (time ran out)
                overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
                overlay.fill((0, 0, 0, 180)) # Semi-transparent black
                self.screen.blit(overlay, (0,0))
                self.draw_text("⏰ TEMPO ESGOTADO! A polícia chegou!", font_title, ERROR_COLOR, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50, align="center")
                self.draw_text("Pressione 'Novo Assalto' para tentar novamente.", font_medium, TEXT_COLOR, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 10, align="center")

        pygame.display.flip()
    
def run(self):
        clock = pygame.time.Clock()
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Clique esquerdo
                        self.handle_click(event.pos)
                elif event.type == pygame.USEREVENT + 1: # Timer para mensagem de erro
                    self.error_message = ""
                    pygame.time.set_timer(pygame.USEREVENT + 1, 0) # Desativa o timer
            
            if self.game_started and not self.game_ended:
                elapsed_time = (pygame.time.get_ticks() - self.start_time) // 1000
                self.time_remaining = max(0, self.time_limit - elapsed_time)
                if self.time_remaining == 0:
                    self.game_ended = True

            self.draw()
            clock.tick(60)
        
        pygame.quit()
        sys.exit()

if name == "main":
    game = KnapsackGame()
    game.run()        