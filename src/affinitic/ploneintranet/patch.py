# -*- coding: utf-8 -*-


def html_cleaner_patch(cleaner):
    cleaner.DocumentCleaner.allow_tags.append('pre')
    cleaner.DocumentCleaner.allow_tags.append('code')
