import xbmc

def start_Stream():
    xbmc.executebuiltin("PlayMedia(C:\Users\Example\Desktop\Example.strm)")
    print("Stream starting...")

start_Stream()
