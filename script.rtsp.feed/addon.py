import xbmcaddon
import xbmcgui
import xbmc

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

warning = "Camera stream isn't working :c"
test1 = "Stream is already playing c:"

def StartStream():
    xbmc.executebuiltin("PlayMedia(Path to .strm)")

def needHelp():
    xbmcgui.Dialog().ok(addonname, warning)

if xbmc.Player().isPlaying() == True:
    xbmcgui.Dialog().ok(addonname, test1)
else:
    StartStream()
