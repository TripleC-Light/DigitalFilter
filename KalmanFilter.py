
##-- Kalman Filter --##

class KalmanFilter:
    def __init__(self, Q=0.005, R=1):
        self.Q = Q      # 狀態預估模型的共變異數
        self.R = R      # 測量值的共變異數矩陣
        self.Vkt = 0    # 推算值誤差
        self.St = 0
        self.Vpt = 0    # 預估值誤差
        self.Yt = 0     # 推算值
        self.Kt = 0     # Kalman Gain
        
    def start(self, Xt, Yt_1 ):
        # Xt 實際測量值
        # Yt_1 前一次推算值
        self.St = Yt_1
        self.Vpt = self.Vkt + self.Q
        self.Kt = self.Vpt / (self.Vpt+self.R)
        self.Yt = self.St + (self.Kt * ( Xt - self.St ))
        self.Vkt = ( 1 - self.Kt ) * self.Vpt
        return self.Yt


if __name__ == '__main__':

    KalmanFilter = KalmanFilter()

    x = [0, 0, 0, 0, 10, 20, 30, 35, 20, 10, 5, 0, 0, 0, 0]
    x_1 = 0
    for i in x:
        print(KalmanFilter.start(i, x_1))
        x_1 = i
