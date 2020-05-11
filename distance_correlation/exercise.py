from libraries import *
np.random.seed(121)
class toy_model():
    def __init__(self):
        # Se crea un vector de variables aleatorias
        self.random_vector_x = np.array;
        self.random_vector_y = np.array;
    # Se llena el vector anterior con numeros aleatorios entre 0 y 1, n indica el tamaño del vector
    def load(self,n):
        self.random_vector_x = np.array(sorted(np.random.uniform(-1,1,n)));
    # Se llena el vector anterior a travez de un archivo de excel, filename indica el nombre del archivo excel
    def loadCSV(self,filename):
        print("cargar archivo desde excel no implementado");
    # Se realiza el ejercicio propuesto y = x**alpha + ruido * numero aleatorio
    def potenciaN(self,n,alpha,noise):
        self.load(n);
        self.random_vector_y = (np.power(self.random_vector_x,alpha) + (noise*np.random.uniform(-1,1,n)));
    def polinomioUno(self,n,noise):
        self.load(n);
        self.random_vector_y =  (self.random_vector_x*(self.random_vector_x-1)*(self.random_vector_x+1)*(self.random_vector_x-0.5)*(self.random_vector_x+0.5)) + (noise*np.random.uniform(-1,1,n));
    def sen(self,n,noise):
        self.random_vector_x = np.array(sorted(np.random.uniform(-np.pi,np.pi,n)))
        self.random_vector_y = (np.sin(self.random_vector_x)+noise*np.random.uniform(-1,1,n))
    # Se grafica el polinomio y además la muestra que se obtiene
    def plot(self):
        plt.figure(0);
        plt.plot(self.random_vector_x,self.random_vector_y,"o");