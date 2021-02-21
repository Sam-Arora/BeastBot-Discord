import pytest

from beastbot.cogs.alias import Alias
from beastbot.core import Config

__all__ = ["alias"]


@pytest.fixture()
def alias(config, monkeypatch):
    with monkeypatch.context() as m:
        m.setattr(Config, "get_conf", lambda *args, **kwargs: config)
        return Alias(None)
