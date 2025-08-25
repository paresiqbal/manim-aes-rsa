from manim import *

class AESInput(Scene):
    def construct(self):
        self.camera.background_color = "#27272A"

        # --- First row: HELLOWORD ---
        word = "HELLOWORD"
        total_boxes = 16
        boxes = VGroup()
        side = 0.5

        for i in range(total_boxes):
            sq = Square(side_length=side)
            sq.set_fill(GREEN, opacity=1)
            sq.set_stroke(WHITE, width=2)

            if i < len(word):
                txt = Text(word[i], font_size=24, color=BLACK, font="KH Interference Trial")
                box = VGroup(sq, txt)
            else:
                box = VGroup(sq)  # keep empty for now

            boxes.add(box)

        boxes.arrange(RIGHT, buff=0.07)
        boxes.move_to([0, 1, 0])

        # Animate first row
        self.play(
            LaggedStart(
                *[FadeIn(b, shift=DOWN, run_time=0.5) for b in boxes],
                lag_ratio=0.07
            )
        )
        self.wait(1)

        # --- Second row: Key A–P ---
        key_letters = "ABCDEFGHIJKLMNOP"
        key_boxes = VGroup()

        for i in range(total_boxes):
            sq = Square(side_length=side)
            sq.set_fill(YELLOW, opacity=1)
            sq.set_stroke(WHITE, width=2)

            txt = Text(key_letters[i], font_size=24, color=BLACK, font="KH Interference Trial")
            box = VGroup(sq, txt)

            key_boxes.add(box)

        key_boxes.arrange(RIGHT, buff=0.07)
        key_boxes.move_to([0, 0, 0])  # placed below first row

        # Animate key row
        self.play(
            LaggedStart(
                *[FadeIn(b, shift=UP, run_time=0.5) for b in key_boxes],
                lag_ratio=0.07
            )
        )
        self.wait(1)

        # --- Fill empty message squares with "00" ---
        fill_anims = []
        for i in range(len(word), total_boxes):
            txt = Text("00", font_size=20, color=BLACK, font="KH Interference Trial")
            txt.scale(0.1)  # start tiny
            txt.move_to(boxes[i][0])  
            boxes[i].add(txt)
            fill_anims.append(ScaleInPlace(txt, 10, run_time=0.3))  # grow effect

        self.play(LaggedStart(*fill_anims, lag_ratio=0.15))
        self.wait(2)

        # --- Convert to ASCII values ---
        ascii_word = ["48", "45", "4C", "4C", "4F", "57", "4F", "52", "44", "00", "00", "00", "00", "00", "00", "00"]
        ascii_key = ["41", "42", "43", "44", "45", "46", "47", "48", "49", "4A", "4B", "4C", "4D", "4E", "4F", "50"]

        word_changes = [
            Transform(boxes[i][1], Text(ascii_word[i], font_size=18, color=BLACK, font="KH Interference Trial").move_to(boxes[i][0]))
            for i in range(total_boxes)
        ]
        key_changes = [
            Transform(key_boxes[i][1], Text(ascii_key[i], font_size=18, color=BLACK, font="KH Interference Trial").move_to(key_boxes[i][0]))
            for i in range(total_boxes)
        ]

        self.play(LaggedStart(*word_changes, lag_ratio=0.1))
        self.play(LaggedStart(*key_changes, lag_ratio=0.1))
        self.wait(2)
