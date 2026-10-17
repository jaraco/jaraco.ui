from jaraco.ui import menu


def test_menu_defaults_to_no_choices():
    assert menu.Menu().choices == []
