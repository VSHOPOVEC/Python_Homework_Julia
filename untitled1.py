import matplotlib.pyplot as plt
import numpy as np 
from multiprocessing import Pool
size = 100
center_point = 0 + 0j
number_of_iteration = 100
splitting = 2/size


def f(z):
    return z**2 - 0.4 + 0.6j;

Complex_matrix = np.array([[ i*splitting + j*1j*splitting for j in range(-1*size,size + 1)] for i in range(-1*size,size + 1)])*(-1j)
temp_Complex_matrix = Complex_matrix.flatten()

def test(point_1,center_point):
   if(abs(point_1 - center_point) > 2):
       return False;
   else:
       return True;
   
def Julia(func, number_of_iteration, number_at_the_moment, z):
    if((number_at_the_moment < number_of_iteration) and test(z,center_point) == True):
        return Julia(func,number_of_iteration,number_at_the_moment + 1,func(z));
    else:
        return number_at_the_moment;

def Julia_task(z):
    return Julia(f, number_of_iteration, 0, z)





if __name__ == "__main__":
    with Pool() as pool:
        result = pool.map(Julia_task, temp_Complex_matrix)
    result = np.array(result).reshape(2*size + 1, 2*size + 1)

    # Визуализация
    plt.figure(figsize=(60, 60))
    plt.imshow(result,cmap = "inferno")
    cbr = plt.colorbar()
    
    plt.savefig("high_quality_image_multiproccesing3.png", dpi=500)
    plt.savefig("high_quality_image_multiproccesing3.pdf", dpi=500)
    plt.savefig("high_quality_image_multiproccesing3.jpeg", dpi=500)


