from .cleanup import Cleanup
from beastbot.core.bot import Red


def setup(bot: Red):
    bot.add_cog(Cleanup(bot))
