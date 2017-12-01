# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 08:57:23 2017

@author: hao
"""

import secsgem
import code

# In[]
class SampleEquipment(secsgem.GemEquipmentHandler):

      
    def __init__(self, address, port, active, session_id, name, custom_connection_handler=None):
        secsgem.GemEquipmentHandler.__init__(self, 
                                             address, port, active, session_id, name, custom_connection_handler)
        self.MDLN = 'GEMEQ'
        self.SOFTREV = '1.0.0'
        
        #--------------------------------------------------------------------------------------------
        # Adding status variables
        self.status_variables.update({
                10: secsgem.StatusVariable(10,'sample1, numeric SVID, SecsVarU4', 'meters', secsgem.SecsVarU4, False), 
                'SV2': secsgem.StatusVariable('SV2', 'sample2, text SVID, SecsVarString','chars', secsgem.SecsVarString, False),
                })
        self.status_variables[10].value = 123
        self.status_variables['SV2'].value = "sample sv"
        
        #--------------------------------------------------------------------------------------------
        # Adding equipment constants
        self.ec1 = 321
        self.ec2 = "sample ec"
        self.equipment_constants.update({
                20: secsgem.EquipmentConstant(20, "sample1, numeric ECID, SecsVarU4", 0,500, 50, "degrees", secsgem.SecsVarU4, True),
                "EC2": secsgem.EquipmentConstant("EC2", "sample2, text ECID, SecsVarString", "", "", "", "chars", secsgem.SecsVarString, True),
                })
    
        def on_ec_value_request(self, ecid, ec):
            if ec.ecid == 20:
                return ec.value_type(value=self.ec1)
            elif ec.ecid == "EC2":
                return ec.value_type(value=self.ec2)
            return []

        def on_ec_value_update(self, ecid, ec, value):
            if ec.ecid == 20:
                self.ec1 = value
            elif ec.ecid == "EC2":
                self.ec2 = value
        #--------------------------------------------------------------------------------------------
        # add Colllection Events():
        self.dv1 = 31337
        self.data_values.update(
                {30: secsgem.DataValue(30, "sample1, numeric DV, SecsVarU4", secsgem.SecsVarU4, True),
                 })
        self.collection_events.update(
                {50: secsgem.CollectionEvent(50, "test collection event", [30]),
                 })

        def on_dv_value_request(self, dvid, dv):
            if dv.dvid == 30:
                return dv.value_type(value=self.dv1)
            return []

        def trigger_sample_collection_event(self):
            self.trigger_collection_events([50])
                  
        #--------------------------------------------------------------------------------------------
        # add Alarm:
        self.collection_events.update({
                100025: secsgem.CollectionEvent(100025, "test collection event alarm set",[]),
                200025: secsgem.CollectionEvent(200025, "test collection event alarm clear", []),
                })
        self.alarms.update({
                25: secsgem.Alarm(25, "test alarm", "test text", 
                                  secsgem.ALCD.PERSONAL_SAFETY | secsgem.ALCD.EQUIPMENT_SAFETY, 
                                  100025, 200025),
              })
        def set_sample_alarm():
            self.set_alarm(25)
        
        def clear_sample_alarm():
            self.clear_alarm(25)
            
        #---------------------------------------------------------------------------------------------
        # Modify S1F12
        class SecsS01F12_r(secsgem.SecsStreamFunction):
            _stream = 1
            _function = 12
            _dataFormat = [
                    [
                        secsgem.SVID,
                        secsgem.SVNAME,
                    ]
            ]
            _toHost = True
            _toEquipment = False
            _hasReply = False
            _isReplyRequired = False
            _isMultiBlock = False

        self.secsStreamsFunctions[1].update({
                12: SecsS01F12_r,
            })
        
# In[]
if __name__ == '__main__':    
    h = SampleEquipment("127.0.0.1", 5000, False, 0, "sampleequipment")
    h.enable()
    code.interact("equipment object is available as variable 'h', press ctrl-d to stop", local=locals())
    # In[]
    msg = secsgem.SecsS01F01()
    print(msg)
    
    # In[]
    h.send_and_waitfor_response(msg)
    
    # In[]
    h.disable()
