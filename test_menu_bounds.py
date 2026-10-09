import pytest

from jaraco.ui.menu import Menu


@pytest.mark.parametrize('answer', ['0', '-1', '-2', '4', 'invalid'])
def test_reject_out_of_range_choices(answer, monkeypatch, capsys):
    menu = Menu(['first', 'second', 'third'])
    monkeypatch.setattr('builtins.input', lambda prompt: answer)
    assert menu.get_choice() is None
    assert 'invalid selection' in capsys.readouterr().out


@pytest.mark.parametrize(('answer', 'expected'), [('1', 'first'), ('3', 'third')])
def test_valid_choice_bounds(answer, expected, monkeypatch):
    menu = Menu(['first', 'second', 'third'])
    monkeypatch.setattr('builtins.input', lambda prompt: answer)
    assert menu.get_choice() == expected
