from manim import *

class RSAMailbox(Scene):
    def construct(self):
        # Background color
        self.camera.background_color = "#27272A"

        # Characters
        alice = Text("Alice", color=BLUE, font="KH Interference Trial").to_edge(LEFT)
        bob = Text("Bob", color=GREEN, font="KH Interference Trial").to_edge(RIGHT)

        # Mailbox
        mailbox = Rectangle(width=2, height=1.5, color=YELLOW).shift(DOWN*0.5)

        # Message (single object)
        message = Text("HELLO", color=WHITE, font_size=24, font="KH Interference Trial").next_to(alice, UP)

        # Hacker image (small) – start from ABOVE
        hacker_img = ImageMobject("media/images/main/anonymous.png").scale(0.30)
        hacker_img.move_to(UP*3.2)

        # Question mark (LaTeX version, with z-index, placed clearly at (2,2))
        qmark = Tex("?", color=RED, font_size=80).move_to([1.1, 1, 0])
        qmark.set_opacity(0).set_z_index(10)

        # --- Animation ---
        self.play(Write(alice), Write(bob), FadeIn(mailbox))
        self.play(Write(message))

        # Encrypt + move to mailbox
        encrypted = Text("ENCRYPTED", color=ORANGE, font_size=24, font="KH Interference Trial").scale(0.8).move_to(message.get_center())
        self.play(Transform(message, encrypted))
        self.play(message.animate.move_to(mailbox.get_center()), run_time=0.9)
        
        # Hacker comes from above
        target_pos = mailbox.get_top() + UP*0.7
        self.play(FadeIn(hacker_img))
        self.play(hacker_img.animate.move_to(target_pos), run_time=0.9)

        # Show "?" AFTER hacker stops
        self.play(qmark.animate.set_opacity(1), run_time=0.5)
        self.wait(0.3)

        # Decrypt to Bob
        decrypted = Text("HELLO", color=WHITE, font_size=24, font="KH Interference Trial").next_to(bob, UP)
        self.play(Transform(message, decrypted), run_time=1.0)
        self.wait(2)
