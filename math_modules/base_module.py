from model.module_answer_pool import ModuleAnswersPool
from model.enums import ModuleMsg
from typing import Callable


class MathTopic:

    def __init__(self,answerPoolSetter):
        self._answerPoolSetter = answerPoolSetter

    def sendLatexText(self,text,node_type_info={'leaf':False}):
        """node_type_info è un dizionario {'leaf':bool} (di default leaf:False) che specifica se la regola triggerata è una foglia oppure no"""
        self._answerPoolSetter((ModuleMsg.TEXT,text,node_type_info))

    def postNewLayerRequest(self,unlock_node_words={'layer_unlock_words':[]}):
        self._answerPoolSetter((ModuleMsg.NEW_LAYER_REQUEST,None,unlock_node_words))
    
    def sendWaitRequest(self):
        self._answerPoolSetter((ModuleMsg.WAIT,None,None))
    
    def sendNoMatchNotification(self):
        self._answerPoolSetter((ModuleMsg.NO_MATCH,None,None))
        

    
