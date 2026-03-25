import streamlit as st
import base64
import time
from datetime import datetime

# --- 1. ARKA PLAN FONKSİYONU ---
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    try:
        bin_str = get_base64(png_file)
        page_bg_img = f'''
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{bin_str}");
            background-size: cover;
            background-position: center;
        }}
        .stMainBlockContainer {{
            background-color: rgba(10, 2, 5, 0.75); 
            border-radius: 25px;
            padding: 35px !important;
            margin-top: 30px;
            border: 2px solid #FFD700;
            box-shadow: 0 0 35px #FFD700;
        }}
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)
    except:
        st.markdown("<style>.stApp {background-color: #0a0205;}</style>", unsafe_allow_html=True)

# --- 2. AYARLAR ---
st.set_page_config(page_title="30 Mart: Bir Mucize", page_icon="🌹")
set_background('ask.png')

# --- 3. PREMIUM CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Satisfy&family=Great+Vibes&display=swap');
    .romantic-title { font-family: 'Great Vibes', cursive; color: #FFD700; text-align: center; font-size: 60px; text-shadow: 0 0 20px #FFD700; margin-bottom: 10px; }
    .siir-box { font-family: 'Dancing Script', cursive; color: #ffffff; font-size: 28px; text-align: center; line-height: 1.6; }
    .question-box { font-family: 'Satisfy', cursive; color: #F48FB1; font-size: 26px; text-align: center; margin-bottom: 20px; }
    .stButton>button { background-color: #D32F2F !important; color: white !important; border-radius: 50px !important; border: 2px solid #FFD700 !important; font-size: 21px !important; width: 100%; height: 3em !important; }
    .stRadio>div { background-color: rgba(255, 255, 255, 0.05); border-radius: 15px; padding: 15px; border: 1px solid #FFD700; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. AKIŞ YÖNETİMİ ---
if 'asama' not in st.session_state:
    st.session_state.asama = 'giris'
if 'parilti_seviyesi' not in st.session_state:
    st.session_state.parilti_seviyesi = 0
if 'soru_no' not in st.session_state:
    st.session_state.soru_no = 1

# --- AŞAMA 1: GİRİŞ ---
if st.session_state.asama == 'giris':
    st.markdown("<h1 class='romantic-title'>Erişim Yetkisi</h1>", unsafe_allow_html=True)
    st.write("<p style='text-align:center; color:white;'>Doğduğun o mucizevi günü gir sevgilim...</p>", unsafe_allow_html=True)
    tarih = st.text_input("", placeholder="GG.AA")
    if st.button("KASAYI AÇ ❤️"):
        if tarih == "30.03":
            st.session_state.asama = 'oyun'
            st.rerun()
        else:
            st.error("Bu tarih kalbimin anahtarı değil.")

# --- AŞAMA 2: OYUN (HATASIZ BÖLÜM) ---
elif st.session_state.asama == 'oyun':
    st.markdown("<h1 class='romantic-title'>Aşkımızın Parıltısı</h1>", unsafe_allow_html=True)
    
    current_p = st.session_state.parilti_seviyesi
    # İşte o düzelen satır kanka:
    bar_renk = f"rgb({current_p*25 + 130}, 215, 0)" 
    
    st.markdown(f"<p style='text-align:center; color:#FFD700; font-size:24px;'>✨ Parıltı Seviyesi: %{current_p*20} ✨</p>", unsafe_allow_html=True)
    st.progress(current_p / 5)

    if st.session_state.soru_no == 1:
        st.markdown("<div class='question-box'>Beni en çok kendine hayran bırakan ne oldu?</div>", unsafe_allow_html=True)
        cevap = st.radio("", ["Gözlerindeki o eşsiz ışıltı.", "Zarafetin ve asalet dolu duruşun.", "Dünyanın en güzel kalbine sahip olman."])
        if st.button("PARILTILARI ARTIR ✨"):
            st.session_state.parilti_seviyesi += 2
            st.session_state.soru_no = 2
            st.rerun()
    elif st.session_state.soru_no == 2:
        st.markdown("<div class='question-box'>Beni kendine nasıl aşık ediyorsun?</div>", unsafe_allow_html=True)
        cevap = st.radio("", ["Sadece sesini duymak yetiyor.", "Karakterindeki güç ve güven.", "Hayallerimizden bahsederkenki gülüşün."])
        if st.button("HAYRANLIĞIMI GÜÇLENDİR ✨"):
            st.session_state.parilti_seviyesi += 2
            st.session_state.soru_no = 3
            st.rerun()
    elif st.session_state.soru_no == 3:
        st.markdown("<div class='question-box'>Senin için yapacağım ilk jest ne olsun?</div>", unsafe_allow_html=True)
        cevap = st.radio("", ["Dev bir gül buketi.", "Sana özel keman dinletisi.", "Sana sımsıkı sarılıp kokunu içime çekmek."])
        if st.button("AŞKIMIZI EBEDİLEŞTİR ✨"):
            st.session_state.parilti_seviyesi += 1
            st.session_state.soru_no = 4
            st.rerun()
    elif st.session_state.soru_no == 4:
        st.balloons()
        st.markdown("<p style='text-align:center; color:white; font-size:22px;'>Asaletine ve kalbine hayranım sevgilim!</p>", unsafe_allow_html=True)
        if st.button("ŞİİRİME ULAŞ 🌹"):
            st.session_state.asama = 'siir'
            st.rerun()

# --- AŞAMA 3: ŞİİR ---
elif st.session_state.asama == 'siir':
    st.markdown("<h1 class='romantic-title'>İyi Ki Doğdun</h1>", unsafe_allow_html=True)
    hedef = datetime(2026, 3, 30)
    fark = hedef - datetime.now()
    if fark.days > 0:
        st.markdown(f"<p style='text-align:center; color:#FFD700;'>Büyük Güne Son {fark.days} Gün!</p>", unsafe_allow_html=True)
    siir = """30 Mart günü doğdu benim güneşim,<br>Dünyada yoktur senin bir benzerin, eşin.<br>Asker yorgun düşse de senin bir gülüşünle,<br>Yeniden canlanır, kalbinde o dev ateşin.<br><br>İyi ki varsın sevgilim..."""
    st.markdown(f"<div class='siir-box'>{siir}</div>", unsafe_allow_html=True)
    if st.button("SON SÜRPRİZ ❤️"):
        st.session_state.asama = 'final'
        st.rerun()

# --- AŞAMA 4: FİNAL ---
elif st.session_state.asama == 'final':
    st.snow()
    st.markdown("<h1 class='romantic-title'>Seni Çok Seviyorum!</h1>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1518709268805-4e9042af9f23?q=80&w=1000", use_container_width=True)
    if st.button("Başa Dön 🔄"):
        st.session_state.asama = 'giris'
        st.session_state.parilti_seviyesi = 0
        st.session_state.soru_no = 1
        st.rerun()