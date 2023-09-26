#REPRODUZIR VIDEO

import cv2  

video = cv2.VideoCapture('video.mp4') #esse cara lê o arquivo de video

while True: #esse comando é pra ele ler o vídeo sem interromper, ele faz um loop

check , img = video.read() #lê o próximo frame

imgRedim = cv2.resize(img,(1280,720)) #redimensiona o video

cv2.imshow('video' , imgRedim) #Mostra em uma janela esses frames redimensionados

cv2.waitKey(10) #espera 0,01 segundo pra continuar o frame