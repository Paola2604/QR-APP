import qrcode
from PIL import Image

# Leer datos del archivo empleado.txt
def generarQR(empleado,nombre):
        # Crear un objeto QRCode
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=15,
            border=1,
        )

        # Agregar datos al código QR (empleado)
        qr.add_data(empleado)
        qr.make(fit=True)

        # Crear una imagen del código QR
        img = qr.make_image(fill_color="black", back_color="white")

        # Cargar la imagen que deseas agregar al código QR
        imagen_personalizada = Image.open("logo.png")  # Reemplaza con la ruta de tu imagen

        # Redimensionar la imagen personalizada para que quepa en el centro del código QR
        qr_size = img.size
        imagen_personalizada.thumbnail((qr_size[0] // 6, qr_size[1] // 6))

        # Calcular la posición para centrar la imagen en el código QR
        posicion_x = (qr_size[0] - imagen_personalizada.width) // 2
        posicion_y = (qr_size[1] - imagen_personalizada.height) // 2

        # Pegar la imagen personalizada en el código QR en la posición calculada
        img.paste(imagen_personalizada, (posicion_x, posicion_y))

        # Guardar el código QR con la imagen
        nombre_img=nombre + ".png"
        img.save(nombre_img)
