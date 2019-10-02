
##-- Moving Average Filter --##

class MovingAverageFilter:
    
    def __init__(self, AVG_level=8):
        
        self.AVG_level = AVG_level
        self.SampleInd = 0
        self.SampleRec = []
        self.Xt_n = 0
        for i in range(0, self.AVG_level):
            self.SampleRec.append(0)

    def start(self, Xt):
        
        if( self.SampleInd < (self.AVG_level-1) ):
          self.SampleInd += 1
        else:
          self.SampleInd = 0
        
        self.SampleRec[self.SampleInd] = Xt
        self.SampleAVG = 0
        for i in range(0,self.AVG_level):
          self.SampleAVG += self.SampleRec[i]
        
        return (self.SampleAVG/self.AVG_level)


    def startX(self, Xt, Yt_1):
        
        if( self.SampleInd < (self.AVG_level-1) ):
          self.SampleInd += 1
        else:
          self.SampleInd = 0


        if((self.SampleInd+1)>=self.AVG_level):
            self.Xt_n = self.SampleRec[0]
        else:
            self.Xt_n = self.SampleRec[self.SampleInd+1]
            
        self.SampleRec[self.SampleInd] = Xt
        
        return (Yt_1 + ((Xt-self.Xt_n)/self.AVG_level))


if __name__ == '__main__':

    MovingAverageFilter = MovingAverageFilter(4)

    x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

    for i in x:
        print(MovingAverageFilter.start(i))
    
