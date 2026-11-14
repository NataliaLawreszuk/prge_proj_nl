FROM python:3.11-slim
#wybór obrazu bazowego w tym przypadku python w wersji 3.11-slim

LABEL authors='Natalia'

RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*
#Zaktualizuj listę pakietów, zainstaluj narzędzia do kompilacji, a następnie usuń zbędne pliki.
#RUN – wykonuje polecenie podczas budowania obrazu.
#apt-get update – aktualizuje listę dostępnych pakietów systemowych. Nie aktualizuje jeszcze samych programów.
#&& – wykonaj następne polecenie tylko wtedy, gdy poprzednie zakończyło się sukcesem.
#apt-get install -y build-essential – instaluje zestaw narzędzi potrzebnych między innymi do kompilacji programów. Parametr -y automatycznie potwierdza instalację.
#rm -rf /var/lib/apt/lists/* – usuwa pobrane listy pakietów, żeby ograniczyć rozmiar obrazu.

WORKDIR /app
#ustawienie katalogu roboczego na app (gdyby app nie istniał zostałby utworzony)

COPY ./docker/fastapi/requirements.txt /app/requirements.txt
#kopiuje pliki podczas budowania oobrazu z fastapi/requirements.txt do app/requirements.txt
#po skopiowaniu plików do obrazu zmiana pliku na Macu nie zmienia automatycznie jego kopii w obrazie.

#żeby pliki w obrazie były automatycznie updatowane uzywa sie bind mount
#zamiast tworzyć niezależną kopię plików,
#Docker umożliwia kontenerowi korzystanie z katalogu znajdującego się na Twoim komputerze.
#przykładem takiego rozwiazania jest np. volumes w docker compose

RUN pip install --no-cache-dir -r requirements.txt
#pip – menedżer pakietów Pythona.
#--no-cache-dir – nie zapisuj pamięci podręcznej pobranych pakietów.
#-r requirements.txt – odczytaj listę pakietów z pliku.


COPY config/fastapi /app

# uvicorn app.main:app --host 0.0.0.0 --port 10000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000"]
#CMD	Określa domyślne polecenie startowe kontenera, może zostać nadpisane przez konfigurację Docker Compose
#uvicorn	Serwer, który uruchamia aplikację FastAPI
#app.main:app	Wskazuje aplikację Python, którą Uvicorn ma obsługiwać
#--host	Parametr określający adres nasłuchiwania
#0.0.0.0	Nasłuchiwanie na wszystkich interfejsach sieciowych kontenera
#--port	Parametr określający port
#10000	Port, na którym Uvicorn nasłuchuje wewnątrz kontenera

