from manim import *

class BlockEncryptionChange(Scene):
    def construct(self):
        self.camera.background_color = "#27272A"

        # Helper: square with text
        def make_block(text, color):
            rect = Square(side_length=1.2, color=WHITE, fill_color=color, fill_opacity=0.9)
            label = Text(
                text,
                color=BLACK,
                font_size=48,
                font="KH Interference Trial"
            )
            return VGroup(rect, label)

        # HELLO (green row)
        word_blocks = VGroup(*[make_block(ch, GREEN) for ch in "HELLO"])
        word_blocks.arrange(RIGHT, buff=0.25).to_edge(UP, buff=1)

        # Key 11001 (yellow row)
        key_blocks = VGroup(*[make_block(ch, YELLOW) for ch in "11001"])
        key_blocks.arrange(RIGHT, buff=0.25).next_to(word_blocks, DOWN, buff=0.8)

        # Cipher Q\UUV (pink row)
        enc_blocks = VGroup(*[make_block(ch, PINK) for ch in "Q\\UUV"])
        enc_blocks.arrange(RIGHT, buff=0.25).next_to(key_blocks, DOWN, buff=0.8)

        # Show all instantly
        self.add(word_blocks, key_blocks, enc_blocks)
        self.wait(1)

        # Step 1: change plaintext "E" → "O" (2nd block, index 1)
        new_O = Text("O", color=BLACK, font_size=48, font="KH Interference Trial")
        new_O.move_to(word_blocks[1][1].get_center())
        self.play(Transform(word_blocks[1][1], new_O))
        self.wait(1)

        # Step 2: change half of cipher text → "XYZ" + keep last 2 "UV"
        new_enc_blocks = VGroup(
            make_block("X", PINK),
            make_block("Y", PINK),
            make_block("Z", PINK),
            make_block("U", PINK),
            make_block("V", PINK),
        )
        new_enc_blocks.arrange(RIGHT, buff=0.25).move_to(enc_blocks)

        self.play(Transform(enc_blocks, new_enc_blocks))
        self.wait(2)
