import pygame
import random

# 1. Inisialisasi Pygame
pygame.init()

# Ukuran Layar Game
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("CIAOBELLA Jumpie")

# Clock & FPS
clock = pygame.time.Clock()
FPS = 60

# Game Variables
GRAVITY = 0.6
SCROLL_THRESH = 200 # Batas saat layar mulai scroll ke atas
scroll = 0
score = 0

# 2. Load Asset Gambar Custom
bg_image = pygame.image.load("sky.png").convert_alpha()
bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Ukuran Player Pas & Jelas (60x60 px)
PLAYER_SIZE = 60
player_image = pygame.image.load("orang.png").convert_alpha()
player_image = pygame.transform.scale(player_image, (PLAYER_SIZE, PLAYER_SIZE)) 

# Warna & Font
WHITE = (255, 255, 255)
WOOD_BROWN = (139, 69, 19)    # Pijakan Standar
MOVING_BLUE = (30, 144, 255)  # Pijakan Bergerak (Skor 1000+)
BROKEN_RED = (220, 20, 60)    # Pijakan Rapuh / Sekali Injak (Skor 2000+)

font = pygame.font.SysFont("Arial", 22, bold=True)

# 3. Class Karakter (Player)
class Player():
    def __init__(self, x, y):
        self.image = player_image
        self.width = PLAYER_SIZE
        self.height = PLAYER_SIZE
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.vel_y = 0
        self.flip = False

    def move(self):
        dx = 0
        dy = 0
        scroll_temp = 0

        # Input Keyboard (Panah / A & D)
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            dx = -8
            self.flip = True
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            dx = 8
            self.flip = False

        # Gravitasi
        self.vel_y += GRAVITY
        dy += self.vel_y

        # Cek Tabrakan dengan Pijakan
        for platform in platform_group:
            if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                # Membal hanya jika posisi kaki mendarat dari atas
                if self.rect.bottom < platform.rect.centery + 10:
                    if self.vel_y > 0:
                        self.rect.bottom = platform.rect.top
                        dy = 0
                        self.vel_y = -14 # Kekuatan lompatan

                        # Jika pijakan jenis 'broken' (merah), langsung hancur setelah diinjak
                        if platform.p_type == 'broken':
                            platform.kill()

        # Update Posisi X
        self.rect.x += dx

        # Screen Wrap (Tembus Layar Kiri/Kanan)
        if self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0
        elif self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH

        # Scroll Kamera ke Atas
        if self.rect.top <= SCROLL_THRESH:
            if self.vel_y < 0:
                scroll_temp = -dy

        # Update Posisi Y
        self.rect.y += dy + scroll_temp

        return scroll_temp

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x, self.rect.y))

# 4. Class Pijakan
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, p_type='standard'):
        super().__init__()
        self.width = width
        self.height = 15
        self.p_type = p_type # Jenis: 'standard', 'moving', atau 'broken'
        self.speed = random.choice([-3, 3]) # Kecepatan gerak pijakan moving

        self.image = pygame.Surface((self.width, self.height))
        
        # Warna berdasarkan jenis pijakan
        if self.p_type == 'moving':
            self.image.fill(MOVING_BLUE)
        elif self.p_type == 'broken':
            self.image.fill(BROKEN_RED)
        else:
            self.image.fill(WOOD_BROWN)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, scroll):
        # Pergerakan khusus pijakan bergerak (biru)
        if self.p_type == 'moving':
            self.rect.x += self.speed
            # Pantulkan jika menyentuh pinggir layar
            if self.rect.right >= SCREEN_WIDTH or self.rect.left <= 0:
                self.speed *= -1

        # Scroll ke bawah seiring player naik
        self.rect.y += scroll
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

# Instansiasi Karakter
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)
platform_group = pygame.sprite.Group()

MAX_PLATFORMS = 8

# Fungsi Menentukan Jenis Pijakan Berdasarkan Skor Terbaru
def get_random_platform_type(current_score):
    if current_score >= 2000:
        # Skor 2000+: Muncul Pijakan Bergerak (Biru) & Pijakan Pecah (Merah)
        return random.choices(['standard', 'moving', 'broken'], weights=[40, 35, 25])[0]
    elif current_score >= 1000:
        # Skor 1000+: Muncul Pijakan Bergerak (Biru)
        return random.choices(['standard', 'moving'], weights=[60, 40])[0]
    else:
        # Skor < 1000: Pijakan Biasa
        return 'standard'

# Fungsi Generate Susunan Pijakan Awal
def generate_platforms():
    platform_group.empty()
    # Pijakan pertama di bawah player
    p_start = Platform(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 50, 100, 'standard')
    platform_group.add(p_start)
    
    # Pijakan ke atas secara bertingkat
    for i in range(1, MAX_PLATFORMS):
        p_w = random.randint(75, 95)
        p_x = random.randint(10, SCREEN_WIDTH - p_w - 10)
        p_y = SCREEN_HEIGHT - 50 - (i * 85)
        p = Platform(p_x, p_y, p_w, 'standard')
        platform_group.add(p)

generate_platforms()

# 5. Game Loop Utama
game_over = False
running = True

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        scroll = player.move()
        score += int(scroll)

        # Generate pijakan baru di atas sesuai kenaikan skor
        if len(platform_group) < MAX_PLATFORMS:
            p_w = random.randint(75, 95)
            p_x = random.randint(10, SCREEN_WIDTH - p_w - 10)
            p_y = -random.randint(10, 30)
            p_type = get_random_platform_type(score)
            p = Platform(p_x, p_y, p_w, p_type)
            platform_group.add(p)

        platform_group.update(scroll)

        # Cek Kalah
        if player.rect.top > SCREEN_HEIGHT:
            game_over = True

        # Render Visual
        screen.blit(bg_image, (0, 0))
        platform_group.draw(screen)
        player.draw()

        # UI Tampilan Skor & Level
        score_text = font.render(f"SKOR: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        # Indikator Tingkat Kesulitan
        if score >= 2000:
            lvl_text = font.render("LEVEL: HARDCORE 🔥", True, BROKEN_RED)
        elif score >= 1000:
            lvl_text = font.render("LEVEL: MEDIUM ⚡", True, MOVING_BLUE)
        else:
            lvl_text = font.render("LEVEL: EASY 🌱", True, WHITE)
        screen.blit(lvl_text, (10, 35))

    else:
        font_go = pygame.font.SysFont("Arial", 22, bold=True)

        go_text = font_go.render("SKILL ISSUE DEK >_<", True, WHITE)
        restart_text1 = font_go.render("Tekan SPASI dulu ga sih", True, WHITE)
        restart_text2 = font_go.render("biar ga TANTRUM? :p", True, WHITE)

        go_rect = go_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 35))
        restart_rect1 = restart_text1.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 10))
        restart_rect2 = restart_text2.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40))

        screen.blit(go_text, go_rect)
        screen.blit(restart_text1, restart_rect1)
        screen.blit(restart_text2, restart_rect2)

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            game_over = False
            score = 0
            player.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)
            player.vel_y = 0
            generate_platforms()

    pygame.display.update()

pygame.quit()