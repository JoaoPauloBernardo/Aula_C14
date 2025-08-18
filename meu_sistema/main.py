
import requests

def get_dog_image():
    """Busca uma imagem aleatória de cachorro usando a Dog API"""
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["message"]
    else:
        return "Erro ao buscar imagem."

def main():
    print("Bem-vindo ao sistema de exemplo!")
    print("Buscando uma imagem aleatória de cachorro...")
    print("URL da imagem:", get_dog_image())

if __name__ == "__main__":
    main()
