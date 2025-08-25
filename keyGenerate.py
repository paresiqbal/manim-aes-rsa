from manim import *

class KeyGenerate(Scene):
    def construct(self):
        # background
        self.camera.background_color = "#27272A"

        # Positions from -5 to 4 (10 keys total)
        positions = [LEFT * 5 + RIGHT * i for i in range(10)]

        # === First key ===
        first_key = ImageMobject("media/images/main/key.png").scale(0.25)

        # 1) Appear in center
        self.play(FadeIn(first_key, run_time=0.6))

        # 2) Wait 2 seconds
        self.wait(2)

        # 3) Move to x = -5
        self.play(first_key.animate.move_to(positions[0]), run_time=0.8)

        keys = [first_key]

        # === Other keys ===
        for pos in positions[1:]:
            key = ImageMobject("media/images/main/key.png").scale(0.25)
            key.move_to(pos)
            self.play(FadeIn(key, run_time=0.3))
            keys.append(key)

        self.wait(1)

        # === Number above first key ===
        num0 = Text("0", font_size=36, color=WHITE).next_to(keys[0], UP, buff=0.3)
        self.play(Write(num0))
        self.wait(1)

        # === Repeat for all keys 1–9 ===
        for i in range(1, len(keys)):
            num = Text(str(i), font_size=36, color=WHITE).next_to(keys[i], UP, buff=0.3)

            arrow = CurvedArrow(
                keys[i].get_bottom(),
                keys[i-1].get_bottom(),
                angle=-PI,        # strong curve at bottom
                stroke_color=YELLOW,
                stroke_width=4,
                tip_length=0.25
            )

            self.play(Write(num), Create(arrow))
            self.wait(2)
