"""
Example on how to use the YouTube Controller

"""

import pychromecast_master.pychromecast as pychromecast
from pychromecast_master.pychromecast.controllers.youtube import YouTubeController


# Change to the video id of the YouTube video
# video id is the last part of the url http://youtube.com/watch?v=video_id

def youtube_player(VIDEO_ID):
    # Change to the name of your Chromecast
    CAST_NAME = "Bedroom TV"

    chromecasts = pychromecast.get_chromecasts()
    cast = next(cc for cc in chromecasts if cc.device.friendly_name == CAST_NAME)
    cast.wait()
    yt = YouTubeController()
    cast.register_handler(yt)
    yt.play_video(VIDEO_ID)
