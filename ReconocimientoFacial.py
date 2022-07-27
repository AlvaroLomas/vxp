# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 22:16:09 2022

@author: STEVEN
"""

import cv2
import os
import win32com.client

def reconocimientoFacial():
    dataPath = 'C:/Users/boall/OneDrive/Escritorio/Reconocimiento Facial/Data' #Cambia a la ruta donde hayas almacenado Data
    imagePaths = os.listdir(dataPath)
    print('imagePaths=',imagePaths)
    
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    
    # Leyendo el modelo
    #instalar pywin32
    face_recognizer.read('modeloLBPHFace.xml')
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    
    bocinas=win32com.client.Dispatch("SAPI.SpVoice")
    
    contador=0
    identificado=''      
    
    while True:
        ret,frame = cap.read()
        if ret == False: break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = gray.copy()
        faces = faceClassif.detectMultiScale(gray,1.3,5)
        # Detecta el rostro
        for (x,y,w,h) in faces:            
            rostro = auxFrame[y:y+h,x:x+w]
            rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
            result = face_recognizer.predict(rostro)            
            cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
            # Detecta el nombre y reproduce el saludo
            if result[1] < 70:
                cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
                identificado2=identificado
                identificado= imagePaths[result[0]]
                if contador==0 and identificado != identificado2:
                    texto=("Hola",'{}'.format(imagePaths[result[0]]),"bienvenido")
                    bocinas.Speak(texto)                
                    contador=contador+1
            else:
                cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
        cv2.imshow('frame',frame)
        
        #Cerrar el programa con la tecla "q"
        k = cv2.waitKey(1)
        if k == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()


