from tokenize import String


class Card(object):
    def __init__(self, number, suit):
        self._suit = suit
        self._value = number

    def __eq__(self, other): 
        if not isinstance(other, Card):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.suit() == other.suit() and self.value() == other.value()

    def __str__(self):
     return str(self.value()) + " of " +  self.suit()

    def __repr__(self):
        val = self.value()
        match val:
            case 11:
                val = 'J'
            case 12:
                val = 'Q'
            case 13:
                val = 'K'
            case 14:
                val = 'A'
        return str(val) + " of " +  self.suit()

    def suit(self):
        return self._suit
    
    def value(self):
        return self._value