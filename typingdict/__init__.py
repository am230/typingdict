from .__version__ import __version__
from .typer import Typer


def typerify(code: dict) -> str:
    return Typer().typerify("Root", code)
