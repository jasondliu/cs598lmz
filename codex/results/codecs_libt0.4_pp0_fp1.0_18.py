import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, StickerSendMessage, VideoSendMessage, AudioSendMessage,
    LocationMessage, QuickReply, QuickReplyButton,
    PostbackAction, DatetimePickerAction,
    CarouselColumn, CarouselTemplate,
    ButtonsTemplate, PostbackTemplateAction, MessageTemplateAction, URITemplateAction,
    TemplateSendMessage,
    ImagemapSendMessage, BaseSize,
    URIImagemapAction, MessageImagemapAction, ImagemapArea,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent,
)

from bs4 import BeautifulSoup
import requests
