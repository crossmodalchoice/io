# Análise de Votação de Ativos

Este projeto analisa os resultados de uma votação sobre a preferência de investimento em diferentes ativos. Os dados da votação são extraídos de uma planilha Google Sheets, processados e visualizados em gráficos de barras e radar.

## Funcionalidades

* **Extração de dados:** Lê os dados da votação de uma planilha Google Sheets especificada.
* **Processamento de dados:** Calcula a pontuação total de cada ativo com base nas escolhas dos votantes (1ª, 2ª e 3ª escolhas).
* **Visualização de dados:** Gera dois gráficos:
    * **Gráfico de barras:** Mostra os 15 ativos mais votados, ordenados por pontuação total. O gráfico possui um estilo visual com fundo preto e cores vibrantes.
    * **Gráfico de radar:** Apresenta a pontuação dos 15 ativos mais votados em um formato radial, permitindo uma comparação visual das pontuações. O gráfico também tem um estilo com fundo preto e cores vibrantes.
* **Identificação do vencedor:** Determina o ativo vencedor com base na maior pontuação total.
* **Salvamento de gráficos:** Salva os gráficos gerados no Google Drive.

## Pré-requisitos

* **Python 3:** Certifique-se de ter o Python 3 instalado.
* **Bibliotecas Python:** Instale as seguintes bibliotecas:
    ```bash
    pip install pandas gspread google-auth google-api-python-client seaborn matplotlib numpy
    ```
* **Google Colab:** Este código foi projetado para ser executado no Google Colab.  A autenticação e a montagem do Google Drive são tratadas no código.
* **Planilha Google Sheets:** Crie uma planilha Google Sheets com os dados da votação. A URL da planilha deve ser especificada na variável `PLANILHA_URL` no código.  A planilha deve conter uma aba chamada "votos" com as colunas formatadas conforme o exemplo no código.
* **Permissões:** Certifique-se de que a conta do Google utilizada no Google Colab tenha permissão para acessar a planilha Google Sheets.

## Como usar

1. **Copie o código:** Copie todo o código Python fornecido.
2. **Abra o Google Colab:** Abra um novo notebook no Google Colab.
3. **Cole o código:** Cole o código copiado no notebook do Colab.
4. **Configure a URL da planilha:** Substitua o valor da variável `PLANILHA_URL` pela URL da sua planilha Google Sheets.
5. **Execute o código:** Execute o código no Colab.  Você será solicitado a autenticar sua conta do Google para acessar a planilha.
6. **Visualize os resultados:** Os gráficos gerados serão exibidos no notebook do Colab e salvos na pasta "io" do seu Google Drive. O nome do ativo vencedor também será impresso no console.

## Estrutura do código

* **`plot_bar_chart(resultados)`:** Função que gera o gráfico de barras.
* **`plot_radar(resultados)`:** Função que gera o gráfico de radar.
* **Bloco principal:** Contém o código para autenticação, acesso à planilha, processamento de dados, chamada das funções de plotagem e salvamento dos gráficos.

## Personalização

* **Cores:** As cores dos gráficos podem ser personalizadas alterando os valores hexadecimais na paleta de cores.
* **Tamanho dos gráficos:** O tamanho dos gráficos pode ser ajustado modificando os parâmetros `figsize` nas funções de plotagem.
* **Nome da aba:** O nome da aba na planilha pode ser alterado modificando o valor da variável `aba`.
* **Nomes das colunas:** Os nomes das colunas na planilha devem corresponder aos nomes usados no código.  Ajuste o código se os nomes das colunas forem diferentes.


## Solução de problemas

* **`FileNotFoundError`:** Se você encontrar este erro, certifique-se de que o Google Drive esteja montado corretamente executando `drive.mount('/content/drive')` antes de tentar salvar as figuras.
* **Problemas de autenticação:** Certifique-se de que a conta do Google utilizada no Colab tenha permissão para acessar a planilha.
* **Erros de formato de dados:** Verifique se os dados na planilha estão no formato correto e se os nomes das colunas correspondem aos usados no código.
