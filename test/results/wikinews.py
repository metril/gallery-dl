# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import wikimedia


__tests__ = (
{
    "#url"     : "https://www.wikinews.org/wiki/Title",
    "#category": ("wikimedia", "wikinews", "article"),
    "#class"   : wikimedia.WikimediaArticleExtractor,
},

{
    "#url"     : "https://en.wikinews.org/wiki/Category:Title",
    "#category": ("wikimedia", "wikinews", "category"),
    "#class"   : wikimedia.WikimediaArticleExtractor,
},

)
