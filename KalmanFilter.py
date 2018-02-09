
##-- Kalman Filter --##
class KalmanFilter:
    def __init__(self, Q=0.01, R=1):
        self.Q = Q
        self.R = R
        self.Vkt = 0
        self.St = 0
        self.Vpt = 0
        self.Yt = 0
        self.Kt = 0
        
    def start(self, Xt, Yt_1 ):
      self.St = Yt_1
      self.Vpt = self.Vkt + self.Q
      self.Kt = self.Vpt/(self.Vpt+self.R)
      self.Yt = self.St + (self.Kt * ( Xt - self.St ))
      self.Vkt = ( 1 - self.Kt ) * self.Vpt
      return self.Yt
