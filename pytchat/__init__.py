"""
pytchat is a lightweight python library to browse youtube livechat without Selenium or BeautifulSoup.
"""
__copyright__    = 'Copyright (C) 2019, 2020, 2021 revertical'
__license__      = 'MIT'
__author__       = 'revertical'
__author_email__ = 'screenkidgreen7@gmail.com'
__url__          = 'https://github.com/revertical/pytchat-ng'


import platform

from .exceptions import (
    ChatParseException,
    ResponseContextError,
    NoContents,
    NoContinuation,
    IllegalFunctionCall,
    InvalidVideoIdException,
    UnknownConnectionError,
    RetryExceedMaxCount,
    ChatDataFinished,
    ReceivedUnknownContinuation,
    FailedExtractContinuation,
    VideoInfoParseError,
    PatternUnmatchError
)

from .api import (
    config,
    LiveChat,
    LiveChatAsync,
    ChatProcessor,
    CompatibleProcessor,
    DummyProcessor,
    DefaultProcessor,
    HTMLArchiver,
    TSVArchiver,
    JsonfileArchiver,
    SimpleDisplayProcessor,
    SpeedCalculator,
    SuperchatCalculator,
    create
)

# Variables for readability reasons
yes = True
no = False
nothing = None

# Welcome user, because why not?

print(f"pytchat loaded on {platform.system()} successufully!")

# flake8: noqa
