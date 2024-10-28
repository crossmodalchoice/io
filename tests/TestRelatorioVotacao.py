import unittest
import pandas as pd
from collections import defaultdict
from colab_votacao import VotacaoSTV

def ler_dados_votacao():
    url = 'https://docs.google.com/spreadsheets/d/1zgH9vRrwofFV4JR66WIzGXVTPY6ibhRT-hONyLjWrFo/export?format=csv'
    votos_df = pd.read_csv(url)
    votos_df.columns = ['Timestamp', 'Email Address', 'STX', 'SEI', 'GMX', 'ASTR', 'MNDE', 'CKB', 
                        'SAVM', 'POND', 'CRU', 'ELA', 'MKR', 'STORJ', 'GLM', 'DHT', 'ANKR', 'GRT', 
                        'IOTX', 'POWR', 'GFI', 'RLC', 'AVAX', 'NOTE', 'FORT', 'INST', 'OCEAN', 
                        'CUDOS', 'GEL', 'BOBA']
    return votos_df

class TestRelatorioVotacao(unittest.TestCase):
    def setUp(self):
        self.votacao = VotacaoSTV()

    def test_relatorio_votos(self):
        self.votacao.processar_voto(["STX", "SEI", "GMX"])
        self.votacao.processar_voto(["SEI", "STX", "ELA"])
        self.votacao.processar_voto(["GMX", "STX", "POWR"])
        resultados = self.votacao.calcular_primeira_colocacao()
        self.assertEqual(resultados[0][0], 'STX')
        self.assertEqual(resultados[1][0], 'SEI')

if __name__ == "__main__":
    unittest.main()