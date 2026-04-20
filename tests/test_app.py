import re

from second_brain.app import main


def test_main_logs_greeting(capfd, monkeypatch):
    monkeypatch.setattr("sys.argv", ["second_brain"])
    main()
    captured = capfd.readouterr()
    pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \| I \| .+ \| Hello from second_brain!"
    assert re.search(pattern, captured.err)
