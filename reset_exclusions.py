#!/usr/bin/python
# -*- coding: utf-8 -*-

import xbmcaddon
import xbmcgui
import utils

# Addon info
__addonID__ = "script.filecleaner"
__addon__ = xbmcaddon.Addon(__addonID__)


def reset_exclusions():
    """
    Reset all user-set exclusion paths to blanks.
    :return:
    """
    if xbmcgui.Dialog().yesno(utils.translate(32604), utils.translate(32610), utils.translate(32607)):
        __addon__.setSetting(id="exclusion1", value="")
        __addon__.setSetting(id="exclusion2", value="")
        __addon__.setSetting(id="exclusion3", value="")
		__addon__.setSetting(id="exclusion4", value="")
		__addon__.setSetting(id="exclusion5", value="")
		__addon__.setSetting(id="exclusion6", value="")
		__addon__.setSetting(id="exclusion7", value="")
		__addon__.setSetting(id="exclusion8", value="")
		__addon__.setSetting(id="exclusion9", value="")
		__addon__.setSetting(id="exclusion10", value="")

reset_exclusions()
