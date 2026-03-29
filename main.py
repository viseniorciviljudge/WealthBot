
from manim import *
class WealthBotScene(Scene):
    def construct(self):
        self.camera.background_color = "#000000"
        txt = Text(""Discover the single most crucial wealth secret that turns average income into a fortune, no matter what your financial situation is right now."", color=GOLD, font_size=36).scale(0.8)
        self.play(Write(txt))
        self.play(txt.animate.set_color(YELLOW).scale(1.1))
        self.wait(2)
