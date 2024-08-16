import named
import typer


def main(func, app=typer.Typer(add_completion=False)):
    """
    Decorator and wrapper around typer to mark a function as main.

    For example:

    @main
    def run(...):
        ...

    Use of this decorator outside of the same module will not have
    the intended effect.
    """
    if named.get_module(func) == '__main__':
        app.command()(func)
        app()
    return func
