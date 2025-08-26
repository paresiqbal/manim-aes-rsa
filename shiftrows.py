from manim import *

class AESShiftRows(Scene):
    def construct(self):
        self.camera.background_color = "#27272A"
        side = 0.7  

        # --- S-Box results (input to ShiftRows) ---
        sbox_results = [
            "01","C5","76","30",
            "67","82","30","A2",
            "D7","D6","B3","29",
            "E3","2F","84","53"
        ]

        # Build grid
        boxes = VGroup()
        for hex_val in sbox_results:
            sq = Square(side_length=side)
            sq.set_fill(PINK, opacity=1)
            sq.set_stroke(WHITE, width=2)
            txt = Text(hex_val, font="KH Interference Trial", font_size=28, color=BLACK)
            box = VGroup(sq, txt)
            boxes.add(box)
        boxes.arrange_in_grid(rows=4, cols=4, buff=0.07, cell_alignment=ORIGIN)
        boxes.move_to(ORIGIN)

        # --- Intro animation (fade in one by one) ---
        self.play(
            LaggedStart(
                *[FadeIn(b, shift=DOWN, run_time=0.6) for b in boxes],
                lag_ratio=0.15
            )
        )
        self.wait(1)

        # Save grid positions
        positions = [b.get_center() for b in boxes]

        # --- ShiftRows Animation ---
        # Row 0 (unchanged)
        self.wait(0.5)

        # Row 1 (shift left by 1)
        row1_indices = [4,5,6,7]
        row1_shifted = [boxes[5], boxes[6], boxes[7], boxes[4]]
        self.play(*[
            box.animate.move_to(positions[i])
            for box, i in zip(row1_shifted, row1_indices)
        ], run_time=1.2)
        self.wait(0.8)

        # Row 2 (shift left by 2)
        row2_indices = [8,9,10,11]
        row2_shifted = [boxes[10], boxes[11], boxes[8], boxes[9]]
        self.play(*[
            box.animate.move_to(positions[i])
            for box, i in zip(row2_shifted, row2_indices)
        ], run_time=1.2)
        self.wait(0.8)

        # Row 3 (shift left by 3)
        row3_indices = [12,13,14,15]
        row3_shifted = [boxes[15], boxes[12], boxes[13], boxes[14]]
        self.play(*[
            box.animate.move_to(positions[i])
            for box, i in zip(row3_shifted, row3_indices)
        ], run_time=1.2)
        self.wait(2)
