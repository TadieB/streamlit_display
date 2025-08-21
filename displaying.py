import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.markdown("# *Streamlit* Is Awesome! :sunglasses: ")

st.subheader('st.write')
st.write("Hello World, I am *Tadie!* :sunglasses:")

st.write(1234)

df = pd.DataFrame({
    "first col.": [1,2,3],
    "second col.": [10,20,30]
})

st.write("Dataframe given below", df, " the data frame is shown above.")

df2 = pd.DataFrame(
    np.random.randn(200,3),
    columns = ['a','b','c']
)

c = alt.Chart(df2).mark_circle().encode(
    x='a',y='b', size='c', color='c', tooltip=['a','b','c']
)

st.write(c)

st.caption("Amazing Chart Illustrations!")


st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

x = '''def hi(): 
           print("Hi! Tad.")'''

st.code(x, language='python')

code = '''Is it a crown or boat?
                        ii
                      iiiiii
WWw                 .iiiiiiii.                ...:
 WWWWWWw          .iiiiiiiiiiii.         ........
  WWWWWWWWWWw    iiiiiiiiiiiiiiii    ...........
   WWWWWWWWWWWWWWwiiiiiiiiiiiiiiiii............
    WWWWWWWWWWWWWWWWWWwiiiiiiiiiiiiii.........
     WWWWWWWWWWWWWWWWWWWWWWwiiiiiiiiii.......
      WWWWWWWWWWWWWWWWWWWWWWWWWWwiiiiiii....
       WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWwiiii.
          -MMMWWWWWWWWWWWWWWWWWWWWWWMMM-
'''
st.code(code, language=None)

