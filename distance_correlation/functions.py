from libraries import *
class Aproximation():
    def __init__(self,size,paso,salto,sample,separation,toy):
        self.size = size;
        self.paso = paso;
        self.salto = salto;
        self.number_of_roots = 0;
        self.sample = sample;
        self.object_distance = separation;
        self.object_toy = toy;
        self.list_iterations = [];
        self.list_index = [];
        self.list_roots = [];
        self.initial_minimun_distance = [];
        self.initial_index = [];
        self.new_x = [];
        self.critical_points = [];
        self.norm = [];
        self.best_aproximation = 0;
        self.aproximations = [];
    def scanner(self):
        i = 0;
        while i<(self.size-self.paso):
            print("iteracion "+str(i)+":");
            self.object_distance.x = self.object_toy.random_vector_x[0+i:self.paso+i];
            self.object_distance.y = self.object_toy.random_vector_y[0+i:self.paso+i];
            self.object_distance.calculateDistanceCorrelation(self.paso);
            self.list_iterations.append(self.object_distance.distance_correlation);
            plt.figure(2)
            plt.plot(self.object_distance.x,self.object_distance.y,"o")
            i+=self.salto;  
    def choose_roots(self):
        j = 0;
        self.initial_minimun_distance = [];
        self.initial_index = [];
        self.list_index = [];
        self.list_roots = [];
        while j < len(self.list_iterations):
            self.initial_minimun_distance.append(min(self.list_iterations[0+j:j+int(self.paso/self.salto)]));
            self.initial_index.append(self.salto*self.list_iterations.index(min(self.list_iterations[0+j:j+int(self.paso/self.salto)])));
            j += int(self.paso/self.salto);
        for i in range(self.number_of_roots):
            self.list_index.append(self.initial_index.pop(self.initial_minimun_distance.index(min(self.initial_minimun_distance))));
            self.list_roots.append(self.initial_minimun_distance.pop(self.initial_minimun_distance.index(min(self.initial_minimun_distance))));
        self.new_x = [];
        self.critical_points = [];
        for i in range(len(self.list_index)):
            self.new_x.append(self.list_index[i]/self.salto)
        plt.figure(3);
        plt.plot(self.list_iterations,"ob");   
        plt.plot(self.new_x,self.list_roots,"or");
        for i in range(len(self.list_index)):
            self.critical_points.append(self.sample.x[self.list_index[i]:self.paso+(self.list_index[i])][int(self.paso/2)]);
    def leastSquares(self,initial_values):
        def exp(a,b,c,x):
            return a*np.exp(-b*(x-c)**2)
        x_0 = self.critical_points;
        def residuos(p, y, x):
            sum = 0.0;
            for i in range(len(x_0)):
                sum += exp(p[i],p[-1],self.critical_points[i],x);
            error = y - (sum);
            return error
        p0 = initial_values;
        ajuste = leastsq(residuos, p0, args=(self.sample.y, self.sample.x));
        def funcion(x, p):
            sum = 0.0;
            for i in range(len(x_0)):
                sum += exp(p[i],p[-1],self.critical_points[i],x);
            return sum
        x1 = self.sample.x;
        y1 = funcion(self.sample.x, ajuste[0]);
        self.norm.append(np.linalg.norm(self.sample.y-y1));
        self.aproximations.append(y1);
    def chooseBestAproximation(self,initial_values,roots):
        self.best_aproximation = 0;
        p_0 = initial_values;
        self.norm = [];
        for i in range(1,roots):
            self.number_of_roots = i;
            self.choose_roots();
            ajuste = self.leastSquares(p_0);
            p_0.append(1);
        self.best_aproximation = self.norm.index(min(self.norm));
        x = self.sample.x
        y = self.aproximations[self.best_aproximation]
        plt.figure(4);
        plt.plot(self.sample.x,self.sample.y, "ob");
        plt.plot(x, y, 'r');
        print(self.norm[self.best_aproximation]);
#------------------------------------------------------------------------------------------------------
"""Partir el dominio y calcular el valor
separacion = Distance_correlation();
regresion_lineal = Linear_regression();
print("enter in how many parts you want to separate the domain: ");
print("it has to be a sample size divisor");
steps = int(input());
paso = int(size/steps);
distance_correlation_example = np.zeros((steps));
i = 0;
j = 0;
while i<size :
    separacion.x = prueba.random_vector_x[0+i:paso+i];
    separacion.y = prueba.random_vector_y[0+i:paso+i];
    regresion_lineal.x = prueba.random_vector_x[0+i:paso+i];
    regresion_lineal.y = prueba.random_vector_y[0+i:paso+i];
    separacion.calculateDistanceCorrelation(paso);
    distance_correlation_example[j] = separacion.distance_correlation;
    plt.figure(2)
    plt.plot(separacion.x,separacion.y,"o")
    regresion_lineal.graphLinearRegression(paso);
    i+=paso;
    j+=1;
plt.figure(3)
plt.plot(distance_correlation_example,"o");"""
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
"""#agregar valores especiales a un vector
print("insert a value for the upper bound of the distance correlation:")
alpha = float(input());
distance_correlation_points=[];
index=[];
#se escogen valores a partir de un parametro ingresado  para el usuario ( cota para el coeficiente)
for i in range(len(distance_correlation_example)):
    if (distance_correlation_example[i]<alpha):
        index.append(i*salto);    
print("you have to choose from this values: ")
print(index);
#se realiza la aproximacion por polinomios
#HAY PROBLEMAS PARA ESCOGER LOS VALORES QUE SE USARAN PARA EL POLINOMIO YA QUE DA COSAS RARAS
#Asi como esta, no escoge , pero aproxima bien
polinomio_aproximacion_x=[];
polinomio_aproximacion_y=[];
for i in range(len(index)):
    polinomio_aproximacion_x.append(prueba2.x[index[i]:paso+index[i]][int(paso/2)]);
    polinomio_aproximacion_y.append(prueba2.y[index[i]:paso+index[i]][int(paso/2)]);
print("you have " +str(len(polinomio_aproximacion_x))+ " points");
print("enter the degree of the polynomial");
m=int(input());
plt.figure(2)
xp = np.linspace(-1,1,size)
pm = np.polyfit(polinomio_aproximacion_x, polinomio_aproximacion_y,m);
plt.plot(xp,np.polyval(pm,xp),"r-");
plt.plot(polinomio_aproximacion_x,polinomio_aproximacion_y,"bo")
plt.ylim(-0.3,0.3)"""
#---------------------------------------------------------------------------------------------