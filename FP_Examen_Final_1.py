# -*- coding: utf-8 -*-
"""
Created on Thu May 27 00:17:14 2021

@author: Andres Guaita
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

Excel=pd.read_excel('Futbol_Partidos.xlsx')
torneo=Excel['torneo'].drop_duplicates()
seleccion=Excel['local'].drop_duplicates()
goles=Excel['goles_visita']
grafica=['Visitante','Local','Total']
abrev=['FIFAQ', 'FR','CC', 'CPC','KC','CA','FIFA','GC','AFC','CP']
abrev_s=Excel['abrev_local'].drop_duplicates()



indext=''
indexs=''
index_r=''
index_rl=''
sumagl=0
sumagl1=0
suma_xs=0
suma_xsv=0
suma_xsl=0
suma_g_t1=[]
suma_g_t=[]
suma_sl=[]
suma_sl1=[]
goles_sv=[]
goles_sl=[]
goles_rv=[]
goles_rv1=[]


def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	os.system('cls') # NOTA para windows tienes que cambiar clear por cls
	print ("\nSelecciona una opción")
	print ("\t1 - Cantidad de goles como locales."),print ("\t2 - Cantidad de goles como visitante."),print ("\t3 - Cantidad de goles en todos los partidos.")
	print("\t4 - Imprimir grafica Goles Visitante-Local-Total."),print("\t5 - Goles como visitante por campeonato."), print("\t6 - Goles como local por campeonato."), print("\t7 - Goles totales por campeonato."),print("\t8 - Partidos como locales."),print("\t9 - Partidos como visitante."),print("\t10 - Partidos totales jugados por seleccion."),print("\t11 - Seleccion que hizo mas goles."),print("\t12 - Seleccion que recibio mas goles."),print("\t13 - Salir.")
	


def gol_local():
    suma_gl=Excel['goles_local'].sum()
    return suma_gl


def gol_visitante():
    suma_gv=Excel['goles_visita'].sum()
    return suma_gv

def total_goles():
    suma_gt= gol_local()+gol_visitante()
    return suma_gt

def goles_xtlo():
   
    for x in range (len(torneo)):
        indext=torneo.iloc[x]
        sumag1=0
        for j in range (len(goles)):
            if indext==Excel.loc[j,'torneo']:
                sumag1=sumag1+Excel.loc[j,'goles_local']
        suma_g_t1.append(sumag1)
    goles_t_l=np.array(suma_g_t1)
    return goles_t_l


def goles_xtvi():
    
    
    for x in range (len(torneo)):
            
            indext=torneo.iloc[x]
            sumag=0
            for j in range (len(goles)):
                if indext==Excel.loc[j,'torneo']:
                    sumag=sumag+Excel.loc[j,'goles_visita']
            suma_g_t.append(sumag)
    goles_t_v=np.array(suma_g_t)
    return goles_t_v

def imprimir_df_tabla_v():
    visi_t=[]        
    np4=goles_xtvi()
    for k in range (len(torneo)):        
        index2=np4[k]
        visi_t.append(index2)        
        v1=np.array(visi_t)
    DF_tabla ={'Campeonato': torneo , 'Goles como visitante': v1}
    DF_tabla_gv= pd.DataFrame(data=DF_tabla)
    return DF_tabla_gv

def imprimir_df_tabla_l():
    local_t=[]        
    np3=goles_xtlo()
    for k in range (len(torneo)):        
        index2=np3[k]
        local_t.append(index2)        
        l1=np.array(local_t)
           
    DF_tabla1 ={'Campeonato': torneo , 'Goles como local': l1}
    DF_tabla_gl= pd.DataFrame(data=DF_tabla1)
    return DF_tabla_gl


def goles_txc(): 
    t_goles1=[]  
    t_goles2=[]
    np1=goles_xtvi()  
    np2=goles_xtlo()
    for k in range (len(torneo)):
        index= np1[k]
        index2=np2[k]
        t_goles1.append(index)
        t_goles2.append(index2)
        tg1=np.array(t_goles1)
        tg2=np.array(t_goles2)
    suma_glt= tg1+tg2
    return suma_glt
    
    

def imprimir_df_txc():
    
    DF_tabla2 ={'Campeonato': torneo , 'Goles totales': goles_txc()}
    DF_tabla_gtc= pd.DataFrame(data=DF_tabla2)
    return DF_tabla_gtc

def partidos_local_s():

    for y in range (len(seleccion)):
            indext=seleccion.iloc[y]
            
            sumagl=0
            for g in range (len(goles)):
                if indext==Excel.loc[g,'local']:
                    sumagl=sumagl+1               
            suma_sl.append(sumagl)
    return suma_sl

def imprimir_partidos_local():
    
    pl=[]        
    np4=partidos_local_s()
    for n in range (len(seleccion)):        
        index2=np4[n]
        pl.append(index2)        
        pl_1=np.array(pl)
    DF_tabla8 ={'Seleccion': seleccion , 'Partidos como local': pl_1}
    DF_tabla_pl= pd.DataFrame(data=DF_tabla8)
    return DF_tabla_pl
      
    
def partidos_visitante_s():   

    for o in range (len(seleccion)):
            indexs=seleccion.iloc[o]
            sumagl1=0
            for q in range (len(goles)):
                if indexs==Excel.loc[q,'visitante']:
                    sumagl1=sumagl1+1               
            suma_sl1.append(sumagl1)

    return suma_sl1


def imprimir_partidos_visitante():
    pl=[]        
    np4=partidos_visitante_s()
    for n in range (len(seleccion)):        
        index2=np4[n]
        pl.append(index2)        
        pl_1=np.array(pl)
    DF_tabla9 ={'Seleccion': seleccion , 'Partidos como visitante': pl_1}
    DF_tabla_vl= pd.DataFrame(data=DF_tabla9)
    return DF_tabla_vl


def total_partidos_s():
    partidos_vs1 = np.array(partidos_visitante_s())
    partidos_ls1 = np.array(partidos_local_s())
        
    suma_total_p= partidos_vs1+partidos_ls1
    return suma_total_p

def imprimir_total_partidos():
    totales_partidos=[]        
    np6=total_partidos_s()
    for k in range (len(seleccion)):        
        index2=np6[k]
        totales_partidos.append(index2)        
        tp=np.array(totales_partidos)
    DF_tabla11 ={'Seleccion': seleccion , 'Partidos totales': tp}
    DF_tabla_total_partidos= pd.DataFrame(data=DF_tabla11)
    return DF_tabla_total_partidos


def goles_xsv():
       
    for o in range (len(seleccion)):
                indexs=seleccion.iloc[o]
                suma_xsv=0
                for q in range (len(goles)):
                    if indexs==Excel.loc[q,'visitante']:
                       suma_xsv=suma_xsv+Excel.loc[q,'goles_visita']                 
                goles_sv.append(suma_xsv)
    return goles_sv
            

def goles_xsl():

    for o in range (len(seleccion)):
                indexs=seleccion.iloc[o]
                suma_xsl=0
                for q in range (len(goles)):
                    if indexs==Excel.loc[q,'local']:
                       suma_xsl=suma_xsl+Excel.loc[q,'goles_local']                 
                goles_sl.append(suma_xsl)
    return goles_sl

def goleador():
    goles_xv = np.array(goles_xsv())
    goles_xs = np.array(goles_xsl())
    suma_goleador= goles_xv+goles_xs
    DF_tabla3 ={'Seleccion': seleccion , 'Goles totales': suma_goleador}
    DF_goleador= pd.DataFrame(data=DF_tabla3)
    goles_ordenado= DF_goleador.sort_values(by=['Goles totales'], ascending=(False))
    print("El mayor goleador es %s con %i goles"%(goles_ordenado.loc[10,'Seleccion'],goles_ordenado.loc[10,'Goles totales']))

          
def goles_recibidos_xsv():
       
    for o in range (len(seleccion)):
                index_r=seleccion.iloc[o]
                suma_xsv=0
                for q in range (len(goles)):
                    if index_r==Excel.loc[q,'visitante']:
                       suma_xsv=suma_xsv+Excel.loc[q,'goles_local']                 
                goles_rv.append(suma_xsv)
    return goles_rv

          
def goles_recibidos_xsl():
       
    for o in range (len(seleccion)):
                index_rl=seleccion.iloc[o]
                suma_xsl=0
                for q in range (len(goles)):
                    if index_rl==Excel.loc[q,'local']:
                       suma_xsl=suma_xsl+Excel.loc[q,'goles_visita']                 
                goles_rv1.append(suma_xsl)
    return goles_rv1

def perdedor_forever():
    goles_xv = np.array(goles_recibidos_xsv())
    goles_xs = np.array(goles_recibidos_xsl())
    suma_perdedor= goles_xv+goles_xs
    DF_tabla4 ={'Seleccion': seleccion , 'Goles recibidos': suma_perdedor}
    DF_goleador= pd.DataFrame(data=DF_tabla4)
    goles_ordenado= DF_goleador.sort_values(by=['Goles recibidos'], ascending=(False))
    print("%s fue el equipo que mas goles recibio con %i goles"%(goles_ordenado.loc[21,'Seleccion'],goles_ordenado.loc[21,'Goles recibidos']))
    
def tabla_abrev_torneo():
    DF_tabla5 ={'Campeonato': torneo , 'Abreviacion': abrev }
    DF_tabla_abrev= pd.DataFrame(data=DF_tabla5)
    return DF_tabla_abrev

def tabla_abrev_s():
    DF_tabla10 ={'Seleccion': seleccion , 'Abreviacion': abrev_s }
    DF_tabla_abrevs= pd.DataFrame(data=DF_tabla10)
    return DF_tabla_abrevs



while True:
    menu()
    opcion=int(input("Ingrese una opcion segun el menu: "))
    if opcion==1:
        print("\nLa cantidad de goles anotados como local son: ",gol_local())
        input("Has pulsado la opción 1...\npulsa enter para continuar")
    if opcion==2:        
        print("\nLa cantidad de goles anotados como visitante son: ",gol_visitante())
        input("Has pulsado la opción 2...\npulsa enter para continuar")
        
    if opcion==3:
        print("\nLa cantidad de goles total anotados son : ",total_goles())        
        input("Has pulsado la opción 3...\npulsa enter para continuar")
    if opcion==4:
        print("\nA continuacion se muestra la grafica...")
        fig, ax = plt.subplots()
        ax.set_title("Cantidad de Goles Visistante-Local-Total")
        ax.set_ylabel("Goles")
        ax.set_xlabel("")
        #crear el gráfico
        grafica_g=[gol_visitante(),gol_local(),total_goles()]
        plt.bar(grafica,grafica_g,width = 0.8,color=('#AF7AC5','#5DADE2','#2ECC71'))
        plt.yticks(grafica_g)
        plt.show()
        
        input("Has pulsado la opción 4...\npulsa enter para continuar")
    
    if opcion==5:
        print("\nA continuacion se muestra la lista de goles como visitante por torneo...\n")
        print(imprimir_df_tabla_v())
        print("Ademas se muestra la tabla de las abreviaciones usadas para los campeonatos\n")
        print(tabla_abrev_torneo())
        fig, ax = plt.subplots()
        ax.set_title("Cantidad de Goles Visistante por campeonato")
        ax.set_ylabel("Goles")
        ax.set_xlabel("")
        #crear el gráfico
        i_goles=[]   
        npi=goles_xtvi()       
        for k in range (len(torneo)):
            index= npi[k]
            i_goles.append(index)
        
        plt.bar(abrev,i_goles,width = 0.8,color=('#AF7AC5','#5DADE2','#2ECC71'))        
        plt.show()
        input("Has pulsado la opción 5...\npulsa enter para continuar")
    
    if opcion==6:
        print("\nA continuacion se muestra la lista de goles como locales por torneo...\n")
        print(imprimir_df_tabla_l())
       
        print("Ademas se muestra la tabla de las abreviaciones usadas para los campeonatos\n")
        print(tabla_abrev_torneo())
        fig, ax = plt.subplots()
        ax.set_title("Cantidad de Goles Locales por campeonato")
        ax.set_ylabel("Goles")
        ax.set_xlabel("")
        #crear el gráfico
        i_goles=[]   
        npi=goles_xtlo()       
        for k in range (len(torneo)):
            index= npi[k]
            i_goles.append(index)
        
        plt.bar(abrev,i_goles,width = 0.8,color=('#AF7AC5','#5DADE2','#2ECC71'))
        plt.show()
        
        input("Has pulsado la opción 6...\npulsa enter para continuar")
        
    if opcion==7:
        print("\nA continuacion se muestra la lista de goles totales por torneo...\n")
        print(imprimir_df_txc())  
        print("\nA continuacion se muestra la grafica...\n")
        print("Ademas se muestra la tabla de las abreviaciones usadas para los campeonatos\n")
        print(tabla_abrev_torneo())
        fig, ax = plt.subplots()
        ax.set_title("Cantidad de Goles Totales por campeonato")
        ax.set_ylabel("Goles")
        ax.set_xlabel("")
        #crear el gráfico
        i_goles=[]   
        npi=goles_txc()       
        for k in range (len(torneo)):
            index= npi[k]
            i_goles.append(index)
        
        plt.bar(abrev,i_goles,width = 0.8,color=('#AF7AC5','#5DADE2','#2ECC71'))
        plt.show()
        input("Has pulsado la opción 7...\npulsa enter para continuar")
        
    if opcion==8:
        print("\nA continuacion se muestra la lista de partidos como locales...\n")
        print(imprimir_partidos_local())
        print("Ademas se muestra la tabla de las abreviaciones usadas para las selecciones\n")
        print(tabla_abrev_s())
        fig, ax = plt.subplots()
        ax.set_title("Partidos como local")
        ax.set_ylabel("Seleccion")
        ax.set_xlabel("Partidos como local")
        #crear el gráfico
        l_partidos=[]   
        npl= partidos_local_s()  
        for k in range (len(seleccion)):
            indexs= npl[k]
            l_partidos.append(indexs)
                
        plt.barh(abrev_s,l_partidos,color=('#196F3D','#F4D03F','#1A5276','#C0392B'
        ,'#F4D03F','#154360','#5DADE2','#1E8449','#7B241C','#A93226','#D7DBDD','#78281F'))
        plt.show()
       
        input("Has pulsado la opción 8...\npulsa enter para continuar")      
    if opcion==9:
        print("\nA continuacion se muestra la lista de partidos como locales...\n")
        print(imprimir_partidos_visitante())
        print("Ademas se muestra la tabla de las abreviaciones usadas para las selecciones\n")
        print(tabla_abrev_s())
        fig, ax = plt.subplots()
        ax.set_title("Partidos como visitante")
        ax.set_ylabel("Seleccion")
        ax.set_xlabel("Partidos como visitante")
        #crear el gráfico
        v_partidos=[]   
        npv= partidos_visitante_s() 
        for k in range (len(seleccion)):
            indexs= npv[k]
            v_partidos.append(indexs)               
        plt.barh(abrev_s,v_partidos,color=('#196F3D','#F4D03F','#1A5276','#C0392B'
        ,'#F4D03F','#154360','#5DADE2','#1E8449','#7B241C','#A93226','#D7DBDD','#78281F'))
        plt.show()
        input("Has pulsado la opción 9...\npulsa enter para continuar")
        
    if opcion==10:
        print("\nA continuacion se muestra la lista de partidos totales jugados por seleccion...\n")
        print(imprimir_total_partidos())
        print("Ademas se muestra la tabla de las abreviaciones usadas para las selecciones\n")
        print(tabla_abrev_s())
        fig, ax = plt.subplots()
        ax.set_title("Partidos totales jugados")
        ax.set_ylabel("Partidos")
        ax.set_xlabel("Seleccion")
        #crear el gráfico
        t_partidos=[]   
        npts= total_partidos_s()
        for k in range (len(seleccion)):
            indexs= npts[k]
            t_partidos.append(indexs)               
        plt.bar(abrev_s,t_partidos,color=('#196F3D','#F4D03F','#1A5276','#C0392B'
        ,'#F4D03F','#154360','#5DADE2','#1E8449','#7B241C','#A93226','#D7DBDD','#78281F'))
        plt.show()
        
        input("Has pulsado la opción 10...\npulsa enter para continuar") 
    if opcion==11:
        
        goleador()
        
        input("Has pulsado la opción 11...\npulsa enter para continuar") 
    if opcion==12:
        perdedor_forever()
        
        input("Has pulsado la opción 12...\npulsa enter para continuar") 
    if opcion==13:
        print("\n---------------- Gracias por utilizar nuestro programa. ------------------")
        break      
    elif opcion<1 or opcion>13:
    	print ("")
    	input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")