
import requests

def get_cat_image():
    """Busca uma imagem aleatória de um gato usando a Cat API"""
    url = "https://cataas.com/cat"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["message"]
    else:
        return "Erro ao buscar imagem."

def main():
    print("Bem-vindo ao sistema de exemplo!")
    print("Buscando uma imagem aleatória de gato...")
    print("URL da imagem:", get_cat_image())


if __name__ == "__main__":
    main()
