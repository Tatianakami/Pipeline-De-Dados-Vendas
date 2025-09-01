Gerador e Analisador de Vendas
📊 Sobre o Projeto
O seu projeto é um Gerador e Analisador de Vendas. A função dele é simular o trabalho de um analista de dados que precisa pegar dados brutos, processá-los e transformá-los em informações úteis para o negócio.

Ele funciona em três etapas principais:

Extração de Dados: Em um projeto real, você extrairia dados de um banco de dados ou API. No seu projeto, isso é simulado com o uso do SQLite para criar uma tabela de vendas com dados de exemplo.

Processamento e Análise: Você usa o Pandas, uma das bibliotecas mais poderosas do Python, para ler os dados do banco de dados e calcular uma métrica importante: o total de vendas diárias.

Visualização e Comunicação: Esta é a etapa de entrega. O projeto não só salva os dados processados em um arquivo CSV (que é útil para planilhas), mas também usa o Matplotlib para criar um gráfico de barras em formato de imagem (.png), o que torna a informação muito mais fácil de ser entendida.

![Gráfico de Vendas](/assets/grafico.jpg)
Extração e Processamento de Dados: Utilizando o SQLite para simular um banco de dados e o pandas para manipular as informações.

Análise e Visualização: Gerando um relatório em formato CSV e uma visualização de dados em formato de gráfico, usando a biblioteca matplotlib.

![Gráfico de Vendas](/assets/relatorio.jpg)

🛠️ Tecnologias Utilizadas
Python: A linguagem de programação principal.

Pandas: Para a manipulação e análise de dados.

Matplotlib: Para a criação e exportação do gráfico.

SQLite3: Módulo embutido do Python para o banco de dados.

🚀 Como Rodar o Projeto
Siga os passos abaixo para executar a aplicação em sua máquina.

1. Pré-requisitos
Certifique-se de que você tem o Python instalado e que criou um ambiente virtual.

2. Instalação das Bibliotecas
Com seu ambiente virtual ativado, instale as bibliotecas necessárias com o seguinte comando:

pip install pandas matplotlib

3. Execução
Execute o script no terminal:

python gerador_relatorio.py

Após a execução, dois novos arquivos serão criados na sua pasta:

relatorio_vendas.csv (o relatório em tabela)



📝 Próximos Passos
Este projeto pode ser expandido para incluir outras funcionalidades e se tornar ainda mais robusto. Algumas ideias incluem:

Automação de E-mail: Adicionar a funcionalidade de enviar o relatório e o gráfico automaticamente por e-mail.

Web Scraping: Modificar o script para coletar os dados de uma fonte real, como um site, em vez de um banco de dados local.