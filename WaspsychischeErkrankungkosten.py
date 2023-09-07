import streamlit as st
import pandas as pd
import altair as alt

st.header("Was psychische Erkrankung kosten")
st.subheader("Von psychischen Problemen direkt oder indirekt verursachte Kosten als Anteil des BIP*")

source = pd.DataFrame({
        'Anteil (%)': [5.4, 4.8, 4.2, 4.1, 4.1, 3.7, 3.3, 2.5],
        'Nation': ['Dänemark', 'Deutschland', 'Spanien', 'EU', 'Großbritannien', 'Frankreich', 'Italien', 'Tschechien']
})
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil (%):Q',
        x='Nation:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    2015
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: OECD")