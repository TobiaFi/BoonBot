#---------------------------
#   Import Libraries
#---------------------------
import threading
import time
from collections import Counter
#---------------------------
#   [Required] Script Information
#---------------------------
ScriptName = "BoonBot"
Website = "https://www.twitch.tv/TobiaF"
Description = "!boon will start a 45s poll with 1/2/3 as options"
Creator = "TobiaF"
Version = "1.0.0.0"

#---------------------------
#   [Required] Initialize Data (Only called on load)
#---------------------------
def Init():
    return

poll_is_active = False
votes = dict()
vote_count = dict()

def end_poll():
    global poll_is_active
    poll_is_active = False
    global votes
    global vote_count
    vote_count = Counter(votes.values())
    Parent.SendStreamMessage('The people have spoken. Boon #' + str(vote_count.most_common()[0][0]) + ' was picked with ' + str(vote_count.most_common()[0][1]) + ' vote(s)')
    votes = dict()
    vote_count = dict()
    return

#---------------------------
#   [Required] Execute Data / Process messages
#---------------------------
def Execute(data):
    if data.IsChatMessage() and data.Message.lower() == '!boon' and data.UserName.lower() == 'tobiaf' and not poll_is_active:
        Parent.SendStreamMessage('Which boon do you want me to pick? Vote by typing 1/2/3 in the chat!')
        global poll_is_active
        poll_is_active = True
        t = threading.Timer(45.0, end_poll)
        t.start()
    if data.IsChatMessage() and data.Message in ['1', '2', '3'] and poll_is_active:
        global votes
        if data.UserName not in votes.keys():
            votes[data.UserName] = int(data.Message)
            Parent.SendStreamMessage('@' + data.UserName + ' has picked boon #' + data.Message)
    return

#---------------------------
#   [Required] Tick method (Gets called during every iteration even when there is no incoming data)
#---------------------------
def Tick():
    return
