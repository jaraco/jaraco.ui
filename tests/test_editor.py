import subprocess

import pytest

from jaraco.ui import editor


def test_editor_launch_failure(monkeypatch, capsys):
    def fail(cmd):
        raise FileNotFoundError(cmd[0])

    monkeypatch.setattr(subprocess, 'call', fail)
    monkeypatch.setenv('EDITOR', 'no-such-editor')
    file = editor.EditableFile('foo')
    file.edit()
    out, _err = capsys.readouterr()
    assert 'Error launching editor no-such-editor' in out
    assert not file.changed


def test_editor_error_status(monkeypatch):
    monkeypatch.setattr(subprocess, 'call', lambda cmd: 3)
    monkeypatch.setenv('EDITOR', 'bad-editor')
    with pytest.raises(
        editor.EditProcessException, match='bad-editor returned error status 3'
    ):
        editor.EditableFile('foo').edit()
