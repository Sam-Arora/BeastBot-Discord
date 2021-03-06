import pytest
from beastbot.pytest.alias import *


def test_is_valid_alias_name(alias):
    assert alias.is_valid_alias_name("valid") is True
    assert alias.is_valid_alias_name("not valid name") is False


@pytest.mark.asyncio
async def test_empty_guild_aliases(alias, empty_guild):
    assert list(await alias._aliases.get_guild_aliases(empty_guild)) == []


@pytest.mark.asyncio
async def test_empty_global_aliases(alias):
    assert list(await alias._aliases.get_global_aliases()) == []


async def create_test_guild_alias(alias, ctx):
    await alias._aliases.add_alias(ctx, "test", "ping", global_=False)


async def create_test_global_alias(alias, ctx):
    await alias._aliases.add_alias(ctx, "test_global", "ping", global_=True)


@pytest.mark.asyncio
async def test_add_guild_alias(alias, ctx):
    await create_test_guild_alias(alias, ctx)

    alias_obj = await alias._aliases.get_alias(ctx.guild, "test")
    assert alias_obj.name == "test"


@pytest.mark.asyncio
async def test_delete_guild_alias(alias, ctx):
    await create_test_guild_alias(alias, ctx)
    alias_obj = await alias._aliases.get_alias(ctx.guild, "test")
    assert alias_obj.name == "test"

    did_delete = await alias._aliases.delete_alias(ctx, "test")
    assert did_delete is True

    alias_obj = await alias._aliases.get_alias(ctx.guild, "test")
    assert alias_obj is None


@pytest.mark.asyncio
async def test_add_global_alias(alias, ctx):
    await create_test_global_alias(alias, ctx)
    alias_obj = await alias._aliases.get_alias(ctx.guild, "test_global")

    assert alias_obj.name == "test_global"


@pytest.mark.asyncio
async def test_delete_global_alias(alias, ctx):
    await create_test_global_alias(alias, ctx)
    alias_obj = await alias._aliases.get_alias(ctx.guild, "test_global")
    assert alias_obj.name == "test_global"

    did_delete = await alias._aliases.delete_alias(ctx, alias_name="test_global", global_=True)
    assert did_delete is True

    alias_obj = await alias._aliases.get_alias(None, "test_global")
    assert alias_obj is None
