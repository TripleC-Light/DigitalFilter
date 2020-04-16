
##-- Exponential Filter --##

class ExponentialFilter:
    
    def __init__(self, alpha=0.2):
        self.oldData = 0
        self.alpha = alpha

    def start(self, newData):
        result = self.alpha*newData + (1-self.alpha) * self.oldData
        self.oldData = result
        return result


if __name__ == '__main__':

    ExponentialFilter = ExponentialFilter(0.2)

    x = [0, 0, 0, 0, 10, 20, 30, 35, 20, 10, 5, 0, 0, 0, 0]
    for i in x:
        print(ExponentialFilter.start(i))
