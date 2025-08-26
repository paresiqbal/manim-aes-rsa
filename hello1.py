from manim import *

class AESGrid(Scene):
    def construct(self):
        self.camera.background_color = "#27272A"

        side = 0.7  

        # --- Message (ASCII HELLOWORD + padding 00) ---
        message_hex = ["48","45","4C","4C","4F","57","4F","52","44"] + ["00"]*7
        message_boxes = VGroup()
        for hex_val in message_hex:
            sq = Square(side_length=side)
            sq.set_fill(GREEN, opacity=1)
            sq.set_stroke(WHITE, width=2)
            txt = Text(hex_val, font="KH Interference Trial", font_size=28, color=BLACK)
            box = VGroup(sq, txt)
            message_boxes.add(box)
        message_boxes.arrange_in_grid(rows=4, cols=4, buff=0.07, cell_alignment=ORIGIN)
        message_boxes.move_to(LEFT*3)

        # --- Key (ASCII A–P) ---
        key_hex = ["41","42","43","44","45","46","47","48",
                   "49","4A","4B","4C","4D","4E","4F","50"]
        key_boxes = VGroup()
        for hex_val in key_hex:
            sq = Square(side_length=side)
            sq.set_fill(YELLOW, opacity=1)
            sq.set_stroke(WHITE, width=2)
            txt = Text(hex_val, font="KH Interference Trial", font_size=28, color=BLACK)
            box = VGroup(sq, txt)
            key_boxes.add(box)
        key_boxes.arrange_in_grid(rows=4, cols=4, buff=0.07, cell_alignment=ORIGIN)
        key_boxes.move_to(RIGHT*3)

        # --- Ciphered Text (Pink) ---
        cipher_hex = [
            "09","07","0F","08",
            "0A","11","08","1A",
            "0D","4A","4B","4C",
            "4D","4E","4F","50"
        ]
        cipher_boxes = VGroup()
        for hex_val in cipher_hex:
            sq = Square(side_length=side)
            sq.set_fill(PINK, opacity=1)
            sq.set_stroke(WHITE, width=2)
            txt = Text(hex_val, font="KH Interference Trial", font_size=28, color=BLACK)
            box = VGroup(sq, txt)
            cipher_boxes.add(box)
        cipher_boxes.arrange_in_grid(rows=4, cols=4, buff=0.07, cell_alignment=ORIGIN)
        cipher_boxes.move_to(LEFT*3)  # Same position as message

        # --- Animations ---
        # Slower intro
        self.play(
            LaggedStart(
                *[FadeIn(b, shift=DOWN, run_time=0.6) for b in message_boxes],
                lag_ratio=0.15
            )
        )
        self.play(
            LaggedStart(
                *[FadeIn(b, shift=DOWN, run_time=0.6) for b in key_boxes],
                lag_ratio=0.15
            )
        )
        self.wait(2)

        # Move key onto plaintext
        self.play(key_boxes.animate.move_to(message_boxes.get_center()), run_time=1.5)

        # Both disappear
        self.play(FadeOut(message_boxes), FadeOut(key_boxes), run_time=1)

        # Cipher text appears all at once (no sliding)
        self.play(FadeIn(cipher_boxes, run_time=1.2))
        self.wait(2)

     # Cipher text appears all at once (no sliding)
        self.play(FadeIn(cipher_boxes, run_time=1.2))
        self.wait(2)

        # --- Replace with S-Box results (correct values) ---
        sbox_results = [
            "01","C5","76","30",
            "67","82","30","A2",
            "D7","D6","B3","29",
            "E3","2F","84","53"
        ]

        anims = []
        for box, new_val in zip(cipher_boxes, sbox_results):
            old_text = box[1]  # box = VGroup(square, text)
            new_text = Text(new_val, font="KH Interference Trial", font_size=28, color=BLACK)
            new_text.move_to(old_text.get_center())
            anims.append(Transform(old_text, new_text))

        self.play(*anims, run_time=1.5)
        self.wait(2)

           # --- Move S-Box result to center ---
        self.play(cipher_boxes.animate.move_to(ORIGIN), run_time=1.5)
        self.wait(1)

        # --- ShiftRows animation ---
        # Current order (row by row in 4x4 grid):
        # 01 C5 76 30
        # 67 82 30 A2
        # D7 D6 B3 29
        # E3 2F 84 53

        # Shifted order:
        # 01 C5 76 30       (no change)
        # 82 30 A2 67       (shift left 1)
        # B3 29 D7 D6       (shift left 2)
        # 53 E3 2F 84       (shift left 3)

        # Store the target positions of the grid
        positions = [box.get_center() for box in cipher_boxes]

        # Rearranged boxes (ShiftRows effect)
        shifted_order = [
            cipher_boxes[0], cipher_boxes[1], cipher_boxes[2], cipher_boxes[3],
            cipher_boxes[5], cipher_boxes[6], cipher_boxes[7], cipher_boxes[4],
            cipher_boxes[10], cipher_boxes[11], cipher_boxes[8], cipher_boxes[9],
            cipher_boxes[15], cipher_boxes[12], cipher_boxes[13], cipher_boxes[14],
        ]

        # Animate each box moving to its new spot
        self.play(*[
            box.animate.move_to(pos)
            for box, pos in zip(shifted_order, positions)
        ], run_time=1.8)

        self.wait(2)