from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math


def main():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)   
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    

    def muteVol():
        volume.SetMute(1, None);
        print("Volume is muted")
    #muteVol()

    def unmuteVol():
        volume.SetMute(0, None);
        print("Volume is unmuted")
    #unmuteVol()

    def increaseVol():
       currentDb = volume.GetMasterVolumeLevel()
       currentWin = 24.3738*math.pow((-(90.3712/(currentDb-25.0589))-1), 1.477575428748062)
       needWin = currentWin + 10
       needDb = 25.05889+(-65.31229-25.05889)/(1+math.pow((needWin/24.37377),(0.6767844)))
       volume.SetMasterVolumeLevel(needDb, None)
       print(f"Current volume is {needWin}")
    #increaseVol()


    def decreaseVol():
       currentDb = volume.GetMasterVolumeLevel()
       currentWin = 24.3738*math.pow((-(90.3712/(currentDb-25.0589))-1), 1.477575428748062)
       needWin = currentWin - 10
       needDb = 25.05889+(-65.31229-25.05889)/(1+math.pow((needWin/24.37377),(0.6767844)))
       volume.SetMasterVolumeLevel(needDb, None)
       print(f"Current volume is {needWin}")
    #decreaseVol()


    #x = 10
    #y=25.05889+(-65.31229-25.05889)/(1+math.pow((x/24.37377),(0.6767844)))
    #print(f"Windows {x} - Master {y}")

    #x = 0
    #y = 24.3738*math.pow((-(90.3712/(x-25.0589))-1), 1.477575428748062)
    #print(f"Master {x} - Windows {y}")

    #print("volume.GetMasterVolumeLevel(): %s" % volume.GetMasterVolumeLevel())
    #print("volume.GetVolumeRange(): (%s, %s, %s)" % volume.GetVolumeRange())
    #print("volume.SetMasterVolumeLevel()")
    
    #need = 20
    #y=25.05889+(-65.31229-25.05889)/(1+math.pow((need/24.37377),(0.6767844)))
    #volume.SetMasterVolumeLevel(y, None)
    #print("volume.GetMasterVolumeLevel(): %s" % volume.GetMasterVolumeLevel())


if __name__ == "__main__":
    main()
















#from __future__ import print_function

#from ctypes import POINTER, cast

#from comtypes import CLSCTX_ALL

#from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


#class AudioController(object):
#    def __init__(self, process_name):
#        self.process_name = process_name
#        self.volume = self.process_volume()

#    def mute(self):
#        sessions = AudioUtilities.GetAllSessions()
#        for session in sessions:
#            interface = session.SimpleAudioVolume
#            if session.Process and session.Process.name() == self.process_name:
#                interface.SetMute(1, None)
#                print(self.process_name, 'has been muted.')  # debug

#    def unmute(self):
#        sessions = AudioUtilities.GetAllSessions()
#        for session in sessions:
#            interface = session.SimpleAudioVolume
#            if session.Process and session.Process.name() == self.process_name:
#                interface.SetMute(0, None)
#                print(self.process_name, 'has been unmuted.')  # debug

#    def process_volume(self):
#        sessions = AudioUtilities.GetAllSessions()
#        for session in sessions:
#            interface = session.SimpleAudioVolume
#            if session.Process and session.Process.name() == self.process_name:
#                print('Volume:', interface.GetMasterVolume())  # debug
#                return interface.GetMasterVolume()

#    def set_volume(self, decibels):
#        sessions = AudioUtilities.GetAllSessions()
#        for session in sessions:
#            interface = session.SimpleAudioVolume
#            if session.Process and session.Process.name() == self.process_name:
#                # only set volume in the range 0.0 to 1.0
#                self.volume = min(1.0, max(0.0, decibels))
#                interface.SetMasterVolume(self.volume, None)
#                print('Volume set to', self.volume)  # debug

#    def decrease_volume(self, decibels):
#        sessions = AudioUtilities.GetAllSessions()
#        for session in sessions:
#            interface = session.SimpleAudioVolume
#            if session.Process and session.Process.name() == self.process_name:
#                # 0.0 is the min value, reduce by decibels
#                self.volume = max(0.0, self.volume-decibels)
#                interface.SetMasterVolume(self.volume, None)
#                print('Volume reduced to', self.volume)  # debug

#    def increase_volume(self, decibels):
#        sessions = AudioUtilities.GetAllSessions()
#        for session in sessions:
#            interface = session.SimpleAudioVolume
#            if session.Process and session.Process.name() == self.process_name:
#                # 1.0 is the max value, raise by decibels
#                self.volume = min(1.0, self.volume+decibels)
#                interface.SetMasterVolume(self.volume, None)
#                print('Volume raised to', self.volume)  # debug


#def main():
#    audio_controller = AudioController('System')
#    #audio_controller.set_volume(1.0)
#    audio_controller.mute()
#    #audio_controller.decrease_volume(0.25)
#    #audio_controller.increase_volume(0.05)
#    #audio_controller.unmute()


#if __name__ == "__main__":
#    main()