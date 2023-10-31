import cv2
import lecturaempleados
capture = cv2.VideoCapture(0)
import sys

def lector():
        if not capture.isOpened():
            print("Error: No se pudo abrir la cámara.")
            exit()
        x=1
        while capture.isOpened()and x==1:
            ret, frame = capture.read()

            if cv2.waitKey(1) == ord('s') or cv2.waitKey(1) ==  ord('S'):
                break
            
            qrDetector = cv2.QRCodeDetector()
            data, bbox, rectifiedImage = qrDetector.detectAndDecode(frame)


            if len(data) > 0:
                print(f'Dato: {data}')
                cv2.imshow('webCam', rectifiedImage)
                x=0

                # Crea la lista y escribe en el archivo dentro del bucle

                with open("novedad.txt", "w",encoding="utf-8") as archivo:
                    archivo.write(data)
                    cv2.destroyAllWindows()
                    print(data) 
                    capture.release()  
                with open("novedad.txt", "r",encoding="utf-8") as archivo:
                    linea=archivo.readline()
                    if linea!="":

                        resultado=lecturaempleados.lectura()
                        if resultado==0:
                            return(0)

                        cv2.destroyAllWindows()
                        print(data)
                        
                sys.exit(0)

            else:
                cv2.imshow('webCam', frame)

        capture.release()
        cv2.destroyAllWindows()
        


