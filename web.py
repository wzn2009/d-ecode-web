#实现加密的库
import base64
#实现程序转网站的库
import streamlit as st

#实现加密的函数
def enc():

    bs = base64.b64encode(text.encode('utf-8'))
    bs = str(bs).lstrip('b')
    return bs

#实现解密的函数
def dec():
    bbs = str(base64.b64decode(text), 'utf-8')
    return bbs

#标题（相当于html中的h1）
st.title('加密-解密')
#创建输入框
text = st.text_input('请输入内容：')

#创建按钮，并在点击时调用函数，获取其返回值并显示在页面上
if st.button('加密'):
    st.write('请复制加密后的文字：')
    st.write(enc())
elif st.button('解密'):
    st.write('解密后的文字为：')
    st.write(dec())
    
