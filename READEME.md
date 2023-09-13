1. Langkah dalam mengimplemtasikan checklist step-by-step
    a. Instalasi Django
        - Membuat direktori baru lalu menginisasi dengan git
        - Membuat repositori baru
        - Menghubungkan antara direktori dengan repositori
        - Menginstalasi django pada direktori
    b. Pembuatan aplikasi main
        - Membuat aplikasi main pada direktori melalui terminal dengan Django Startapp
    c. Routing main
        - Mendaftarkan main ke dalam installed_apps pada direktori marcard
    d. Membuat model pada aplikasi
        - Mendaftarkan IntegerField, TextField, dan CharField pada models
    e. Mengaplikasikan views
        - Membuat template html pada aplikasi main lalu memasukan variable bahasa django
        - Pada views.py, mendeklarasikan context pada bahasa django
    f. Routing urls ke main
        - Membuat routing dari urls pada main lalu di-route ke urls pada marcard
    g. Deploy app ke adaptable
        - Membuat app baru pada Adaptable dengan source repository github
        - Melakukan deployment pada aplikasi

2. Bagan berada pada berkas "bagan.jpg", alur pada bagan ini adalah client melakukan request aplikasi yang kemudian dilempar ke urls.py pada direktori marcard, urls.py ini akan menghubungkan ke urls.py pada aplikasi main yang memiliki fungsi untuk memunculkan konten. Kita dilakukan show_main pada urls.py, maka akan dilakukan pengambilan data dari views.py yang kemudian dimasukkan ke dalam main.html pada direktori template. Selain itu, views.py juga menginisiasi bentuk dari field pada html melalui models.py

3. Dengan adanya virtual environment makan terdapat beberapa manfaat bagi pemrogram, yaitu :
    1. Mengisolasi lingkungan direktori, dengan kata lain membantu menghindari konflik dan memastikan kestabilan dari proyek
    2. Mamudahkan pembaruan, jika adanya ingin diperbaharui dari proyek maka pemrogram tidak perlu khawatir menggangu yang lain
    3. Mudah untuk menguji, perubahan yang dilakukan dilakam virtual environment akan lebih mudah dilakukan

4. Ketiga model memiliki perbedaan sebagai berikut
    1. MVC atau Model-View-Controller: Dalam MVC, View dan Controller biasanya lebih erat terkait, yang berarti bahwa mereka sering berinteraksi secara langsung. Model memiliki pengetahuan tentang Controller tetapi tidak tentang View.
    2. MVT atau Model-View-Template : Pada MVT peran yang biasanya dipegang oleh Controller dalam MVC digantikan oleh Template. MVT adalah pola yang lebih umumnya terkait dengan kerangka kerja seperti Django yang digunakan untuk pengembangan web.
    3. MVVM atau Model-View-ViewModel : MVVM akan melakukan ViewModel yang memiliki peran lebih kuat dalam mengelola tampilan daripada Controller dalam MVC. ViewModel mengikat data dari Model ke tampilan secara deklaratif, yang memungkinkan perubahan otomatis dalam tampilan saat data Model berubah.
