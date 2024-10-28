import pandas as pd
from collections import defaultdict

def ler_dados_votacao():
    url = 'https://docs.google.com/spreadsheets/d/1zgH9vRrwofFV4JR66WIzGXVTPY6ibhRT-hONyLjWrFo/export?format=csv'
    votos_df = pd.read_csv(url)
    
    # Renomear as colunas da planilha conforme a formatação de votos
    votos_df.columns = ['Timestamp', 'Email Address', 'STX', 'SEI', 'GMX', 'ASTR', 'MNDE', 'CKB', 
                        'SAVM', 'POND', 'CRU', 'ELA', 'MKR', 'STORJ', 'GLM', 'DHT', 'ANKR', 'GRT', 
                        'IOTX', 'POWR', 'GFI', 'RLC', 'AVAX', 'NOTE', 'FORT', 'INST', 'OCEAN', 
                        'CUDOS', 'GEL', 'BOBA']
    
    return votos_df

class VotacaoSTV:
    def __init__(self):
        """Inicializa com um dicionário para armazenar os votos e as contagens."""
        self.resultados = defaultdict(int)

    def processar_voto(self, voto):
        """Processa um voto, adicionando ao dicionário de resultados."""
        for escolha in voto:
            if escolha:
                self.resultados[escolha] += 1
                break

    def calcular_primeira_colocacao(self):
        """Retorna os candidatos ordenados pela quantidade de votos."""
        return sorted(self.resultados.items(), key=lambda x: x[1], reverse=True)

    def exibir_resultados(self):
        """Exibe os resultados acumulados."""
        print("Resultados da Votação STV:")
        for candidato, votos in self.resultados.items():
            print(f"{candidato}: {votos} votos")

def main():
    """Função principal que integra a leitura dos dados e o processamento da votação."""
    # Ler os dados da planilha Google Sheets
    df_votos = ler_dados_votacao()

    # Criar uma instância da classe VotacaoSTV
    votacao = VotacaoSTV()

    # Processar cada linha de votos da planilha
    for _, row in df_votos.iterrows():
        # Cada linha contém as preferências de um votante, capturadas nas colunas de ativos
        voto = [row['STX'], row['SEI'], row['GMX'], row['ASTR'], row['MNDE'], row['CKB'], 
                row['SAVM'], row['POND'], row['CRU'], row['ELA'], row['MKR'], row['STORJ'], 
                row['GLM'], row['DHT'], row['ANKR'], row['GRT'], row['IOTX'], row['POWR'], 
                row['GFI'], row['RLC'], row['AVAX'], row['NOTE'], row['FORT'], row['INST'], 
                row['OCEAN'], row['CUDOS'], row['GEL'], row['BOBA']]
        
        # Processar o voto
        votacao.processar_voto(voto)

    # Calcular a primeira colocação para cada candidato
    votacao.calcular_primeira_colocacao()

    # Exibir os resultados finais
    votacao.exibir_resultados()

# Executar a função principal
if __name__ == "__main__":
    main()






