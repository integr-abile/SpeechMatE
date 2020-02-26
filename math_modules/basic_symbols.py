from math_modules.base_module import MathTopic
from jsgf import PublicRule, Literal, Grammar, AlternativeSet
from model.enums import NODE_TYPE

class Per(MathTopic):
    def __init__(self):
        super().__init__()
        #init a vuote variabili che andranno a comporre lo string.format
        self._symbol = ""
        self._format = "{}".format(self._symbol)
        self._g = self.createGrammar()
        self._buffer = [] #tiene conto delle parole dette fino a che una regola non è stata metchata completamente

    @staticmethod #mi permette di non mettere il self tra parentesi perchè non è un metodo di istanza
    def createGrammar():
        short_rule = Literal("per") #expansion
        short_rule.tag = "\cdot" #il contributo di questa regola per il latex finale
        long_rule = Literal("moltiplicato per") #expansion
        long_rule.tag = "\cdot"
        multiplication_rule = PublicRule("multiplication",AlternativeSet(short_rule,long_rule)) #rule
        setattr(multiplication_rule,'type',NODE_TYPE.FOGLIA.name) #aggiungiamo un attributo type direttamente sull'oggetto PublicRule per connotarlo come nodo o attributo
        g = Grammar()
        g.add_rule(multiplication_rule)

        return g
    
    def onInput(self,sender,notification_name,last_token): #Chiamato su nuovo testo in input. Qua arriva token per token
        print("notification info {}".format(last_token))
        self._buffer.append(last_token)
        tags = []
        for i in range(1,len(self._buffer)):
            matched_rules = self._g.find_matching_rules(' '.join(self._buffer[-i:])) #qua creo ad ogni iterazione stringhe sempre più lunghe
            for matched_rule in matched_rules:
                matched_rule.disable() #disabilitandola è come se la marcassi come visitata
                tags.append([tag for tag in matched_rule.matched_tags if len(matched_rule.matched_tags)>0])
        #controllo che i tag trovati siano tutti uguali
        if(checkAllArrayElementsEquals(tags) and len(tags)>0):
            self.sendLatexText(tags[0])

        # matched_rules = self._g.find_matching_rules(last_token)
        # for matched_rule in matched_rules:
        #     print('Public rule tags: {}'.format(matched_rule.type))
        #     matched_rule.disable() #disabilitandola è come se la marcassi come visitata
        #     print("expansions matched tags: {}".format(matched_rule.matched_tags))


def checkAllArrayElementsEquals(lst):
    return lst[1:] == lst[:-1]
