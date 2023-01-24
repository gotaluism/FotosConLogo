# import matplotlib.pyplot as plt
# import cv2
# imagen=cv2.imread('foto1.png')
# imagen=cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
# plt.imshow(imagen)
# #plt.show()

# imagenLogo=cv2.imread('logoDegradadoFotos.png')
# imagenLogo=cv2.cvtColor(imagenLogo,cv2.COLOR_BGR2RGB)

# plt.imshow(imagenLogo)
# #plt.show()

# logo= imagenLogo.shape
# imagenDim=imagen.shape

# imagenLogo=cv2.resize(imagenLogo,(100,100))

# #plt.imshow(imagenLogo)


# parteImagen1=imagen[imagenDim[0]-100:imagenDim[0],0:100]  #Y/X
# plt.imshow(parteImagen1)


# mezclaImg=cv2.addWeighted(src1=parteImagen1,alpha=0.5,src2=imagenLogo,beta=0.5,gamma=0)
# plt.imshow(mezclaImg)


# imagen[imagenDim[0]-100:imagenDim[0],0:100]=mezclaImg
# plt.imshow(imagen)
# plt.show()



#FORMA 2----------------------------
import cv2 
import matplotlib.pyplot as plt
import os



def cambiarNombreArchivos():
    path=os.chdir("C:\\Users\\Luis Miguel\\OneDrive - Universidad EAFIT\\OneDocumentos\\ROPA MYOSE PROYECTO\\ProyectoCodigo\\CodigoFotos\\fotos1")
    i=0
    for file in os.listdir(path):
        if file=="1foto{}.png".format(i):
            pass
        else:
            new_file_name="1foto{}.png".format(i)
            os.rename(file, new_file_name)
        i=i+1    

def recorreArchivos():
    path=os.chdir("C:\\Users\\Luis Miguel\\OneDrive - Universidad EAFIT\\OneDocumentos\\ROPA MYOSE PROYECTO\\ProyectoCodigo\\CodigoFotos\\fotos1")
    for file in os.listdir(path):
        print(file)
        ponerCorazon(file)


def ponerCorazon(nombreArchivo):
    error=0
    fondo=cv2.imread("C:\\Users\\Luis Miguel\\OneDrive - Universidad EAFIT\\OneDocumentos\\ROPA MYOSE PROYECTO\\ProyectoCodigo\\CodigoFotos\\fotos1\\{}".format(nombreArchivo))#jpg
    try:
        fondo=cv2.cvtColor(fondo,cv2.COLOR_BGR2BGRA)
    except Exception as e:
        print("Error en la foto: "+nombreArchivo)
        error=1
    
    if error==1:
        pass
    else:
        logo=cv2.imread('C:\\Users\\Luis Miguel\\OneDrive - Universidad EAFIT\\OneDocumentos\\ROPA MYOSE PROYECTO\\ProyectoCodigo\\CodigoFotos\\logoDegradadoFotos.png',cv2.IMREAD_UNCHANGED)
        #plt.imshow(logo)
        #plt.show()
        #dimLogo=logo.shape
        dimFondo=fondo.shape
        if (dimFondo[0]>dimFondo[1]):
            resultado=int((dimFondo[1]*0.2))
            #print(resultado)
            logo=cv2.resize(logo,(resultado,resultado))
        else:
            resultado=int((dimFondo[0]*0.2))
            #print(resultado)
            logo=cv2.resize(logo,(resultado,resultado))

        filaDeseada=dimFondo[0]-resultado         # x      Y/X
        columnaDeseada=dimFondo[1]-resultado  #y 

        for i in range(logo.shape[0]):
            for j in range(logo.shape[1]):
                if (logo[i,j][3]!=0):
                    fondo[i+filaDeseada,j+columnaDeseada]=logo[i,j]

        #fondoo=cv2.cvtColor(fondo,cv2.IMREAD_ANYCOLOR)



        #plt.show()
        os.remove("C:\\Users\\Luis Miguel\\OneDrive - Universidad EAFIT\\OneDocumentos\\ROPA MYOSE PROYECTO\\ProyectoCodigo\\CodigoFotos\\fotos1\\{}".format(nombreArchivo))
        #cv2.imshow('imagenNena',fondoo)
        cv2.imwrite("C:\\Users\\Luis Miguel\\OneDrive - Universidad EAFIT\\OneDocumentos\\ROPA MYOSE PROYECTO\\ProyectoCodigo\\CodigoFotos\\fotos1\\{}".format(nombreArchivo),fondo)

#cambiarNombreArchivos()
recorreArchivos()






#resultado=int((dimFondo[1])*0.2)
#logo=cv2.resize(logo,(resultado,resultado))

#print(logo.shape)


#print(dimLogo,dimFondo)



            


