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
