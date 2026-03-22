import pygame
import sys
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My First Pygame")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

clock = pygame.time.Clock()
running = True

# 원의 시작 위치
x = 400
y = 300

# 기본 속도
base_speed = 5

# 원 크기
# 실제 기본 파란 원이 50x50 이므로 반지름은 25로 맞춤
radius = 25

# 꿀렁 애니메이션 변수
squish_timer = 0

# 튕김 애니메이션 변수
bounce_frames = 0
bounce_dx = 0
bounce_dy = 0

# 충돌 메시지용 폰트
font = pygame.font.SysFont("malgungothic", 48, bold=True)

# 충돌 메시지 상태
message_timer = 0
message_particles = []

# 경계선 두께
border_thickness = 6


def trigger_collision_message():
    global message_timer, message_particles

    # 1초 표시 + 0.25초 분산 = 총 75프레임 (60fps 기준)
    message_timer = 75
    message_particles = []

    text = "충돌감지!"
    char_spacing = 38
    start_x = 400 - (len(text) - 1) * char_spacing // 2
    center_y = 300

    for i, ch in enumerate(text):
        particle = {
            "char": ch,
            "x": start_x + i * char_spacing,
            "y": center_y,
            "vx": random.uniform(-3.0, 3.0),
            "vy": random.uniform(-4.0, -1.0),
            "alpha": 255
        }
        message_particles.append(particle)


def draw_collision_message():
    global message_timer

    if message_timer <= 0:
        return

    # 75 ~ 16 프레임: 중앙 고정 표시
    # 15 ~ 1 프레임: 분산되며 사라짐
    if message_timer > 15:
        text_surface = font.render("충돌감지!", True, RED)
        text_rect = text_surface.get_rect(center=(400, 300))
        screen.blit(text_surface, text_rect)
    else:
        fade_ratio = message_timer / 15.0  # 1.0 -> 0.0

        for particle in message_particles:
            particle["x"] += particle["vx"]
            particle["y"] += particle["vy"]
            particle["vy"] += 0.15  # 살짝 아래로 떨어지게
            particle["alpha"] = int(255 * fade_ratio)

            char_surface = font.render(particle["char"], True, RED).convert_alpha()
            char_surface.set_alpha(particle["alpha"])
            char_rect = char_surface.get_rect(
                center=(int(particle["x"]), int(particle["y"]))
            )
            screen.blit(char_surface, char_rect)

    message_timer -= 1


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Shift 누르면 속도 2배
    speed = base_speed
    if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
        speed = base_speed * 2

    move_x = 0
    move_y = 0

    # 이동 입력
    if keys[pygame.K_w]:
        move_y -= speed
    if keys[pygame.K_a]:
        move_x -= speed
    if keys[pygame.K_s]:
        move_y += speed
    if keys[pygame.K_d]:
        move_x += speed

    # 스페이스 누르면 꿀렁 시작
    if keys[pygame.K_SPACE] and squish_timer == 0:
        squish_timer = 10

    # 기본 이동
    x += move_x
    y += move_y

    # 부드러운 튕김 이동 적용
    if bounce_frames > 0:
        x += bounce_dx
        y += bounce_dy
        bounce_frames -= 1

    # 충돌 판정용 경계
    min_x = border_thickness + radius
    max_x = 800 - border_thickness - radius
    min_y = border_thickness + radius
    max_y = 600 - border_thickness - radius

    collided = False

    # 왼쪽 벽 충돌
    if x < min_x:
        x = min_x
        collided = True
        bounce_frames = 10
        bounce_dx = 25 / 5   # 오른쪽으로 25픽셀
        bounce_dy = 0

    # 오른쪽 벽 충돌
    if x > max_x:
        x = max_x
        collided = True
        bounce_frames = 10
        bounce_dx = -25 / 5  # 왼쪽으로 25픽셀
        bounce_dy = 0

    # 위쪽 벽 충돌
    if y < min_y:
        y = min_y
        collided = True
        bounce_frames = 10
        bounce_dx = 0
        bounce_dy = 25 / 5   # 아래로 25픽셀

    # 아래쪽 벽 충돌
    if y > max_y:
        y = max_y
        collided = True
        bounce_frames = 10
        bounce_dx = 0
        bounce_dy = -25 / 5  # 위로 25픽셀

    # 충돌했으면 메시지 시작
    if collided:
        trigger_collision_message()

    screen.fill(WHITE)

    # 빨간 경계선
    pygame.draw.rect(screen, RED, (0, 0, 800, 600), border_thickness)

    # 꿀렁 효과
    if squish_timer > 0:
        width = 70
        height = 40
        squish_timer -= 1
    else:
        width = 50
        height = 50

    # 파란 원(타원)
    pygame.draw.ellipse(screen, BLUE, (x - width // 2, y - height // 2, width, height))

    # 충돌 메시지 그리기
    draw_collision_message()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()