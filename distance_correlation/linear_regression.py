from libraries import *
class Linear_regression():
    def __init__(self):
        self.x = np.array;
        self.y = np.array;
        self.linear_regression_x = np.array;
        self.linear_regression_y = np.array;
        self.covariance_x_y = 0;
        self.variance_x = 0;
        self.variance_y = 0;
        self.correlation_coefficient = 0;
        self.slope = 0;
        self.intersection = 0;
    def calculateCovariance(self,n):
        for i in range(n):
            self.covariance_x_y += (self.x[i]-np.mean(self.x))*(self.y[i]-np.mean(self.y));
        self.covariance_x_y = self.covariance_x_y*(1/n);
    def calculateVariance(self,n):
        for i in range(n):
            self.variance_x += (self.x[i]-np.mean(self.x))**2;
            self.variance_y += (self.y[i]-np.mean(self.y))**2;
        self.variance_x = math.sqrt(self.variance_x*(1/n));
        self.variance_y = math.sqrt(self.variance_y*(1/n));
    def calculateCorrelationCoefficient(self,n):
        self.calculateCovariance(n);
        self.calculateVariance(n);
        self.correlation_coefficient = self.covariance_x_y/((self.variance_x)*(self.variance_y));
    def calculateLinearRegression(self,n):
        self.calculateCovariance(n);
        self.calculateVariance(n);
        self.linear_regression_x = self.x;
        self.slope = self.covariance_x_y/(self.variance_x**2);
        self.intersection = np.mean(self.y)-self.slope*np.mean(self.x);
        self.linear_regression_y = self.intersection + self.slope*self.linear_regression_x;
    def graphLinearRegression(self,n):
        self.calculateLinearRegression(n);
        plt.plot(self.linear_regression_x,self.linear_regression_y,"k");
