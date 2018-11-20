import random
class Helper (object):
    def __init__ (self):
        self.name = "Sidekick"
        self.health = 5
        self.damage = random.randint(1,4)
    def defend (self):
        defend_or_deflect = random.randint(1,3)
        if Hero.take_damage():
            if defend_or_deflect == 1:
                monster.health-=self.damage()
            else:
                theHero.health = 10
                self.health-=monster.damage()
        print "I shall defend you!"
