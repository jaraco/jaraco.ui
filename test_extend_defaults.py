import argparse

from jaraco.ui.cmdline import Extend


def test_extend_keeps_parser_defaults_and_previous_results():
    default = ['default']
    parser = argparse.ArgumentParser()
    parser.add_argument('--item', nargs='*', default=default, action=Extend)
    first = parser.parse_args(['--item', 'a', '--item', 'b'])
    second = parser.parse_args(['--item', 'c'])
    assert first.item == ['default', 'a', 'b']
    assert second.item == ['default', 'c']
    assert parser.parse_args([]).item == ['default']
    assert default == ['default']


def test_extend_without_explicit_default():
    parser = argparse.ArgumentParser()
    parser.add_argument('--item', nargs='*', action=Extend)
    assert parser.parse_args(['--item', 'a', '--item', 'b']).item == ['a', 'b']
