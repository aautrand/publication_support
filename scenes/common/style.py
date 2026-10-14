"""Shared look for every video, so episodes stay visually consistent."""

from manim import *

BG = "#0f1117"
TEXT = "#e6e6e6"
MUTED = "#8b93a7"
ACCENT = "#4fc3f7"
ACCENT_2 = "#ffb74d"
OK = "#81c784"
WARN = "#e57373"

FONT = "Helvetica Neue"
MONO = "Menlo"


def title(text: str, **kwargs) -> Text:
    return Text(text, font=FONT, color=TEXT, weight=BOLD, **kwargs)


def label(text: str, color: str = TEXT, **kwargs) -> Text:
    return Text(text, font=FONT, color=color, **kwargs).scale(0.5)


def box(text: str, color: str = ACCENT, width: float = 2.2) -> VGroup:
    """A rounded box with a centred label, used for components in diagrams."""
    rect = RoundedRectangle(corner_radius=0.15, width=width, height=1.0, color=color)
    rect.set_fill(color, opacity=0.12)
    return VGroup(rect, label(text).move_to(rect))
