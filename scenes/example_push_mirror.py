"""Example episode scene: how a push reaches the public mirror.

Render with `make preview SCENE=scenes/example_push_mirror.py`.
"""

from manim import *

from scenes.common.style import ACCENT, ACCENT_2, MUTED, OK, WARN, box, label, title


class PushMirror(Scene):
    def construct(self):
        heading = title("From laptop to GitHub").scale(0.8).to_edge(UP)
        self.play(Write(heading))

        laptop = box("Laptop", ACCENT)
        forgejo = box("Forgejo", ACCENT_2)
        github = box("GitHub", OK)
        row = VGroup(laptop, forgejo, github).arrange(RIGHT, buff=2.0)
        self.play(LaggedStart(*(FadeIn(b, shift=UP * 0.3) for b in row), lag_ratio=0.3))

        push = Arrow(laptop.get_right(), forgejo.get_left(), buff=0.1, color=MUTED)
        mirror = Arrow(forgejo.get_right(), github.get_left(), buff=0.1, color=MUTED)
        push_label = label("git push", MUTED).next_to(push, UP, buff=0.2)
        mirror_label = label("push mirror", MUTED).next_to(mirror, UP, buff=0.2)

        gate = label("pre-push: gitleaks", WARN).next_to(laptop, DOWN, buff=0.4)
        self.play(FadeIn(gate))
        self.play(GrowArrow(push), FadeIn(push_label))

        commit = Dot(laptop.get_center(), color=ACCENT, radius=0.12)
        self.play(FadeIn(commit, scale=2))
        self.play(commit.animate.move_to(forgejo.get_center()), run_time=1.2)
        self.play(GrowArrow(mirror), FadeIn(mirror_label))
        self.play(commit.animate.move_to(github.get_center()), run_time=1.2)
        self.play(FadeOut(commit, scale=0.5), Indicate(github, color=OK))
        self.wait()
