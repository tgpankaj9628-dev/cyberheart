import turtle
import math
import time
import random
import colorsys

# ==========================================
# 🌟 Screen Setup & Configuration
# ==========================================
screen = turtle.Screen()
screen.setup(850, 850)
screen.bgcolor("#040207")  # Deep cosmic midnight background
screen.title("✨ Ethereal Cyber-Glow Beating Heart ✨")
screen.colormode(1.0)
screen.tracer(0)

# Turtle Artists
bg_t = turtle.Turtle()      # For stars and background glow
bg_t.hideturtle()
bg_t.speed(0)

ray_t = turtle.Turtle()     # For glowing rays
ray_t.hideturtle()
ray_t.speed(0)

pulse_t = turtle.Turtle()   # For live beating core & pulse effects
pulse_t.hideturtle()
pulse_t.speed(0)

text_t = turtle.Turtle()    # For glowing text
text_t.hideturtle()
text_t.speed(0)


# ==========================================
# 📐 Heart Geometry Formula
# ==========================================
def heart_x(angle):
    return 16 * (math.sin(angle) ** 3)

def heart_y(angle):
    return 13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)


# ==========================================
# 🌌 Phase 1: Cosmic Background Stars & Halo
# ==========================================
def draw_background():
    # Subtle background twinkling stars
    random.seed(42)
    for _ in range(75):
        sx = random.randint(-400, 400)
        sy = random.randint(-400, 400)
        # Avoid cluttering exact heart center
        if math.hypot(sx, sy) < 140:
            continue
        brightness = random.uniform(0.3, 0.95)
        # Soft blue/purple/white star shades
        star_color = (brightness * 0.9, brightness * 0.85, brightness)
        bg_t.penup()
        bg_t.goto(sx, sy)
        bg_t.pendown()
        bg_t.dot(random.uniform(1.2, 3.2), star_color)
    screen.update()

draw_background()


# ==========================================
# 💖 Phase 2: Radiant Aurora Glowing Rays
# ==========================================
N = 220
outer_scale = 18.5
inner_scale = 4.2
steps = 22

for i in range(N):
    angle = 2 * math.pi * i / N
    
    xo = heart_x(angle) * outer_scale
    yo = heart_y(angle) * outer_scale
    
    xi = heart_x(angle) * inner_scale
    yi = heart_y(angle) * inner_scale
    
    # Dynamic Aurora Palette: Violet -> Magenta -> Rose -> Crimson -> Gold
    # Sweeps smoothly around 360 degrees
    hue = (0.76 + 0.32 * (i / N)) % 1.0
    c_outer = colorsys.hsv_to_rgb(hue, 0.95, 1.0)
    c_inner = colorsys.hsv_to_rgb((hue + 0.05) % 1.0, 0.9, 0.12)
    
    for j in range(steps):
        f1 = j / steps
        f2 = (j + 1) / steps
        
        x1 = xo + (xi - xo) * f1
        y1 = yo + (yi - yo) * f1
        x2 = xo + (xi - xo) * f2
        y2 = yo + (yi - yo) * f2
        
        # Color interpolation
        r = c_outer[0] + (c_inner[0] - c_outer[0]) * (f1 ** 0.8)
        g = c_outer[1] + (c_inner[1] - c_outer[1]) * (f1 ** 0.8)
        b = c_outer[2] + (c_inner[2] - c_outer[2]) * (f1 ** 0.8)
        
        # Width tapers gracefully inwards
        w = 2.8 * (1.0 - 0.75 * f1)
        
        ray_t.pencolor(r, g, b)
        ray_t.width(w)
        ray_t.penup()
        ray_t.goto(x1, y1)
        ray_t.pendown()
        ray_t.goto(x2, y2)
        
    # Floating spark at outer tip
    if i % 6 == 0:
        spark_color = colorsys.hsv_to_rgb(hue, 0.4, 1.0)
        ray_t.penup()
        ray_t.goto(xo, yo)
        ray_t.dot(random.uniform(2.5, 4.5), spark_color)
        
    screen.update()
    time.sleep(0.009)


# ==========================================
# 💎 Phase 3: Inner Crystalline Core Rings
# ==========================================
def draw_heart_contour(t, scale, color, pen_width):
    t.penup()
    t.width(pen_width)
    t.pencolor(color)
    pts = 100
    for k in range(pts + 1):
        a = 2 * math.pi * k / pts
        x = heart_x(a) * scale
        y = heart_y(a) * scale
        if k == 0:
            t.goto(x, y)
            t.pendown()
        else:
            t.goto(x, y)
    t.penup()

# Draw static inner concentric ripple rings
for s, col, pw in [
    (10.0, (0.7, 0.1, 0.45), 1.2),
    (6.5, (0.9, 0.2, 0.6), 1.5),
    (4.0, (1.0, 0.4, 0.8), 2.0),
    (2.0, (1.0, 0.85, 0.95), 2.5)
]:
    draw_heart_contour(ray_t, s, col, pw)

screen.update()


# ==========================================
# ✍️ Phase 4: Ambient Romantic Typography
# ==========================================
text_t.penup()
text_t.goto(0, -345)
text_t.pencolor((1.0, 0.75, 0.88))
text_t.write("Forever in my Heart", align="center", font=("Georgia", 16, "italic"))

text_t.goto(0, -370)
text_t.pencolor((0.65, 0.45, 0.65))
text_t.write("— rhythm of love —", align="center", font=("Verdana", 10, "normal"))
screen.update()


# ==========================================
# 💓 Phase 5: Dynamic Heartbeat Pulse Loop
# ==========================================
# Precompute normalized points for the pulsing core
contour_angles = [2 * math.pi * k / 80 for k in range(81)]
base_core_points = [(heart_x(a), heart_y(a)) for a in contour_angles]

pulse_time = 0.0

try:
    while True:
        pulse_t.clear()
        
        # Real anatomical heartbeat rhythm formula: Lub-Dub
        # Using periodic exponential pulse
        cycle = (pulse_time * 2.8) % (2 * math.pi)
        beat = (math.sin(cycle) ** 63) * 0.4 + (math.sin(cycle + 0.35) ** 63) * 0.25
        
        core_scale = 3.5 + beat * 1.5
        halo_scale = 5.2 + beat * 2.2
        
        # Outer dynamic pulse halo
        pulse_t.width(1.8 + beat * 2)
        halo_r = min(1.0, 0.9 + beat * 0.1)
        halo_g = 0.15 + beat * 0.35
        halo_b = 0.5 + beat * 0.45
        pulse_t.pencolor(halo_r, halo_g, halo_b)
        
        pulse_t.penup()
        for idx, (hx, hy) in enumerate(base_core_points):
            px = hx * halo_scale
            py = hy * halo_scale
            if idx == 0:
                pulse_t.goto(px, py)
                pulse_t.pendown()
            else:
                pulse_t.goto(px, py)
        pulse_t.penup()
        
        # Bright vibrant core
        core_col = (1.0, 0.4 + beat * 0.5, 0.7 + beat * 0.3)
        pulse_t.width(2.5 + beat * 1.5)
        pulse_t.pencolor(core_col)
        for idx, (hx, hy) in enumerate(base_core_points):
            px = hx * core_scale
            py = hy * core_scale
            if idx == 0:
                pulse_t.goto(px, py)
                pulse_t.pendown()
            else:
                pulse_t.goto(px, py)
        pulse_t.penup()
        
        # Soft center glow point
        pulse_t.goto(0, 5)
        pulse_t.dot(14 + beat * 12, (1.0, 0.85, 0.95))
        
        screen.update()
        time.sleep(0.02)
        pulse_time += 0.02

except turtle.Terminator:
    pass
except Exception:
    pass

turtle.done()
