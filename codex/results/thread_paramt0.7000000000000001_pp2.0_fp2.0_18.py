import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

from gui import gui
import gui.gui_common as gui_common
import gui.gui_common_windows as gui_common_windows
import gui.gui_common_linux as gui_common_linux
import gui.gui_common_osx as gui_common_osx

from frontpage import frontpage
from frontpage.frontpage_common.video_class import Video
from frontpage.frontpage_common.trending import Trending

from videos import videos
from videos.videos_common.video_class import Video

from channels import channels
from channels.channels_common.channel_class import Channel
from channels.channels_common.videos import ChannelsVideos

from search import search
from search.search_common.search_class import Search
from search.search_common.search_results import SearchResults

from subscriptions import subscriptions
from subscriptions.subscriptions_common.subscriptions import Subscriptions

from account import account
