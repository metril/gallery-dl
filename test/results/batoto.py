# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import batoto
from gallery_dl import exception

__tests__ = (
{
    "#url"     : "https://bato.to/title/86408-i-shall-master-this-family-official/1681030-ch_8",
    "#category": ("", "batoto", "chapter"),
    "#class"   : batoto.BatotoChapterExtractor,
    "#count"   : 66,

    "chapter"      : 8,
    "chapter_id"   : 1681030,
    "chapter_minor": "",
    "count"        : 66,
    "date"         : "dt:2021-05-15 18:51:37",
    "extension"    : "webp",
    "filename"     : str,
    "manga"        : "I Shall Master this Family! [Official]",
    "manga_id"     : 86408,
    "page"         : range(1, 66),
    "title"        : "Observing",
    "volume"       : 0,

},

{
    "#url"     : "https://bato.to/title/104929-86-eighty-six-official/1943513-vol_1-ch_5",
    "#comment" : "volume (vol) in url",
    "#category": ("", "batoto", "chapter"),
    "#class"   : batoto.BatotoChapterExtractor,
    "#count"   : 7,

    "manga"  : "86--EIGHTY-SIX (Official)",
    "title"  : "The Spearhead Squadron's Power",
    "volume" : 1,
    "chapter": 5,
},

{
    "#url"     : "https://bato.to/title/113742-futsutsuka-na-akujo-de-wa-gozaimasu-ga-suuguu-chouso-torikae-den-official",
    "#category": ("", "batoto", "manga"),
    "#class"   : batoto.BatotoMangaExtractor,
    "#count"   : ">= 21",

    "chapter"      : int,
    "chapter_minor": str,
    "date"         : "type:datetime",
    "manga"        : "Futsutsuka na Akujo de wa Gozaimasu ga - Suuguu Chouso Torikae Den (Official)",
    "manga_id"     : 113742,
},

{
    "#url"     : "https://bato.to/title/104929-86-eighty-six-official",
    "#comment" : "Manga with number in name",
    "#category": ("", "batoto", "manga"),
    "#class"   : batoto.BatotoMangaExtractor,
    "#count"   : ">= 18",

    "manga": "86--EIGHTY-SIX (Official)",
},

{
    "#url"     : "https://bato.to/title/140046-the-grand-duke-s-fox-princess-mgchan",
    "#comment" : "Non-English translation (Indonesian)",
    "#category": ("", "batoto", "manga"),
    "#class"   : batoto.BatotoMangaExtractor,
    "#count"   : ">= 29",

    "manga": "The Grand Duke’s Fox Princess ⎝⎝MGCHAN⎠⎠",
},

{
    "#url"     : "https://bato.to/title/134270-removed",
    "#comment" : "Deleted/removed manga",
    "#category": ("", "batoto", "manga"),
    "#class"   : batoto.BatotoMangaExtractor,
    "#exception": exception.StopExtraction,
},

{
    "#url"     : "https://bato.to/title/86408/1681030",
    "#category": ("", "batoto", "chapter"),
    "#class"   : batoto.BatotoChapterExtractor,
},

{
    "#url"     : "https://bato.to/chapter/1681030",
    "#category": ("", "batoto", "chapter"),
    "#class"   : batoto.BatotoChapterExtractor,
},

{
    "#url"     : "https://dto.to/title/86408/1681030",
    "#category": ("", "batoto", "chapter"),
    "#class"   : batoto.BatotoChapterExtractor,
},

{
    "#url"     : "https://wto.to/title/86408/1681030",
    "#category": ("", "batoto", "chapter"),
    "#class"   : batoto.BatotoChapterExtractor,
},

{
    "#url"     : "https://batotoo.com/title/86408/1681030",
    "#category": ("", "batoto", "chapter"),
    "#class"   : batoto.BatotoChapterExtractor,
},

{
    "#url"     : "https://mangatoto.com/title/86408/1681030",
    "#category": ("", "batoto", "chapter"),
    "#class"   : batoto.BatotoChapterExtractor,
},

{
    "#url"     : "https://bato.to/title/86408-i-shall-master-this-family-official",
    "#category": ("", "batoto", "manga"),
    "#class"   : batoto.BatotoMangaExtractor,
},

{
    "#url"     : "https://bato.to/series/86408/i-shall-master-this-family-official",
    "#category": ("", "batoto", "manga"),
    "#class"   : batoto.BatotoMangaExtractor,
},

)
