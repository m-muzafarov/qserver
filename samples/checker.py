#!/usr/bin/env python2
#-*- coding=utf-8 -*-
from __future__ import with_statement
import subprocess, os, cPickle
from quest import QuestDescriptor

__all__ = ["VPNQuestProvider"]

class VPNQuestProvider:
    
    names = [ 'zero', 
        "team1",
        "team2",
        "team3",
    ]




    def __init__(self):
        self.nextId = 1

    def GetId(self):
        return "vuln:100"

    def GetName(self):
        return "Old stories"

    def GetSeries(self):
        return "vuln"

    def OnUserAction(self, qd, actionString):
        if "FLAGFLAGFLAG" == actionString:
            return (True,"Congrats! You've solved the task")
        else:
            return (False, "Sorry, you need to try harder")

    def SaveState(self, dir):
        with open(os.path.join(dir, "vpnquest"), "w") as writer:
            cPickle.dump(self.__dict__, writer)

    def LoadState(self, dir):
        with open(os.path.join(dir, "vpnquest"), "r") as reader:
            self.__dict__ = cPickle.load(reader)
            
    def CreateQuest(self,team_id):
        id = team_id+1
        text = {"ru": "Get the key from: google.ru", 
                "en": "Найдите ключ на: google.ru" }
        html = {"ru": """\
<p>
Найдите ключ на: google.ru
</p>
""", 
                "en": """\
<p>
Get the key from: google.ru
</p>
"""}
        file = "static/km/%s_team%s.zip" % (self.names[id],id)
        qd = QuestDescriptor(id,text,html,file)
        return qd
