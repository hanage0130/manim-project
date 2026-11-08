from manim import *

class SquareToCircle(Scene):
    def construct(self):
        square = Square()
        circle = Circle()
        self.play(Create(square))
        self.play(ReplacementTransform(square, circle))
        eq = MathTex(r"\int_a^b f'(x) \, dx = f(b) - f(a)")
        eq.scale(1.5)

        self.play(Write(eq))
        self.wait(2)