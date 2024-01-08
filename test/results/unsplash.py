# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import unsplash


__tests__ = (
{
    "#url"     : "https://unsplash.com/photos/red-wooden-cross-on-gray-concrete-pathway-between-green-trees-during-daytime-kaoHI0iHJPM",
    "#category": ("", "unsplash", "image"),
    "#class"   : unsplash.UnsplashImageExtractor,
    "#urls"    : "https://images.unsplash.com/photo-1601823984263-b87b59798b70?ixid=M3wxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNzAwODY2NDE4fA&ixlib=rb-4.0.3",

    "alt_description": "red wooden cross on gray concrete pathway between green trees during daytime",
    "blur_hash"  : "LIAwhq%e4TRjXAIBMyt89GRj%fj[",
    "breadcrumbs": list,
    "color"      : "#0c2626",
    "created_at" : "2020-10-04T15:13:59Z",
    "date"       : "dt:2020-10-04 15:13:59",
    "description": None,
    "downloads"  : range(50000, 300000),
    "exif"       : {
        "aperture"     : "9",
        "exposure_time": "1/125",
        "focal_length" : "35.0",
        "iso"          : 800,
        "make"         : "SONY",
        "model"        : "ILCE-7M3",
        "name"         : "SONY, ILCE-7M3",
    },
    "extension"  : "jpg",
    "filename"   : "photo-1601823984263-b87b59798b70",
    "height"     : 5371,
    "id"         : "kaoHI0iHJPM",
    "liked_by_user": False,
    "likes"      : range(1000, 10000),
    "links"      : dict,
    "location"   : {
        "city"    : "箱根町",
        "country" : "日本",
        "name"    : "Hakone, 神奈川県 日本",
        "position": {
            "latitude" :  35.232383,
            "longitude": 139.106936,
        },
    },
    "meta"       : {
        "index": True,
    },
    "plus"       : False,
    "premium"    : False,
    "promoted_at": "2020-10-05T13:04:43Z",
    "public_domain": False,
    "slug"       : "red-wooden-cross-on-gray-concrete-pathway-between-green-trees-during-daytime-kaoHI0iHJPM",
    "sponsorship": None,
    "subcategory": "image",
    "tags"       : [
        "japan",
        "hakone",
        "神奈川県 日本",
        "torii",
        "hakone shrine",
        "sunrise",
        "traditional",
        "shrine",
        "grey",
        "wallpaper",
        "arbour",
        "garden",
        "outdoors",
        "gate",
    ],
    "tags_preview": list,
    "topic_submissions": {},
    "topics"     : [],
    "updated_at" : "2023-11-24T08:17:36Z",
    "urls": {
        "full"    : "https://images.unsplash.com/photo-1601823984263-b87b59798b70?crop=entropy&cs=srgb&fm=jpg&ixid=M3wxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNzAwODY2NDE4fA&ixlib=rb-4.0.3&q=85",
        "raw"     : "https://images.unsplash.com/photo-1601823984263-b87b59798b70?ixid=M3wxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNzAwODY2NDE4fA&ixlib=rb-4.0.3",
        "regular" : "https://images.unsplash.com/photo-1601823984263-b87b59798b70?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNzAwODY2NDE4fA&ixlib=rb-4.0.3&q=80&w=1080",
        "small"   : "https://images.unsplash.com/photo-1601823984263-b87b59798b70?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNzAwODY2NDE4fA&ixlib=rb-4.0.3&q=80&w=400",
        "small_s3": "https://s3.us-west-2.amazonaws.com/images.unsplash.com/small/photo-1601823984263-b87b59798b70",
        "thumb"   : "https://images.unsplash.com/photo-1601823984263-b87b59798b70?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNzAwODY2NDE4fA&ixlib=rb-4.0.3&q=80&w=200",
    },
    "user": {
        "accepted_tos"      : True,
        "bio"               : "Professional photographer.\r\nBased in Japan.",
        "first_name"        : "Syuhei",
        "for_hire"          : True,
        "id"                : "F4HO358YSeo",
        "instagram_username": "_______life_",
        "last_name"         : "Inoue",
        "links": {
            "followers": "https://api.unsplash.com/users/_______life_/followers",
            "following": "https://api.unsplash.com/users/_______life_/following",
            "html"     : "https://unsplash.com/@_______life_",
            "likes"    : "https://api.unsplash.com/users/_______life_/likes",
            "photos"   : "https://api.unsplash.com/users/_______life_/photos",
            "portfolio": "https://api.unsplash.com/users/_______life_/portfolio",
            "self"     : "https://api.unsplash.com/users/_______life_",
        },
        "location"          : "Yokohama, Japan",
        "name"              : "Syuhei Inoue",
        "portfolio_url"     : "https://syuheiinoue.life/",
        "profile_image"     : {
            "large" : "https://images.unsplash.com/profile-1601689368522-8855bbd61be6image?ixlib=rb-4.0.3&crop=faces&fit=crop&w=128&h=128",
            "medium": "https://images.unsplash.com/profile-1601689368522-8855bbd61be6image?ixlib=rb-4.0.3&crop=faces&fit=crop&w=64&h=64",
            "small" : "https://images.unsplash.com/profile-1601689368522-8855bbd61be6image?ixlib=rb-4.0.3&crop=faces&fit=crop&w=32&h=32",
        },
        "social"            : {
            "instagram_username": "_______life_",
            "paypal_email"      : None,
            "portfolio_url"     : "https://syuheiinoue.life/",
            "twitter_username"  : None,
        },
        "total_collections" : 2,
        "total_likes"       : 32,
        "total_photos"      : 86,
        "total_promoted_photos": 24,
        "twitter_username"  : None,
        "updated_at"        : "2023-11-24T19:15:32Z",
        "username"          : "_______life_"
    },
    "views": range(2000000, 10000000),
    "width": 3581,
},

{
    "#url"     : "https://unsplash.com/@_______life_",
    "#category": ("", "unsplash", "user"),
    "#class"   : unsplash.UnsplashUserExtractor,
    "#pattern" : r"https://images\.unsplash\.com/(photo-\d+-\w+|reserve/[^/?#]+)\?ixid=\w+&ixlib=rb-4\.0\.3$",
    "#range"   : "1-30",
    "#count"   : 30,
},

{
    "#url"     : "https://unsplash.com/@_______life_/likes",
    "#category": ("", "unsplash", "favorite"),
    "#class"   : unsplash.UnsplashFavoriteExtractor,
    "#pattern" : r"https://images\.unsplash\.com/(photo-\d+-\w+|reserve/[^/?#]+)\?ixid=\w+&ixlib=rb-4\.0\.3$",
    "#count"   : 31,
},

{
    "#url"     : "https://unsplash.com/collections/3178572/winter",
    "#category": ("", "unsplash", "collection"),
    "#class"   : unsplash.UnsplashCollectionExtractor,
    "#pattern" : r"https://images\.unsplash\.com/(photo-\d+-\w+|reserve/[^/?#]+)\?ixid=\w+&ixlib=rb-4\.0\.3$",
    "#range"   : "1-30",
    "#count"   : 30,

    "collection_id"   : "3178572",
    "collection_title": "winter",
},

{
    "#url"     : "https://unsplash.com/collections/3178572/",
    "#category": ("", "unsplash", "collection"),
    "#class"   : unsplash.UnsplashCollectionExtractor,
},

{
    "#url"     : "https://unsplash.com/collections/_8qJQ2bCMWE/2021.05",
    "#category": ("", "unsplash", "collection"),
    "#class"   : unsplash.UnsplashCollectionExtractor,
},

{
    "#url"     : "https://unsplash.com/s/photos/hair-style",
    "#category": ("", "unsplash", "search"),
    "#class"   : unsplash.UnsplashSearchExtractor,
    "#pattern" : r"https://(images|plus)\.unsplash\.com/((flagged/|premium_)?photo-\d+-\w+|reserve/[^/?#]+)\?ixid=\w+&ixlib=rb-4\.0\.3$",
    "#range"   : "1-30",
    "#count"   : 30,
},

)
