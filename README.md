# Analisis Listing Airbnb Bangkok

## Pembuka

Daegu adalah kota yang menjelma menjadi daerah aglomerasi dengan beberapa kota satelit yang mengelilinginya dan berada di daerah Yeongnam, Korea Selatan, dan tepatnya berada di sekitaran provinsi Gyeongsang Utara, sebuah provinsi hasil pemekaran dari provinsi Gyeongsang yang telah lama berdiri sejak Kekaisaraan Korea pada masa wangsa Joseon yang menduduki seluruh Semenanjung Korea, jauh sebelum terbelah menjadi dua pada saat ini. Meskipun kota ini hanya menampung 4,84% dari total populasi Korea Selatan, dengan luasan kota hanya mencapai 1.500 kmkm<sup>2</sup>, kepadatan penduduk kota ini mencapai 1.600 jiwa per km<sup>2</sup>, hal akomodasi alias papan dalam tiga kebutuhan utama manusia (sandang, papan, dan pangan) menjadi tantangan vital bagi kota ini dan penduduknya. Sehingga, kebutuhan akomodasi yang diejawantahkan dalam bentuk hunian berupa apartemen ini menjadi kebutuhan penting bagi masyarakatnya, dan analisis serta pemodelan valuasi bangunan ini menjadi hal yang menarik untuk ditelisik. Valuasi yang mudah dalam kasus ini ialah harga apartemen yang ditawarkan. Dengan variasi harga apartemen yang cukup beragam, penentuan harga jual hunian dengan harga sepantasnya dan sesuai dengan harga pasaran di Kota Daegu menjadi hal yang teramat penting.

## Data dan *Library*

Proses pengerjaan analisis ini menggunakan data yang disematkan pada repositori ini, dengan data awal berupa *file* berekstensi CSV dengan nama `data_daegu_apartment.csv` dan dengan penyesuaian analisis dihasilkan set data dalam bentuk CSV lain yang bernama `data_daegu_apartment_cleaned.csv`. Lalu, dengan menggunakan bahasa pemrograman Python sebagai penunjang analisis, pada kesempatan ini disokong juga dengan beberapa *library* terkait seperti Pandas, Numpy, Seaborn, Scipy, Warnings, Matplotlib, Time, Sklearn, Streamlit, dan SHAP.

## Tahapan Pengerjaan

Untuk pengerjaan analisis ini, secara garis besar proses pengerjaan bisa dibagi menjadi lima proses, yakni:

1. Peninjuan konteks dan pemetikan permasalahan dan solusi yang bersesuaian dari kasus yang dihadapi.
2. Pembersihan Data dengan identifikasi data pra-pembersihan, identifikasi data absah pada set data dan pembersihannya, dan identifikasi data pasca-pembersihan.
3. Pemodelan dengan menguji model dengan 12 metode berbeda yang dites pada saat _fitting_ model, lalu didapatkan 4 model yang dites untuk prediksi. Setelah itu, dipilihlah 3 model untuk disetel lebih lanjut sebelum dites kembali untuk menentukan model yang dipilih.
4. Penyimpanan model dalam `plckled file` dan pemanfaataannya dengan aplikasi berbasis Streamlit.
5. Inferensi kesimpulan yang bisa dipetik dari pemodelan dan saran terkait yang bisa menunjang model ke depannya.

## Penutup

Dengan analisis yang disematkan pada file berekstensi .ipynb yang bernama `data-analysis-and-modelling.ipynb`, didapatkan beberapa kesimpulan sebagai berikut:

* Model yang terpilih yakni _XG Boosting_ dengan penyetelan pada beberapa parameter.
* Model ini mempunyai besaran MAPE sebesar 20,20 % dan tergolong sebagai model dengan kemampuan _forecasting_ yang cukup _reasonable_.
* Dari pemodelan, didapatkan fakta bahwa variabel tipe _hallway_ berupa _terraced_, tahun didirikannya apartemen, dan jumlah slot pada lahan parkir menjadi variabel yang lebih berpengaruh pada model.