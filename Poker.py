def main ():
  class Card:
    def __init__(self,value,suit):
      self.value= value
      self.suit = suit

      def _repr_(self):
        value_name=""
        suit_name=""
        if self.value == 0:
          value_name = "Knight"
        if self.value == 1:
          value_name = "Ranger"
        if self.value == 2:
          value_name = "Mage"
        return value_name

  class StandardDeck(list):
    def _init_(self):
      super()._init_()
      suits = list(range(4)) # 0 for Fire, 1 for Earth, 2 for Water, 3 for Air
      values = list(range(3)) # 0 for Knight, 1 for Ranger, 2 for MAge
      [[self.append(Card(i,j)) for j in suits] for i in values]

  deck = StandardDeck()
  for card in deck:
    print(card.value, card.suit)


if __name__ == '__main__':
  main()