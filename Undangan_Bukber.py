import streamlit as st
import base64

# --- FUNGSI UNTUK MENAMBAHKAN BACKGROUND (CSS CUSTOM) ---
# Sebagai mahasiswa TI, ini adalah trik 'curang' tapi efektif:
# Mengubah gambar lokal menjadi base64 string dan menyuntikkannya sebagai CSS.
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string.decode()}");
            background-attachment: fixed;
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }}
        
        /* --- PENYESUAIAN WARNA TEKS AGAR TERBACA --- */
        /* Mengubah semua teks utama (p) dan markdown menjadi putih */
        .stApp, h1, h2, h3, h4, h5, h6, .stMarkdown p {{
            color: #ffffff !important;
        }}
        
        /* Mengubah warna teks judul kolom dan teks detail di dalamnya */
        div[data-testid="stForm"] label, .stMarkdown label {{
            color: #ffffff !important;
        }}

        /* Mengubah warna teks di dalam tombol Maps (Link Button) */
        button[data-testid="baseButton-primary"] {{
            border: 2px solid #ffffff !important;
        }}
        
        /* Mengubah warna teks di dalam formulir agar tetap gelap */
        input, textarea, .stSelectbox, .stNumberInput, .stSlider {{
            color: #ffffff !important;
        }}
        
        /* Mengubah warna latar belakang formulir input agar lebih terlihat */
        input, textarea {{
            background-color: rgba(255, 255, 255, 0.9) !important;
            border-radius: 5px;
        }}
        
        /* Menyesuaikan label radio button (Hadir/Tidak Hadir) agar teksnya putih */
        .stRadio label span p {{
            color: #ffffff !important;
        }}
        
        /* Menyesuaikan warna divider */
        .stMarkdown hr {{
            border-top: 2px solid #000000;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

# --- MULAI SCRIPT UTAMA ---

# Masukkan nama file gambar kamu (harus satu folder dengan script ini)
image_filename = "images.png"

# Konfigurasi halaman (Tab browser) - HARUS PERTAMA KALI DIPANGGIL
st.set_page_config(page_title="UNDANGAN BUKA BERSAMA", page_icon="🏡", layout="centered")

# Panggil fungsi untuk menambahkan background
try:
    add_bg_from_local(image_filename)
except FileNotFoundError:
    st.error(f"Error: File gambar '{image_filename}' tidak ditemukan di folder yang sama dengan script. Pastikan nama file sama persis.")
    # Fallback ke warna latar gelap jika gambar tidak ditemukan
    st.markdown(
        """
        <style>
        .stApp {{
            background-color: #0a1033;
        }}
        .stApp, h1, h2, h3, h4, h5, h6, .stMarkdown p {{
            color: #ffffff !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# --- SISA SCRIPT ASLI KAMU (DENGAN PENYESUAIAN KECIL PADA CSS DI ATAS) ---

# Bagian Header Undangan
st.title("🏡 UNDANGAN BUKA BERSAMA")
st.subheader("KHUSUS UNTUK TEAM CURUG! 💻🚀")

st.markdown("---")

# Pesan Pembuka
st.write("""
Assalamu’alaikum Warahmatullahi Wabarakatuh / Selamat Siang.

Dalam indahnya bulan suci Ramadan yang penuh berkah ini, kami ingin mengundang rekan-rekan sekalian untuk hadir dalam acara Buka Puasa Bersama. Acara ini diadakan untuk mempererat tali persaudaraan dan kebersamaan di antara kita.

Kehadiran rekan-rekan akan sangat berarti. Mohon kesediaannya untuk mengisi konfirmasi kehadiran pada tautan undangan berikut.""")

# Detail Acara menggunakan kolom agar rapi
st.subheader("📌 Detail Waktu Acara")
col1, col2 = st.columns(2)

with col1:
    st.markdown("**📅 Tanggal :**")
    st.write("Minggu, 8 Maret 2026")
    
    st.markdown("**⏰ Waktu :**")
    st.write("16.30 WIB - Selesai ")

with col2:
    st.markdown("**📍 Lokasi :**")
    st.write("[RUMAH ORANG TUA IBU SELVI KUSTIANINGSIH]")
    
    st.markdown("**👗 Dresscode :**")
    st.write("Bebas, Sopan, dan Keren")

st.markdown("---")

# Bagian Peta / Link Google Maps
st.subheader("🗺️ Lokasi")
st.write("Biar nggak nyasar atau kena MACET, langsung saja klik tombol di bawah untuk mendapatkan rute ke lokasi:")

# Memasukkan link maps yang kamu berikan menggunakan link_button Streamlit
maps_url = "https://www.google.com/maps/place/Gg.+Rw.+Bebek+I+30,+RW.011,+Kota+Baru,+Kec.+Bekasi+Bar.,+Kota+Bks,+Jawa+Barat+17133/@-6.2184339,106.9624242,19z/data=!3m1!4b1!4m6!3m5!1s0x2e698c7c2fc3798f:0xa9e2433a30bbb9f6!8m2!3d-6.2184339!4d106.9630679!16s%2Fg%2F11g62k67dw?entry=ttu&g_ep=EgoyMDI2MDMwMi4wIKXMDSoASAFQAw%3D%3D"
st.link_button("📍 Buka Rute di Google Maps", maps_url, use_container_width=True)

st.markdown("---")

# Form RSVP interaktif
st.subheader("📩 (Konfirmasi Kehadiran)")
st.write("Tolong isi form di bawah ini ya!")

with st.form("rsvp_form"):
    nama = st.text_input("Nama Lengkap :")
    kehadiran = st.radio("Status Kehadiran :", ("Hadir", "Tidak Hadir"))
    pesan = st.text_area("Pesan ")
    
    submit_button = st.form_submit_button(label="Kirim Konfirmasi 🚀")
    
    # Logika setelah tombol ditekan
    if submit_button:
        if nama.strip() == "":
            st.error("Error: Variabel 'Nama' tidak boleh Null/kosong! Silakan isi dulu ya.")
        else:
            if "Tidak" in kehadiran:
                st.warning(f"Yah sayang sekali {nama} belum bisa ikut. *System* mencatat alasanmu. Semoga bisa ikut di *event* selanjutnya!")
            else:
                st.success(f"Data {nama} berhasil di-*compile*! Ditunggu kedatangannya ya. 🎉")