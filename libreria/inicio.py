import numpy as np
import subprocess
import matplotlib.pyplot as plt

deciVolt  = 0.1
centiVolt = 0.01
milliVolt = 0.001
microVolt = 0.000001
nanoVolt  = 0.000000001
picoVolt  = 0.000000000001
femtoVolt = 0.000000000000001
attoVolt  = 0.000000000000000001
zeptoVolt = 0.000000000000000000001
yoctoVolt = 0.000000000000000000000001

def two_dimension_sor(schematic, boundary_location, error_treshold):
    # Get the dimensions of the input matrix to loop through. 
    height, width = schematic.shape
    alpha = 2/(1+(np.pi/width))
    #print( " Esta es alpha    ",alpha)
    #alpha = 0.05

    # As the input_matrix is updated, the result is stored in the input_matrix (Gauss Seidel solution).
    # A new array is made for the output_matrix as it does not equal the Gauss Seidel matrix
    input_matrix        = schematic.copy()
    gauss_seidel        = schematic.copy()


    # The number of iterations to reach acceptable delta_v is tracked.
    iterations = 0
    sor_adjustment = 0.0
    delta_v = 0.0
    while(True):
    
        # Loop left to right from top to bottom
        for row in range(1, width - 1):
            for col in range(1, height - 1):
                if (row, col) in boundary_location:
                    pass
                else:
                    gauss_seidel[row][col] = (input_matrix[row-1][col] + input_matrix[row+1][col] + input_matrix[row][col-1] + input_matrix[row][col+1])/4
                    sor_adjustment = alpha * (gauss_seidel[row][col] - input_matrix[row][col])
                    input_matrix[row][col] = sor_adjustment + input_matrix[row][col]
                    delta_v += abs(input_matrix[row][col] - gauss_seidel[row][col])

        iterations += 1
        if delta_v < error_treshold:
            break
        else:
            delta_v = 0  # Restart counting delta_v for the next iteration 
            #print(input_matrix, iterations)
    #print( input_matrix)
    #return input_matrix, iterations, delta_v
    return input_matrix

def ini_potencial(ancho,alto,voltaje ):

    width, height = ancho,alto
    minima, maxima = 0.0, voltaje 
    metal_box = np.zeros((width, height), dtype=float)

    boundary_location = []
    for i in range(width):                      
        #################   DEFINE LA MALLA DE PUNTOS  ###############################
        metal_box[i][0] = minima 
        metal_box[i][width-1] = maxima
        metal_box[0][i] = minima + ((maxima - minima) / (width-1) * i)
        metal_box[width-1][i] = minima + ((maxima - minima) / (width-1) * i)
        
        #############################################################################
        
        ###############  LIMITES  CONDICIONES  FRONTERAS ############################
        boundary_location.append((i,0))
        boundary_location.append((i,width-1))
        
        boundary_location.append((0,i))
        boundary_location.append((width-1,i))
    ##############################################################################
    output_matrix = two_dimension_sor(metal_box, boundary_location,milliVolt) 
    return  output_matrix



def ini_temperatura_gas(bloque,tempera,resolucion ):
    for j in range(0,resolucion+1):
          for i in range(0,resolucion+1): 
                       bloque[j][i]= tempera + 0.2*(5*i)+j*j +273
  
    
def ini_temperatura_electron(bloque,tempe,resolucion):
     for j in range(0,resolucion+1):
          for i in range(0,resolucion+1): 
                       bloque[j][i]= tempe +273 
   
    
def ini_densidad_gas(bloque,resolucion):
     for j in range(0,resolucion+1):
               for i in range(0,resolucion+1): 
                            bloque[j][i]= 0.0015 
   
   
def ini_densidad_electron(bloque,resolucion ):
     for j in range(0,resolucion+1):
               for i in range(0,resolucion+1): 
                            bloque[j][i]= 0.0000000008
    
    

def ini_velocidad_u(bloque,resolucion ):
          for j in range(0,resolucion+1):
                for i in range(0,resolucion): 
                             bloque[j][i]=  200+ 0.6*(8*i+5*j) 
def ini_velocidad_v(bloque,resolucion ):
          for j in range(0,resolucion+1):
	            for i in range(0,resolucion+1): 
                             bloque[j][i]=  5 + 0.6*(8*i+5*j)

def ini_velocidad_u_e(bloque,resolucion ):
          for j in range(0,resolucion+1):
                for i in range(0,resolucion): 
                             bloque[j][i]=  3000+ 0.6*(8*i+5*j) 
def ini_velocidad_v_e(bloque,resolucion ):
          for j in range(0,resolucion+1):
	            for i in range(0,resolucion+1): 
                             bloque[j][i]=  1000 + 0.6*(8*i+5*j)




def ini_campo_magnetico(bloque,I,Radio_c,resolucion):
         u_o = 4*(3.1416)*10**(-7)  
         pi = 3.14159265359
         valor = (u_o*I)/2*pi*Radio_c
         for j in range(0,resolucion+1):
	                for i in range(0,resolucion+1): 
                               bloque[j][i]= valor 

def ini_campo_electrico(bloque,resolucion ):
         for j in range(0,resolucion+1):
	 	        for i in range(0,resolucion+1): 
                                bloque[j][i]= 30 
    
def ini_Energia_gas(bloque,resolucion ):
         for j in range(0,resolucion+1):
	 	        for i in range(0,resolucion+1): 
                                bloque[j][i]= 50

def ini_Energia_electron(bloque,resolucion ):
         for j in range(0,resolucion+1):
	 	        for i in range(0,resolucion+1): 
                                bloque[j][i]= 500 