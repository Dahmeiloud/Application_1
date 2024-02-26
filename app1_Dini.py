# اتدعتء المكتبات 
from pywebio import *
from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from pywebio import config
css = """
@import url('https://fonts.googleapis.com/css2?family=Amiri:ital@0;1&family=Changa:wght@200&display=swap');
#h3{
font-family: 'Amiri', serif;
font-family: 'Changa', sans-serif;
}
#para{
font-family: 'Amiri', serif;
font-family: 'Changa', sans-serif;
color: grey;
}
#y{
font-family: 'Amiri', serif;
font-family: 'Changa', sans-serif;
width:40%;
}
"""
@config(css_style=css)
def app():
    put_image('data:image/jpeg;base64,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', width='900px' ,height='200px' )
    put_html("""
        <h3 id='h3'>تطبيق القرآن الكريم <h3/>
        <p id='para'>اهلا وسهلا بيكم في تطبيقنا الجديد  لحفظ القرآن الكريم</p>
        <ul>
            <li>حفظ القرآن الكريم</li>
             <li>احديث نبوية </li>
             <li>تفسير القرآن الكريم </li>     
        </ul>
        <details id='y'> 
            <summary>  سورة الفاتحة   </summary>
             <p>  سورة الفاتحة بصوت ابراهيم الدوسري </p>
             <audio controls>
                <source src="https://server10.mp3quran.net/ibrahim_dosri/Rewayat-Warsh-A-n-Nafi/001.mp3" type="audio/mp3">
             </audio>
             
        </details>
        <details id='y'>
             <summary> سورة الكهف </summary>
             <p>سورة الكهف بصوت ياسر الدوسري   </p>
             <audio controls>
                <source src="https://server11.mp3quran.net/yasser/018.mp3" type="audio/mp3">
             </audio>
        </details>
         <details id='y'>
            <summary> سورة الإسراء </summary>
             <p> سورة الإسراء بصوت إسلام صبحي - حفص عن عاصم   </p>
             <audio controls>
                <source src="https://server14.mp3quran.net/islam/Rewayat-Hafs-A-n-Assem/017.mp3" type="audio/mp3">
             </audio>
        </details>    
        <hr>
        <p>جميع الحقوق محفوظة للمطور @ ميلود الداه</p>
    """).style('direction:rtl; text-align: right;')


start_server(app , port=34345 , debug=True)


# ======================================================

# while True:
#     time = datetime.datatime.now()
#     now = timo.strftime("%H:%M:%S")
#     if now == time:
#         medcine = AudioSegment.from_mp3('sounds/')
#         play(medcine)
#     if now > time:
#         break

# ======================================================