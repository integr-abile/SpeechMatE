from enum import Enum

class Action(Enum):
    NESSUNA = 0
    DETTATURA = 1
    EDITING = 2

class NODE_TYPE(Enum):
    INTERNO = 0
    FOGLIA = 1 #aiuta a facilitare la fine del layer senza dover dire esplicitamente 'fine'

class LayerMsg(Enum):
    NEW_LAYER_REQUEST = 0 #forward da ModuleMsg
    END_THIS_LAYER = 1 #sull'arrivo della parola "fine"
    END_THIS_LAYER_WITH_TEXT = 2 #quando hanno dato tutti una risposta e sono tutti foglie o quando c'è un end layer, ma ci sono foglie pendenti
    TEXT = 3 #ciò che arriva dai vari moduli è coerente e può essere inoltrato al srv, oppure è un testo da inviare "as is" perchè non triggera fin dal principio nessuna regola
    WAIT = 4 #quando uno o più moduli gli hanno risposto Wait o nessuna regola è stata metchata
    REWIND = 5 #chiede al server di ripartire da un punto più indietro del burst a somministrare al layer il burst corrente
    ANNULLA = 6 #chiede di tornare allo stato precedente

class ModuleMsg(Enum):
    TEXT = 0 #una regola metchata o più regole metchate che però scriverebbero la stessa cosa
    NEW_LAYER_REQUEST = 1 #se una regola richiede un nuovo layer, questa ha la priorità su ogni altro match
    WAIT = 2 #più regole metchate contrastanti
    NO_MATCH = 3 #nessuna regola metchata a questo giro, ma potrei metcharla in un momento successivo
    OUT_OF_PLAY = 4 #nessuna regola può più essere triggerata perchè il token che è arrivato non da spazio a match presenti e/o futuri


class EditMsg(Enum):
    RETRY = 0 #il master deve riprovare ad inviare lo stesso token (eventualmente inviando prima a texstudio qualcosa)
    NEXT_TOKEN = 1 #token non appartenente a niente di accettabile. Skip
    WAIT = 2 #a quel livello ha metchato qualcosa.. bisogna vedere se al livello successivo sarà la stessa cosa
    COMMAND = 3 #se abbiamo tutte foglie, tipicamente una
    
