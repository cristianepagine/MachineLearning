import cv2
from google.colab.patches import cv2_imshow
import requests
import numpy as np
from io import BytesIO

def download_image(url):
    response = requests.get(url)
    image = np.asarray(bytearray(response.content), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image

# URL da imagem
url = "https://cdn.autopapo.com.br/box/uploads/2019/02/18163003/jaguar-e-type-1961-732x488.jpeg"

# Baixar a imagem da web
image = download_image(url)

# Se a imagem foi baixada com sucesso
if image is not None:
    # Transformar em tons de cinza
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Binarizar
    _, binary = cv2.threshold(grayscale, 127, 255, cv2.THRESH_BINARY)

    # Mostrar as imagens
    cv2_imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    cv2_imshow(grayscale)
    cv2_imshow(binary)
else:
    print("Falha ao baixar a imagem. Insira uma URL com imagem válida")
