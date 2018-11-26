# -*- coding: utf-8 -*-
"""Init and utils."""
from affinitic.ploneintranet.patch import html_cleaner_patch
from ploneintranet.workspace import html_cleaners
from zope.i18nmessageid import MessageFactory


html_cleaner_patch(html_cleaners)


_ = MessageFactory('affinitic.ploneintranet')
