from manim import *

class BlockEncryption(Scene):
    def construct(self):
        self.camera.background_color = "#27272A"

        # Helper: square with text
        def make_block(text, color):
            rect = Square(side_length=1.2, color=WHITE, fill_color=color, fill_opacity=0.9)
            label = Text(
                text,
                color=BLACK,
                font_size=48,              # bigger letters (used to be 36)
                font="KH Interference Trial"  # custom font
            )
            return VGroup(rect, label)

        # HELLO (green row)
        word_blocks = VGroup(*[make_block(ch, GREEN) for ch in "HELLO"])
        word_blocks.arrange(RIGHT, buff=0.25).to_edge(UP, buff=1)

        # Key 11001 (yellow row)
        key_blocks = VGroup(*[make_block(ch, YELLOW) for ch in "11001"])
        key_blocks.arrange(RIGHT, buff=0.25).next_to(word_blocks, DOWN, buff=0.8)

        # Encrypted Q\UUV (pink row)
        enc_blocks = VGroup(*[make_block(ch, PINK) for ch in "Q\\UUV"])
        enc_blocks.arrange(RIGHT, buff=0.25).next_to(key_blocks, DOWN, buff=0.8)

        # Wait 1s then show all instantly
        self.wait(1)
        self.add(word_blocks, key_blocks, enc_blocks)
        self.wait(1)

        # Step 1: change first key bit "1" → "0"
        new_first_bit = Text(
            "0", color=BLACK, font_size=48, font="KH Interference Trial"
        )
        new_first_bit.move_to(key_blocks[0][1].get_center())
        self.play(Transform(key_blocks[0][1], new_first_bit))
        self.wait(1)

        # Step 2: change entire cipher row to "X5KLH"
        new_enc_blocks = VGroup(*[make_block(ch, PINK) for ch in "X5KLH"])
        new_enc_blocks.arrange(RIGHT, buff=0.25).move_to(enc_blocks)
        self.play(Transform(enc_blocks, new_enc_blocks))
        self.wait(2)
