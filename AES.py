from manim import *

class Blocks4x4(Scene):
    def construct(self):
        self.camera.background_color = "#27272A"

        # Phase 1: single square
        single = Square(
            side_length=1.2,
            color=WHITE, stroke_width=3,
            fill_color=GREEN, fill_opacity=1
        )
        self.play(Create(single, run_time=2))
        self.wait(1)
        self.play(FadeOut(single, run_time=1))

        # Phase 1: first grid
        cell_size = 0.7 
        gap = 0.20      

        grid1 = VGroup(*[
            Square(
                side_length=cell_size,
                color=WHITE, stroke_width=3,
                fill_color=GREEN, fill_opacity=1
            ) for _ in range(16)
        ]).arrange_in_grid(rows=4, cols=4, buff=gap)

        self.play(
            LaggedStart(
                *[FadeIn(sq, run_time=0.6) for sq in grid1],
                lag_ratio=0.08
            )
        )
        self.wait(1)

        # Phase 2: second green grid appears
        grid2 = VGroup(*[
            Square(
                side_length=cell_size,
                color=WHITE, stroke_width=3,
                fill_color=GREEN, fill_opacity=1
            ) for _ in range(16)
        ]).arrange_in_grid(rows=4, cols=4, buff=gap)

        grid1_target = grid1.copy().shift(LEFT * 2.5)
        grid2.move_to(RIGHT * 2.5)

        self.play(
            Transform(grid1, grid1_target),
            FadeIn(grid2, run_time=1)
        )
        self.wait(1)

        # Phase 3: replace grid2 with yellow grid & add XOR
        grid3 = VGroup(*[
            Square(
                side_length=cell_size,
                color=WHITE, stroke_width=3,
                fill_color=YELLOW, fill_opacity=1
            ) for _ in range(16)
        ]).arrange_in_grid(rows=4, cols=4, buff=gap)
        grid3.move_to(RIGHT * 2.5)

        xor_text = Text("XOR", font_size=30, color=WHITE, font="KH Interference Trial")
        xor_text.scale(0.1)  # start tiny
        xor_text.set_opacity(0)  # invisible at first

        self.play(
            FadeOut(grid2, run_time=1),
            FadeIn(grid3, run_time=1),
            xor_text.animate.set_opacity(1).scale(10),  # fade in & grow to normal
            run_time=1.5
        )
        self.wait(2)
