import json
from pytchat.parser.live import Parser
from pytchat.processors.compatible.processor import CompatibleProcessor

parser = Parser(is_replay=False)

root_keys = ('kind', 'etag', 'nextPageToken', 'pollingIntervalMillis', 'pageInfo', 'items')
item_keys = ('kind', 'etag', 'id', 'snippet', 'authorDetails')
snippet_keys = ('type', 'liveChatId', 'authorChannelId', 'publishedAt', 'hasDisplayContent', 'displayMessage', 'textMessageDetails')
author_details_keys = ('channelId', 'channelUrl', 'displayName', 'profileImageUrl', 'isVerified', 'isChatOwner', 'isChatSponsor', 'isChatModerator')

def test_compatible_processor():
    processor = CompatibleProcessor()

    with open("tests/testdata/compatible/textmessage.json", mode='r', encoding='utf-8') as f:
        _json = f.read()

    _, chatdata = parser.parse(parser.get_contents(json.loads(_json))[0])
    data = {
        "video_id": "",
        "timeout": 7,
        "chatdata": chatdata
    }
    ret = processor.process([data])

    for key in ret.keys():
        assert key in root_keys
    for key in ret["items"][0].keys():
        assert key in item_keys
    for key in ret["items"][0]["snippet"].keys():
        assert key in snippet_keys
    for key in ret["items"][0]["authorDetails"].keys():
        assert key in author_details_keys
