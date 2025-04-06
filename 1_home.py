import streamlit as st
import webbrowser
import pandas as pd
import os
from datetime import datetime

# Caminho relativo para o arquivo CSV
file_path = os.path.join(os.path.dirname(__file__), "datasets", "CLEAN_FIFA23_official_data.csv")

# Verifica se o arquivo existe antes de tentar carregá-lo
if not os.path.exists(file_path):
    st.error("Arquivo não encontrado! Verifique o caminho do arquivo.")
else:
    # Carregar os dados apenas uma vez e armazená-los no estado da sessão
    if "data" not in st.session_state:
        # Carrega o dataset
        df_data = pd.read_csv(file_path, index_col=0)

        # Filtra os dados
        df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]  # Filtra pelo ano atual
        df_data = df_data[df_data["Value(£)"] > 0]  # Filtra jogadores com valor de mercado maior que 0
        df_data = df_data.sort_values(by="Overall", ascending=False)  # Ordena por Overall

        # Salva o dataframe no session_state para uso posterior
        st.session_state["data"] = df_data

    # Cabeçalho e informações
    st.markdown("# FIFA23 OFFICIAL DATASET! ⚽️")
    st.sidebar.markdown("Desenvolvido por [Asimov Academy](https://asimov.academy)")

    # Botão para acessar os dados no Kaggle
    btn = st.button("Acesse os dados no Kaggle")
    if btn:
        webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")

    # Descrição do conjunto de dados
    st.markdown("""
        O conjunto de dados
        de jogadores de futebol de 2017 a 2023 fornece informações 
        abrangentes sobre jogadores de futebol profissionais.
        O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos 
        do jogador, características físicas, estatísticas de jogo, detalhes do contrato e 
        afiliações de clubes. 

        Com **mais de 17.000 registros**, este conjunto de dados oferece um recurso valioso para 
        analistas de futebol, pesquisadores e entusiastas interessados em explorar vários 
        aspectos do mundo do futebol, pois permite estudar atributos de jogadores, métricas de 
        desempenho, avaliação de mercado, análise de clubes, posicionamento de jogadores e 
        desenvolvimento do jogador ao longo do tempo.
    """)

#"streamlit run "C:\Users\Usuario\PycharmProjects\ASIMOV\Introducao_Streamlit\Deploy_streamlit_cloud\streamlit_fifa_deploy_elv/1_home.py"
