.. red's core utils documentation

=================
Utility Functions
=================

General Utility
===============

.. automodule:: beastbot.core.utils
    :members: deduplicate_iterables, bounded_gather, bounded_gather_iter, get_end_user_data_statement, get_end_user_data_statement_or_raise

.. autoclass:: AsyncIter
    :members:
    :special-members: __await__
    :exclude-members: enumerate, filter

    .. automethod:: enumerate
        :async-for:

    .. automethod:: filter
        :async-for:


Chat Formatting
===============

.. automodule:: beastbot.core.utils.chat_formatting
    :members:

Embed Helpers
=============

.. automodule:: beastbot.core.utils.embed
    :members:
    :exclude-members: randomize_color

Reaction Menus
==============

.. automodule:: beastbot.core.utils.menus
    :members:

Event Predicates
================

MessagePredicate
****************

.. autoclass:: beastbot.core.utils.predicates.MessagePredicate
    :members:

ReactionPredicate
*****************

.. autoclass:: beastbot.core.utils.predicates.ReactionPredicate
    :members:

Mod Helpers
===========

.. automodule:: beastbot.core.utils.mod
    :members:

Tunnel
======

.. automodule:: beastbot.core.utils.tunnel
    :members: Tunnel

Common Filters
==============

.. automodule:: beastbot.core.utils.common_filters
    :members:
