import time
import xbmc

if __name__ == '__main__':
    monitor = xbmc.Monitor()

    while not monitor.abortRequested():
        # Sleep/wait for abort for 10 seconds
        if monitor.waitForAbort(10):
            # Abort was requested while waiting. We should exit
            break
        if xbmc.Player().isPlaying() == True:
            #TotalTime = xbmc.Player().getTotalTime() Doesn't work too lazy
            xbmc.log("Stream already running. Ignoring...", level=xbmc.LOGNOTICE)
            #xbmc.log(str(TotalTime), level=xbmc.LOGNOTICE) Doesn't work still too lazy
        else:
            xbmc.executebuiltin("PlayMedia(Path to .strm)")
            xbmc.log("Stream wasnt running. Restarting...", level=xbmc.LOGNOTICE)
