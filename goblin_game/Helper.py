import random

class Helper (object):
    def __init__ (self):
        self.name = "Sidekick"
        self.health = 5
        self.damage = random.randint(1,4)
    def defend (self,theHero):
        defend_or_deflect = random.randint(1,2)
        if theHero.take_damage(self, theHero, monster.power):
            if defend_or_deflect == 1:
                monster.health-=self.damage()
            else:
                theHero.health = 10
                self.health-=monster.damage()
        print "I shalt defend thee, %s!" %theHero.name
