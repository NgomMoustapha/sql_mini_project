from collections import OrderedDict

import streamlit as st

from streamlit_app import style

# TODO : change TITLE, TEAM_MEMBERS and PROMOTION values in config.py.
import config

# TODO : you can (and should) rename and add tabs in the ./tabs folder, and import them here.
from tabs import intro, second_tab, third_tab


st.set_page_config(
    page_title=config.TITLE,
    page_icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS4_bnuiBj-yvKr-I6XxgqcgEQHCIdRZrlQ_g&usqp=CAU",
)

with open("style.css", "r") as f:
    style = f.read()

st.markdown(f"<style>{style}</style>", unsafe_allow_html=True)


# TODO: add new and/or renamed tab in this ordered dict by
# passing the name in the sidebar as key and the imported tab
# as value as follow :
TABS = OrderedDict(
    [
        (intro.sidebar_name, intro),
        (second_tab.sidebar_name, second_tab),
       # (third_tab.sidebar_name, third_tab),
    ]
)


def run():
    st.sidebar.image(
        "https://designvault.io/wp-content/uploads/2020/06/IMG_2201-600x1299.png",
        width=200,
    )
    tab_name = st.sidebar.radio("", list(TABS.keys()), 0)
    st.sidebar.markdown("---")

    st.sidebar.markdown("### Auteur:")
    for member in config.AUTEUR:
        st.sidebar.markdown(member.sidebar_markdown(), unsafe_allow_html=True)

    tab = TABS[tab_name]

    tab.run()


if __name__ == "__main__":
    run()
