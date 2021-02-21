.. red commands module documentation

================
Commands Package
================

This package acts almost identically to :doc:`discord.ext.commands <dpy:ext/commands/api>`; i.e.
all of the attributes from discord.py's are also in ours. 
Some of these attributes, however, have been slightly modified, while others have been added to
extend functionalities used throughout the bot, as outlined below.

.. autofunction:: beastbot.core.commands.command

.. autofunction:: beastbot.core.commands.group

.. autoclass:: beastbot.core.commands.Cog

    .. automethod:: format_help_for_context
    
    .. automethod:: red_get_data_for_user
    
    .. automethod:: red_delete_data_for_user

.. autoclass:: beastbot.core.commands.Command
    :members:
    :inherited-members: format_help_for_context

.. autoclass:: beastbot.core.commands.Group
    :members:

.. autoclass:: beastbot.core.commands.Context
    :members:

.. autoclass:: beastbot.core.commands.GuildContext

.. autoclass:: beastbot.core.commands.DMContext

.. automodule:: beastbot.core.commands.requires
    :members: PrivilegeLevel, PermState, Requires

.. automodule:: beastbot.core.commands.converter
    :members:
    :exclude-members: UserInputOptional, convert
    :no-undoc-members:

    .. autodata:: UserInputOptional
        :annotation:

.. _framework-commands-help:

******************
Help Functionality
******************

.. warning::

    The content in this section is provisional and may change
    without prior notice or warning. Updates to this will be communicated
    on `this issue <https://github.com/Cog-Creators/Red-DiscordBot/issues/4084>`_


.. automodule:: beastbot.core.commands.help
    :members:
