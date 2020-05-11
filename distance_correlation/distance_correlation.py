from libraries import *
class Distance_correlation():
    def __init__(self):
        # Vectores aleatorios
        # Cuando se instancie el objeto, se deben cargar estos vectores usando la clase anterior
        self.x = np.array;
        self.y = np.array;
        # Matrices de distancias
        self.matrix_distances_x = np.array;
        self.matrix_distances_y = np.array;
        # Promedios a calcular de estas matrices
        self.row_average_x = np.array;
        self.column_average_x = np.array;
        self.total_average_x = 0.;
        self.row_average_y = np.array;
        self.column_average_y = np.array;
        self.total_avergae_y = 0.;
        # Matrices usadas para calcular la distancia de covariancia
        self.A = np.array;
        self.B = np.array;
        # Valores necesarios para calcular la distancia de correlacion
        self.distance_covariance_x_y = 0.;
        self.distance_covariance_x_x = 0.;
        self.distance_covariance_y_y = 0.;
        self.distance_correlation = 0.;
    # Se llena la matriz de distancias
    def fillDistanceMatrix(self,n):
        self.matrix_distances_x = np.zeros((n,n));
        self.matrix_distances_y = np.zeros((n,n));
        for i in range(n):
            for j in range(n):
                if j>i:
                    self.matrix_distances_x[i][j] = np.linalg.norm(self.x[i]-self.x[j]);
                    self.matrix_distances_x[j][i] = np.linalg.norm(self.x[i]-self.x[j]);
                    self.matrix_distances_y[i][j] = np.linalg.norm(self.y[i]-self.y[j]);
                    self.matrix_distances_y[j][i] = np.linalg.norm(self.y[i]-self.y[j]);
    # Se calculan los promedios de las matrices anteriores
    def generateAditionalValues(self,n):
        self.row_average_x = np.zeros((n));
        self.column_average_x = np.zeros((n,1));
        self.row_average_y = np.zeros((n));
        self.column_average_y = np.zeros((n,1));
        for i in range(n):
            self.row_average_x[i] = np.mean(self.matrix_distances_x[i]);
            self.column_average_x[i] = np.mean(self.matrix_distances_x.T[i]);
            self.row_average_y[i] = np.mean(self.matrix_distances_y[i]);
            self.column_average_y[i] = np.mean(self.matrix_distances_y.T[i]);
        self.total_average_x = np.mean(self.matrix_distances_x);
        self.total_average_y = np.mean(self.matrix_distances_y);
    # Se rellena la matriz a usar para calcular la distancia de covarianza
    def fillCenteredMatrix(self,n):
        self.A = np.zeros((n,n));
        self.B = np.zeros((n,n));
        for i in range(n):
            for j in range(n):
                self.A[i][j] = self.matrix_distances_x[i][j]-self.row_average_x[i]-self.column_average_x[j][0]+self.total_average_x;
                self.B[i][j] = self.matrix_distances_y[i][j]-self.row_average_y[i]-self.column_average_y[j][0]+self.total_average_y;
    # Se calculan las distancia de covarianza 
    def calculateDistanceCovariance(self,n):
        for i in range(n):
            for j in range(n):
                self.distance_covariance_x_y +=  (self.A[i][j])*(self.B[i][j]);
                self.distance_covariance_x_x +=  self.A[i][j]**2;
                self.distance_covariance_y_y +=  self.B[i][j]**2;
        self.distance_covariance_x_y = self.distance_covariance_x_y*(1/n**2);
        self.distance_covariance_x_x = self.distance_covariance_x_x*(1/n**2);
        self.distance_covariance_y_y = self.distance_covariance_y_y*(1/(n**2));
    # Se calcula la distancia de correlacion
    def calculateDistanceCorrelation(self,n):
        self.fillDistanceMatrix(n);
        self.generateAditionalValues(n);
        self.fillCenteredMatrix(n);
        self.calculateDistanceCovariance(n);     
        if self.distance_covariance_x_x*self.distance_covariance_y_y != 0:
            self.distance_correlation = math.sqrt((self.distance_covariance_x_y)/(math.sqrt(self.distance_covariance_x_x*self.distance_covariance_y_y)));
        else:
            self.distance_correlation = 0;
        print("The distance correlation is: "+str(self.distance_correlation));
