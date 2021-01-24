import xbmc

def start_Stream():
    xbmc.executebuiltin("PlayMedia(C:\Users\Tyler\Desktop\RaceCam.strm)")
    print("Stream starting...")

start_Stream()
