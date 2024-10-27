import turtle


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_snowflake(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / 3)  # Початкове положення трохи вище центру
    t.pendown()

    for _ in range(3):  # Малюємо три сторони рівностороннього трикутника
        koch_curve(t, order, size)
        t.right(120)  # Повертаємо черепашку на 120 градусів для наступної сторони

    window.mainloop()

# Виклик функції для малювання сніжинки Коха
draw_koch_snowflake(5)
