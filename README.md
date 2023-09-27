1. TUGAS 2

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

2. TUGAS 3 
    1.  Perbedaan POST dan GET

        POST dalam django mememiliki pengerti pengiriman data. POST akan digunakan untuk mengirimkan data ke server, data yang dikirimkan akan berbentuk permintaan HTTP. POST cocok untuk mengirimkan data pribadi atau rahasia yang berkonten sensitif seperti kata sandi atau lainnya.

        GET merupakan perintah untuk mengambil data dari server. Data tersebut dikirimkan melalui URL sebagai bentuk dari query string yang nantinya dapat terlihat di browser. Cocok untuk mengambil tautan bebas yang dapat dibagikan.

    2. Perbedaan dari HTML, XML, dan JSON

        HTML (Hypertext Markup Language) :
        -> Merupakan bahasa yang digunakan untuk menampilkan konten dari web, tidak dirancang untuk pertukaran data
        -> Bahasa ini bertujuan untuk menentukan tampilan dan struktur dari web
        -> Terdapat tag dan atribut untuk mendeklarasikan elemen yang akan dirancang seperti teks, gambar, tautan, dan lainnya

        XML (Extensible Markup Language) :
        -> Merupakan bahasa yang digunakan untuk mendefinisikan struktur data
        -> Dapat digunakan untuk pertukaran data antara sistem dan aplikasi
        -> Secara sintaks, bentuk xml lebih rumit dalam penggunaannya

        JSON (JavaScript Object Notation) :
        -> Merupakan bahasa yang digunakan untuk pertukaran data ringan  berbasis teks
        -> Biasa digunakan untuk pertukaran data antara server dan klien pada aplikasi
        -> Lebih cocok untuk data yang memiliki struktur mirip dengan objek dalam pemrograman

    3. Mengapa JSON sering diguankan untuk pertukaran data

        -> Format penulisan dan sintaks yang mudah dibaca.
        -> Mendukung struktur data, JSON mendukung berbagai struktur data, termasuk objek dan array sehingga memungkinkan pemrogram untuk menggambarkan data dalam format yang paling sesuai dengan kebutuhan aplikasi
        -> Mudah diintegrasikan dengan JavaScript, JSON sangat kompatibel dengan JavaScript yang merupakan bahasa pemrograman yang dominan dalam pengembangan aplikasi. Data JSON dapat dengan mudah diurai menjadi objek JavaScript dan sebaliknya sehingga membuat interaksi antara klien dan server lebih mudah

    4. --Checklist--
        1. Membuat input form
            Untuk membuat sebuah form pada aplikasi yang diinginkan, dilakukan inisiasi pembuatan html dasar dalam base.html.

            Selanjutnya diperlukan pembuatan struktur form pada aplikasi (main) dalam bentuk berkas forms.py dengan isi fields dari form yang diinginkan

            Pada views.py diperlukan inisiasi pembuatan produk baru sehingga diperlukan fungsi pembuatan produk.

            Selain inisiasi pada views.py, perlu membuat pula html dari create_products dengan isi model html untuk add new product.

            Lalu, memasukan bentuk dari form (table) dengan masukan dan keperluan dari form seperti nama, harga, deskripsi, dan tanggal (perlu disesuaikan pula dengan models yang telah kita buat).

        2. Menambahkan fungsi views
            Agar data dapat dikembalikan dalam bentuk HTML, XML, JSON, XML by ID, dan JSON by ID perlu dilakukan deklarasi pada views.py

            HTML telah diinsiasi pada views ketika pembuatan show_main,

            XML perlu diinsiasi dengan pada views.py dengan fungsi dengan return yang memmiliki serializer ke "xml" agar objek dapat ditranslate ke dalam XML, contoh kode

            def show_xml(request):
                data = Product.objects.all()
                return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

            JSON perlu diinisiasi pada views.py mirip dengan XML. return juga perlu memiliki serializers ke "json",

            Untuk membuat XML by id dan JSON by id perlu membuat sebuah fungsi dengan parameter tambahan yaitu id dimana ketika dimasukkan id maka akan melempar data pada id tersebut saja, contoh kode

            def show_xml_by_id(request, id):
                data = Product.objects.filter(pk=id)
                return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

            dan

            def show_json_by_id(request, id):
                data = Product.objects.filter(pk=id)
                return HttpResponse(serializers.serialize("json", data), content_type="application/json")

        3. Perlu diingat, urls perlu ditambahkan sehingga fungsi-fungsi diatas dapat dijalankan. Bentuk penambahan pada akhir urls.py di main akan berbentuk sebagai berikut

        ---
        from django.urls import path
        from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id 
        app_name = 'main'

        urlpatterns = [
            path('', show_main, name='show_main'),
            path('create-product', create_product, name='create_product'),
            path('xml/', show_xml, name='show_xml'), 
            path('json/', show_json, name='show_json'), 
            path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
            path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
        ]
        ---

    5. Hasil screenshot postman
        -> HTML : pada berkas posthtml.jpg
        -> XML : pada berkas postxml.jpg
        -> JSON : pada berkas postjson.jpg
        -> XML by ID : pada berkas postxmlid.jpg
        -> JSON by ID : pada berkas postjsonid.jpg

3. Tugas 4
    1. Apa itu Django UserCreationForm?
        Django UserCreationForm adalah sebuah fork bawaan atau built-in dari framewrok web Python yaitu Django. Form ini dibuat agar ketika pemrogram membuat fitur pembuatan pengguna akan lebih mudah jika menggunakan authentication pengguna dari Django. 

        UserCreationForm mengandung beberapa fiels yang umumnya diperlukan yaitu username, password, dan password confirmation. Form ini juga memastikan bahwa username unik dan password kuat.

        Kelebihan : Praktis untuk digunakan karena telah menyediakan data umum yang diperlukan sehingga menghemat waktu pemgrogram untuk membuat form.

        Kekurangan : Karena berbentuk umum, form ini hanya menyediakan data dan tampilan standar saja. Form ini juga tidak melakukan cek terhadap email pengguna sehingga tidak dapat dilihat apakah email pengguna unik. Tidak pula dapat dilakukan autentikasi dua-kali seperti 2-step Verification.

    2. Perbedaan antara Autentikasi dan Otorisasi

        -> Autentikasi :
        Merupakan sebuah proses memverifikasi indentitas dari pengguna. Pada Django, informasi yang digunakan untuk melakukan verifikasi autentikasi antaralain adalah username dan password.

        -> Otorisasi : 
        Merupaka proses menentukan akses pengguna yang teratentikasi terhadap aplikasi. Pengguna akan dapat mengakses fitur sesuai dengan role mereka. Pada Django, Otorisasi memungkinkan pemrogram untuk mengatur izin akses dari pengguna terhadap fitur-fitur aplikasi berdasarkan role mereka. 

    3. Apa itu cookies dalam konteks aplikasi web

        Secara singkat, Cookies adalah cara bagi aplikasi untuk menyimpan sedikit informasi di komputer pengguna, biasanya dalam browser web. Hal ini berguna untuk menyimpan data sementara seperti pengaturan atau informasi login saat penggunan menggunakan situs web.

        Dalam Django, cookies digunakan untuk mengelola sesi pengguna, yang merupakan cara aplikasi web menyimpan informasi yang berhubungan dengan pengguna selama mereka berinteraksi dengan situs web tersebut.

        Beberapa cara Django menggunakan Cookies :
        1. Konfigurasi terhadap sesi pengguna (Konfirmasi penggunaan cookies)
        2. Menyimpan data pada sesi
        3. Mengakses data pada sesi
        4. Menghapus data
    
    4. Tentunya terdapat beberapa masalah yang dapat muncul dengan penggunaan Cookies
