DICOM Anonimizáló
Egy Python és Tkinter alapú alkalmazás, amellyel egyszerre több DICOM fájlt vagy egy teljes mappát is anonimizálhatsz. A program a pydicom könyvtárra épül, és automatikusan eltávolítja vagy átírja a személyes adatokat (pl. PatientName, PatientID, PatientBirthDate), így megfelel a kutatási és diagnosztikai célú adatvédelem elvárásainak.

Funkciók
Több fájl / mappa támogatása: Kiválaszthatsz egyszerre több fájlt vagy akár egy egész mappát.

Felhasználóbarát felület: Egy gombnyomással anonimizálhatsz, nincs szükség parancssori ismeretekre.

Önálló futtatható fájl: Készíthetsz .exe verziót, amelyhez nem kell külön Python környezet.

Gyors és megbízható feldolgozás: A pydicomnak köszönhetően nagyobb adathalmazokkal is könnyen boldogul.

Használati útmutató
Indítás (Python környezetben):

Telepítsd a függőségeket:

bash
Másolás
pip install pydicom
Futtasd a programot:

bash
Másolás
python dicom_anonymizer_gui_multi.py
Megnyílik egy Tkinter ablak, ahol kiválaszthatod a bemeneti fájlokat vagy mappát, majd a kimeneti mappát, és elindíthatod az anonimizálást.

Önálló .exe fájl használata (telepítés nélkül):

Töltsd le a kész .exe-t a „Releases” lapról (vagy ahonnan a kollégád megosztotta).

Futtasd a .exe-t: a program ugyanúgy egy felhasználóbarát ablakban nyílik meg.

Válaszd ki a bemeneti fájlokat vagy mappát, majd a kimeneti mappát, és kattints az „Anonimizálás indítása” gombra.

Feldolgozott fájlok megtalálása:

Az anonimizált fájlok a megadott kimeneti mappába kerülnek, ugyanolyan névvel, mint az eredeti fájlok.


