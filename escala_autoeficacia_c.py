import streamlit as st




# Perguntas da Escala de Autoeficácia Geral
questions = [
    "Sempre consigo resolver problemas difíceis se me esforçar suficientemente.",
    "Se alguém se opõe a mim, consigo encontrar os meios e formas de conseguir o que quero.",
    "É fácil para mim manter meus objetivos e alcançar minhas metas.",
    "Tenho confiança de que poderia lidar eficientemente com eventos inesperados.",
    "Graças à minha engenhosidade, sei como lidar com situações imprevistas.",
    "Consigo resolver a maioria dos problemas se investir o esforço necessário.",
    "Consigo manter a calma ao enfrentar dificuldades porque posso confiar em minhas habilidades de enfrentamento.",
    "Quando confrontado com um problema, geralmente consigo encontrar várias soluções.",
    "Se estou em apuros, geralmente consigo pensar em uma solução.",
    "Geralmente consigo lidar com qualquer situação que surja."
]

options = ["Nada verdadeiro", "Quase nada verdadeiro", "Moderadamente verdadeiro", "Exatamente verdadeiro"]



st.title("Escala de Autoeficácia Geral (GSE)")

id = st.text_input('Escreva o seu código de identificação: ')

# Lista para armazenar as respostas
answers = []


for idx, question in enumerate(questions):
    st.write(f"{idx + 1}. {question}")
    selected_option = st.radio("", options, key=f'{idx}_radio')
    answers.append(selected_option)
    st.write("\n")

if st.button("Enviar Respostas"):
    with open(f"{id}_answers.txt", "w") as file:
        for idx, (question, answer) in enumerate(zip(questions, answers)):
            file.write(f"{idx + 1}. {question}\nResposta: {answer}\n\n")

    st.write(answers)