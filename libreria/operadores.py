
import numpy as np
import matplotlib.pyplot as plt







def revisare( variable):

           for i in range(len(variable)):
	             for j in range(len(variable[i])):
                          if (np.isinf(variable[i][j])):
                                                   x = i
                                                   y = j
                                                   while ( np.isinf(variable[x][y])  ):
                                                           y = y+1              
                                                   variable[i][j]= variable[x][y]  
       
       
def limite_predictor(argumento3 ):
           print("Esta es la impresion del argumento2", argumento3)


def limite_corrector( argumento4  ):
           print("Esta es la impresion del argumento2", argumento4)




def diff_predictor(bloque , eje, cor,resolucion ):
                      resulta = np.array([[0.00  for col in range(resolucion+1)] for row in range(resolucion+1)])
                      if eje=="x" :
                          for i in range(0,resolucion):
                             for j in range(0,resolucion):
                                   tempo1 = cor[i][j]
                                   tempo1_x = tempo1[0]
                                   tempo2 = cor[i][j+1]
                                   tempo2_x = tempo2[0]
                                   if(tempo2_x == tempo1_x):
                                        delta_x = 0.000001
                                   else:
                                      delta_x  = tempo2_x - tempo1_x
                                   
                                   
                                   #print(tempo2_x,"-- ",i," ---",tempo1_x)
                                   #print("delta_x",delta_x)
                                   #print(" bloque[i+1][j] :",bloque[i+1][j])
                                   #print("    bloque",i," ",j,"  :",bloque[i][j+1])
                                   resulta[i][j]= (bloque[i][j+1] - bloque[i][j])/delta_x
                                   #print("predictor x ",resulta[i][j])
                             #print("-----------------------------------  ",j," ---------------------------------")
                               
                      if eje == "y" :
                           for i in range(0,resolucion):
                                for j in range(0,resolucion):
                                      tempo3 = cor[i][j]
                                      tempo3_y = tempo3[1]
                                      tempo4 = cor[i][j+1]
                                      tempo4_y = tempo4[1]
                                      if(tempo4_y == tempo3_y):
                                                   delta_y = 0.00001
                                      else:
                                                   delta_y  =tempo4_y - tempo3_y
                                      #print(tempo4_y,"-- ",i," ---",tempo3_y)
                                      #print("delta_y",delta_y)
                                      resulta[i][j]= (bloque[i][j+1]-bloque[i][j])/delta_y
                                      #print("predictor y ",resulta[i][j])
                      return  resulta


def diff_corrector(bloque1 , eje1, cor1,resolucion ):
                     resulta1 = np.array([[0.00  for col in range(resolucion+1)] for row in range(resolucion+1)])
                     if eje1=="x" :
                          for i in range(0,resolucion):
                             for j in range(0,resolucion):
                                   tempo1 = cor1[i][j]
                                   tempo1_x = tempo1[0]
                                   tempo2 = cor1[i][j-1]
                                   tempo2_x = tempo2[0]
                                   if(tempo2_x == tempo1_x):
                                                 delta_x = 0.000001
                                   else:
                                        delta_x  =tempo1_x - tempo2_x
                                   
                                   resulta1[i][j]= (bloque1[i][j]- bloque1[i][j-1])/delta_x
                                   
                     if eje1=="y" :
                           for j in range(0,resolucion):
                              for i in range(0,resolucion):
                                   tempo3 = cor1[j][i]
                                   tempo3_y = tempo3[1]
                                   tempo4 = cor1[j][i-1]
                                   tempo4_y = tempo4[1]
                                   if(tempo3_y == tempo4_y):
                                                    delta_y = 0.000001
                                   else:
                                        delta_y = tempo3_y - tempo4_y
                                   
                                   resulta1[j][i]= (bloque1[j][i]-bloque1[j-1][i])/delta_y
                                   #print("corrector y ",resulta1[i][j])
                     return  resulta1

def delta( eje1, cor1,resolucion ):
                     delta = np.array([[0.00  for col in range(resolucion+1)] for row in range(resolucion+1)])
                     if eje1=="x" :
                          for i in range(0,resolucion+1):
                             for j in range(0,resolucion+1):
                                   tempo1 = cor1[i][j]
                                   tempo1_x = tempo1[0]
                                   tempo2 = cor1[i][j-1]
                                   tempo2_x = tempo2[0]
                                   if(tempo2_x == tempo1_x):
                                                 delta_x = 0.01
                                   else:
                                        delta_x  =tempo1_x - tempo2_x
                                                                  
                                   if delta_x == 0 :
                                           delta_x = 0.1
                                   if abs(delta_x) > 20:
                                           delta_x = 20
                                   
                                   delta[i][j] = delta_x
                                   
                                   
                     if eje1=="y" :
                           for j in range(0,resolucion+1):
                              for i in range(0,resolucion+1):
                                   tempo3 = cor1[i][j]
                                   tempo3_y = tempo3[1]
                                   tempo4 = cor1[i-1][j]
                                   tempo4_y = tempo4[1]
                                   if(tempo3_y == tempo4_y):
                                                    delta_y = 0.01
                                   else:
                                        delta_y  =tempo3_y - tempo4_y
                                                                      
                                   if delta_y == 0 :
                                          delta_y = 0.1 
                                   
                                   delta[i][j] = delta_y
                                   
                     return  delta


