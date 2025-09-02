# test_main.py
import unittest
from unittest.mock import patch, MagicMock
import requests
import main

POSITIVE_COUNT = 0
NEGATIVE_COUNT = 0


class TestGetCatImage(unittest.TestCase):

    # --------- Casos Positivos ---------
    @patch("requests.get")
    def test_status_200_com_json_valido(self, mock_get):
        global POSITIVE_COUNT
        POSITIVE_COUNT += 1
        print("\n[POSITIVO] Rodando: test_status_200_com_json_valido")

        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"message": "https://cataas.com/cat1"}
        mock_get.return_value = mock_resp

        result = main.get_cat_image()
        self.assertEqual(result, "https://cataas.com/cat1")

    @patch("requests.get")
    def test_status_200_com_diferente_url(self, mock_get):
        global POSITIVE_COUNT
        POSITIVE_COUNT += 1
        print("\n[POSITIVO] Rodando: test_status_200_com_diferente_url")

        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"message": "https://cataas.com/cat2"}
        mock_get.return_value = mock_resp

        result = main.get_cat_image()
        self.assertTrue("cataas.com" in result)

    @patch("requests.get")
    def test_resposta_json_contem_chave_message(self, mock_get):
        global POSITIVE_COUNT
        POSITIVE_COUNT += 1
        print("\n[POSITIVO] Rodando: test_resposta_json_contem_chave_message")

        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"message": "https://cataas.com/cat3"}
        mock_get.return_value = mock_resp

        result = main.get_cat_image()
        self.assertTrue(result.startswith("https://"))

    @patch("requests.get")
    def test_retorna_url_com_https(self, mock_get):
        global POSITIVE_COUNT
        POSITIVE_COUNT += 1
        print("\n[POSITIVO] Rodando: test_retorna_url_com_https")

        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"message": "https://cats.com/valid"}
        mock_get.return_value = mock_resp

        result = main.get_cat_image()
        self.assertIn("https://", result)

    @patch("requests.get")
    def test_variacao_de_urls_validas(self, mock_get):
        global POSITIVE_COUNT
        POSITIVE_COUNT += 1
        print("\n[POSITIVO] Rodando: test_variacao_de_urls_validas")

        urls = ["https://cataas.com/cat4", "https://cataas.com/cat5"]
        for url in urls:
            mock_resp = MagicMock()
            mock_resp.status_code = 200
            mock_resp.json.return_value = {"message": url}
            mock_get.return_value = mock_resp
            result = main.get_cat_image()
            self.assertEqual(result, url)

    @patch("requests.get")
    def test_resultado_eh_string(self, mock_get):
        global POSITIVE_COUNT
        POSITIVE_COUNT += 1
        print("\n[POSITIVO] Rodando: test_resultado_eh_string")

        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"message": "https://cataas.com/cat6"}
        mock_get.return_value = mock_resp

        result = main.get_cat_image()
        self.assertIsInstance(result, str)

    @patch("requests.get")
    def test_status_200_nao_retorna_erro(self, mock_get):
        global POSITIVE_COUNT
        POSITIVE_COUNT += 1
        print("\n[POSITIVO] Rodando: test_status_200_nao_retorna_erro")

        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"message": "https://cataas.com/cat7"}
        mock_get.return_value = mock_resp

        result = main.get_cat_image()
        self.assertNotEqual(result, "Erro ao buscar imagem.")

    @patch("requests.get")
    def test_chamada_api_realizada(self, mock_get):
        global POSITIVE_COUNT
        POSITIVE_COUNT += 1
        print("\n[POSITIVO] Rodando: test_chamada_api_realizada")

        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"message": "https://cataas.com/cat8"}
        mock_get.return_value = mock_resp

        main.get_cat_image()
        mock_get.assert_called_once()

    @patch("requests.get")
    def test_chave_message_retornada(self, mock_get):
        global POSITIVE_COUNT
        POSITIVE_COUNT += 1
        print("\n[POSITIVO] Rodando: test_chave_message_retornada")

        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"message": "https://cataas.com/cat9"}
        mock_get.return_value = mock_resp

        result = main.get_cat_image()
        self.assertRegex(result, r"^https://")

    @patch("requests.get")
    def test_multipla_chamadas_ok(self, mock_get):
        global POSITIVE_COUNT
        POSITIVE_COUNT += 1
        print("\n[POSITIVO] Rodando: test_multipla_chamadas_ok")

        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"message": "https://cataas.com/cat10"}
        mock_get.return_value = mock_resp

        for _ in range(5):
            result = main.get_cat_image()
            self.assertEqual(result, "https://cataas.com/cat10")

    # --------- Casos Negativos ---------
    @patch("requests.get")
    def test_status_404(self, mock_get):
        global NEGATIVE_COUNT
        NEGATIVE_COUNT += 1
        print("\n[NEGATIVO] Rodando: test_status_404")

        mock_resp = MagicMock()
        mock_resp.status_code = 404
        mock_get.return_value = mock_resp
        result = main.get_cat_image()
        self.assertEqual(result, "Erro ao buscar imagem.")

    @patch("requests.get")
    def test_status_500(self, mock_get):
        global NEGATIVE_COUNT
        NEGATIVE_COUNT += 1
        print("\n[NEGATIVO] Rodando: test_status_500")

        mock_resp = MagicMock()
        mock_resp.status_code = 500
        mock_get.return_value = mock_resp
        result = main.get_cat_image()
        self.assertEqual(result, "Erro ao buscar imagem.")

    @patch("requests.get")
    def test_status_diferente_200(self, mock_get):
        global NEGATIVE_COUNT
        NEGATIVE_COUNT += 1
        print("\n[NEGATIVO] Rodando: test_status_diferente_200")

        mock_resp = MagicMock()
        mock_resp.status_code = 302
        mock_get.return_value = mock_resp
        result = main.get_cat_image()
        self.assertEqual(result, "Erro ao buscar imagem.")

    @patch("requests.get")
    def test_json_invalido(self, mock_get):
        global NEGATIVE_COUNT
        NEGATIVE_COUNT += 1
        print("\n[NEGATIVO] Rodando: test_json_invalido")

        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.side_effect = ValueError("JSON inválido")
        mock_get.return_value = mock_resp

        with self.assertRaises(ValueError):
            main.get_cat_image()

    @patch("requests.get")
    def test_timeout(self, mock_get):
        global NEGATIVE_COUNT
        NEGATIVE_COUNT += 1
        print("\n[NEGATIVO] Rodando: test_timeout")

        mock_get.side_effect = requests.exceptions.Timeout
        with self.assertRaises(requests.exceptions.Timeout):
            main.get_cat_image()

    @patch("requests.get")
    def test_connection_error(self, mock_get):
        global NEGATIVE_COUNT
        NEGATIVE_COUNT += 1
        print("\n[NEGATIVO] Rodando: test_connection_error")

        mock_get.side_effect = requests.exceptions.ConnectionError
        with self.assertRaises(requests.exceptions.ConnectionError):
            main.get_cat_image()

    @patch("requests.get")
    def test_http_error(self, mock_get):
        global NEGATIVE_COUNT
        NEGATIVE_COUNT += 1
        print("\n[NEGATIVO] Rodando: test_http_error")

        mock_get.side_effect = requests.exceptions.HTTPError
        with self.assertRaises(requests.exceptions.HTTPError):
            main.get_cat_image()

    @patch("requests.get")
    def test_request_exception(self, mock_get):
        global NEGATIVE_COUNT
        NEGATIVE_COUNT += 1
        print("\n[NEGATIVO] Rodando: test_request_exception")

        mock_get.side_effect = requests.exceptions.RequestException
        with self.assertRaises(requests.exceptions.RequestException):
            main.get_cat_image()

    @patch("requests.get")
    def test_status_403_proibido(self, mock_get):
        global NEGATIVE_COUNT
        NEGATIVE_COUNT += 1
        print("\n[NEGATIVO] Rodando: test_status_403_proibido")

        mock_resp = MagicMock()
        mock_resp.status_code = 403
        mock_get.return_value = mock_resp
        result = main.get_cat_image()
        self.assertEqual(result, "Erro ao buscar imagem.")


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestGetCatImage)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print("\n=== RESUMO FINAL ===")
    print(f"Testes positivos rodados: {POSITIVE_COUNT}/10")
    print(f"Testes negativos rodados: {NEGATIVE_COUNT}/10")
    print("====================")
