import requests
import os
from urllib.parse import urlparse

def download_images(base_url, num_images):
    try:
        counter = 1
        for i in range(1, num_images + 1):
            image_name = f"image_{counter:02d}.jpg"
            image_urls = [
                f"{base_url}-{i:02d}.jpg",
                f"{base_url}-{i}.jpg",
                f"{base_url}{i:02d}.jpg",
                f"{base_url}{i}.jpg",
            ]
            for image_url in image_urls:
                if not os.path.exists(image_name):
                    print(f"Tentando baixar {image_url}")
                    response = requests.get(image_url)
                    if response.status_code == 200:
                        parsed_url = urlparse(image_url)
                        image_name = os.path.basename(parsed_url.path)
                        download_image(image_url, image_name)
                        counter += 1
                        break
                    else:
                        print(f"Erro ao baixar a imagem {image_url}. Status code: {response.status_code}")
                else:
                    print(f"A imagem {image_name} já existe, pulando para a próxima.")
                    counter += 1
                    break
            else:
                print(f"Nenhuma imagem válida encontrada para o índice {i}.")
        print("Todas as imagens foram baixadas com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

def download_image(url, image_name):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(image_name, "wb") as f:
                f.write(response.content)
            print(f"Imagem {image_name} baixada com sucesso!")
        else:
            print(f"Erro ao baixar a imagem {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Ocorreu um erro ao baixar a imagem {url}: {str(e)}")

# Solicitar a URL da imagem ao usuário
url_imagem = input("Insira a URL da imagem: ")

# Definir o número total de imagens
num_images = int(input("Insira o número total de imagens: "))

# Baixar as imagens
download_images(url_imagem, num_images)