# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 09:24:58 2017

@author: hao
"""
import secsgem

# S1F15: OFFline Request
# S1F17: Online Request
# S2F41: Remote Command
# S2F45: Limit
# S2F49: Enhanced Remote Command
# S7F1: Process Program Inquiy
# S7F3: Process Program Send
# S2F17: Timer Request
# S2F31: Timer Set


# In[]

if __name__ == '__main__':
    
    # Request equipment status VID 
    print(secsgem.SecsS01F01())
    print(secsgem.SecsS01F02())
    
    # Request state variable SVID list
    print(secsgem.SecsS01F11())
    print(secsgem.SecsS01F12())
    
    # Request equipment constant ECID
    print(secsgem.SecsS02F13())
    print(secsgem.SecsS02F14())
    
    # Change equipment constant ECID
    print(secsgem.SecsS02F15())
    print(secsgem.SecsS02F16())
    
    # Set trace condition 
#    print(secsgem.SecsS02F23())
#    print(secsgem.SecsS02F24())
    
    # Request equipment constant ECID list
    print(secsgem.SecsS02F29())
    print(secsgem.SecsS02F30())
    
    # Set Report
    print(secsgem.SecsS02F33())
    print(secsgem.SecsS02F34())
    
    # Get Timer
    print(secsgem.SecsS02F17())
    print(secsgem.SecsS02F18())
#    
    #Event
    print(secsgem.SecsS06F11())
    print(secsgem.SecsS06F12())

    #Alarm
    print(secsgem.SecsS05F01())
    print(secsgem.SecsS05F02())
    # In[]
    
    f = secsgem.SecsS02F33()
    print(f)
    
    # In[]
    f.DATAID=10
    f.DATA.append({"RPTID": 5, "VID": ["Hello", "Hallo"]})
    f.DATA.append({"RPTID": 6, "VID": ["1", "2"]})
    print(f)
    # In[]
    f.DATA[1].VID[0]="Goodbye"
    f.DATA[1].VID[1]="Auf Wiedersehen"
    print(f)
    
    # In[]
    print(secsgem.format_hex(f.encode()))
