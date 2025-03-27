# DICOM Anonimizáló

Ez a projekt egy **Python** és **Tkinter** alapú DICOM anonimizáló alkalmazást tartalmaz, amellyel akár több fájlt vagy egy teljes mappát is egyszerre anonimizálhatsz. A [pydicom](https://pydicom.github.io/) könyvtár segítségével a program gyorsan és biztonságosan eltávolítja a személyes adatokat (például `PatientName`, `PatientID`, `PatientBirthDate`) a DICOM fájlokból.

---

## Fő funkciók

- **Több fájl / mappa kiválasztása:**  
  Kényelmesen beolvashatsz több DICOM fájlt, vagy egy egész mappát.
  
- **Anonimizálási beállítások:**  
  Alapértelmezés szerint a betegadatok (név, ID, születési dátum) törlésre vagy „Anonymous” értékre módosításra kerülnek.
  
- **Felhasználóbarát felület:**  
  Egyszerű gombokkal (Tallózás, Anonimizálás indítása) vezérelhető.
  
- **Önálló futtatható fájl (.exe):**  
  A feltöltött .exe fájl segítségével a program futtatható Python környezet nélkül, közvetlenül Windows rendszeren.

---

## Telepítés és használat (Python környezetben)

1. **Függőségek telepítése:**

    ```bash
    pip install pydicom
    ```

2. **Program indítása:**

    ```bash
    python dicom_anonymizer_gui.py
    ```

    Ekkor megnyílik a Tkinter alapú ablak, ahol:
    
    - **Fájlok kiválasztása:** Válaszd ki a feldolgozandó DICOM fájlokat vagy egy teljes mappát.
    - **Kimeneti mappa megadása:** Add meg azt a mappát, ahová az anonimizált fájlok kerülnek.
    - **Anonimizálás indítása:** Kattints az "Anonimizálás indítása" gombra a feldolgozás elindításához.

---

## Használat az önálló .exe fájl esetén

A feltöltött .exe fájl egy önálló, Windows rendszeren futtatható verzió, amely nem igényel külön Python telepítést:

1. **Futtatás:**  
   Dupla kattintással indítsd el a `.exe` fájlt. A program ugyanazt a felhasználóbarát Tkinter felületet jeleníti meg.
   
2. **Használat:**  
   - **Fájlok kiválasztása:** Használd a "Tallózás" gombot a feldolgozandó DICOM fájlok vagy egy teljes mappa kiválasztásához.
   - **Kimeneti mappa megadása:** Válaszd ki azt a mappát, ahová az anonimizált fájlokat szeretnéd menteni.
   - **Anonimizálás indítása:** Kattints az "Anonimizálás indítása" gombra, és a program automatikusan feldolgozza a fájlokat.
   
3. **Eredmény:**  
   Az anonimizált fájlok a megadott kimeneti mappában jelennek meg, az eredeti fájlnevekkel.

---

## Önálló futtatható (.exe) készítése (fejlesztőknek)

1. **PyInstaller telepítése:**

    ```bash
    pip install pyinstaller
    ```

2. **Futtatható fájl létrehozása:**

    ```bash
    pyinstaller --onefile --windowed dicom_anonymizer_gui_multi.py
    ```

    A sikeres futtatás után a `dist` mappában megjelenik a `.exe` állomány, amely önállóan futtatható.

---

## Hibák és kérdések

- **Nem találja a DICOM metaadatokat:**  
  Győződj meg róla, hogy a fájl valóban DICOM formátumú.
  
- **Futtatás közben hibaüzenet:**  
  Ellenőrizd, hogy a `pydicom` telepítve van, és a Python verziód 3.x.
  
- **További kérdések:**  
  Ha bármilyen hibát vagy javaslatot találsz, kérjük, nyiss egy Issue-t a repóban.

---

## Hozzájárulás

- **Fork & Pull Request:**  
  Ha módosítanál a kódban, kérjük, forkold a repót, majd küldj egy Pull Requestet.
  
- **Issue:**  
  Hibák és javaslatok esetén nyiss egy Issue-t.

---

## Licenc

Ez a projekt az [MIT licenc](LICENSE) alatt érhető el, így szabadon felhasználható és módosítható.

---


