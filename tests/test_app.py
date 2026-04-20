import re

from second_brain.app import build_parser, main

_LOG_PREFIX = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \| I \| .+ \| "


def _log_pattern(msg: str) -> str:
    return _LOG_PREFIX + re.escape(msg)


def test_main_logs_default_greeting(capfd, monkeypatch):
    monkeypatch.setattr("sys.argv", ["second_brain"])
    main()
    captured = capfd.readouterr()
    assert re.search(_log_pattern("Hello from second_brain!"), captured.err)


def test_main_logs_custom_message(capfd, monkeypatch):
    monkeypatch.setattr("sys.argv", ["second_brain", "--message", "My custom message"])
    main()
    captured = capfd.readouterr()
    assert re.search(_log_pattern("My custom message"), captured.err)


def test_build_parser_default_message():
    parser = build_parser()
    args = parser.parse_args([])
    assert args.message == "Hello from second_brain!"


def test_build_parser_custom_message():
    parser = build_parser()
    args = parser.parse_args(["--message", "Custom"])
    assert args.message == "Custom"
