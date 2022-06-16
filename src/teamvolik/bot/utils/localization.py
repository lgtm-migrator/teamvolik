"""Module imported functionality required for correct localization."""

import gettext

translation = gettext.translation("bot", "teamvolik/localization", fallback=True)
_, ngettext = translation.gettext, translation.ngettext