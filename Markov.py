import random

class MarkovChain(object):
    def __init__(self, inputString): #CONSTRUCTOR FOR THE MARKOV CHAIN OBJECT
           
           self.inputString = inputString 
           self.states = {}    #STORES THE PROBABILITES OF EACH TRANSITION, PRINT THE OBJECT TO SEE PROBABILITIES AND TRANSITIONS
    
    def __str__(self):    #JUST USED FOR WHEN SOMEONE TRIES TO PRINT THE OBJECT
        for f in self.states:
            print f, self.states[f]
            
    def createSequence(self, length, start=""):    #CREATES A VARIABLE LENGTH SEQUENCE BASED UPON A TRAINED MARKOV CHAIN
        if start == "":
            start = random.choice(self.states.keys())[0]
        string = start
        
        for f in range(length):
            start = self.transition(start)
            string += " "+start
            
        return string 
    
    def transition(self, start): #RANDOMLY USES TRAINED MARKOV CHAIN TO TRANSITION FROM A GIVEN STRING TO ANOTHER GIVEN STRING, BOTH MUST BE PRESENT IN THE MARKOV CHAIN
            gen = random.random()
            tot = 0.0
            for f in self.states:
                if f[0] == start:
                    if self.states[f]+tot > gen:
                        return f[1]
                    else:
                        tot += self.states[f]
            return random.choice(self.states.keys())[1]
            
    def train(self): #TRAINS THE MARKOV CHAIN BASED UPON THE INPUTSTRING, THE RESULTING MARKOV CHAIN IS STORED IN THE SELF.STATES PROPERTY
        string = self.inputString
        string = string.split(" ")

        for f in string:
            for g in string:
                self.states[(f,g)] = 0
                
        start = string[0]
        for f in string:  
            self.states[(start,f)] += 1
            start=f
        self.states[(string[0],string[0])] -= 1

        tally = 0
        done = {}
        for f in self.states:
            if f[0] not in done:
                done[f[0]] = self.states[f]
            else:
                done[f[0]] += self.states[f]

        for g in self.states:
            if done[g[0]] != 0:
                self.states[g] = float(self.states[g])/float(done[g[0]])
        

        
if __name__ == "__main__":
    m = MarkovChain("THIS THE WHERE THE TEXT GOES. IT DOESN'T MATTER WHAT TEXT YOU ENTER. THE PROGRAM SHOULD WORK GENERALLY WITH WHATEVER INPUT YOU LIKE.")
    m.train()
    print m.createSequence(5)
    

