import random

class Nine_Coins:
    
    def __init__(self, dec): 
        self.dec = dec
    
    def __str__(self):
        # convert decimal to binary and put it into a list
        bin_code = [] 
        # 用0補齊九位數的二進位表示法 
        bin_code = bin_code + \
                   ['0'] * (9-len(bin(self.dec))+2) + [str(j) for j in bin(self.dec)[2:]] 
        # convert to str for print
        bin_code_whole = "".join(bin_code[:]) 
        return f"binary: " + "".join(bin_code_whole[:]) + f" and decimal: {self.dec}"
    
    def __repr__(self):
        # same as above
        bin_code = [] 
        bin_code = bin_code + \
                   ['0'] * (9-len(bin(self.dec))+2) + [str(j) for j in bin(self.dec)[2:]] 
        # convert 0 to "H" and 1 to "T" into a list
        coin = [] 
        for i in bin_code:
            if int(i) == 0:
                coin += "H"
            else:
                coin += "T"
        # convert to str for print        
        coinlist = "".join(coin[:]) 
        return f"Nine_Coins: " + coinlist
    
        
    def toss(self):
        # 2**9 = 512, total 512 state of nine coins
        # give a random state 
        self.dec = random.randint(0,511) 
         
