# -*- coding: utf-8 -*-
"""projekt_9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cFdliP4F_ARuZCTsEHutLjUPEMnTQkXj
"""

import cv2
import numpy as np
from google.colab import files
from google.colab.patches import cv2_imshow

video = cv2.VideoCapture("droga.mkv")

while video.isOpened():
    ret, frame = video.read()

    if not ret:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2_imshow(gray_frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

while video.isOpened():
    ret, frame = video.read()

    if not ret:
        break

    # Zastosowanie rozmycia Gaussa na klatce
    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)

    # Wyświetlenie klatki oryginalnej i rozmytej
    cv2_imshow(blurred_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

import matplotlib.pyplot as plt
while video.isOpened():
    ret, frame = video.read()

    if not ret:
        break

    # Konwersja klatki na odcienie szarości
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Zastosowanie algorytmu Canny'ego do wykrywania konturów
    edges = cv2.Canny(gray_frame, 100, 200)

    # Wyświetlenie klatki z wykrytymi konturami
    plt.subplot(1, 2, 2)
    plt.imshow(edges, cmap='gray')
    plt.title("Edges")
    plt.axis("off")

    plt.show()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

# Ścieżka do filmu
video_path = 'droga.mkv'

# Otwieranie filmu
video = cv2.VideoCapture(video_path)

# Sprawdzenie, czy film jest otwarty
if not video.isOpened():
    print("Nie można otworzyć pliku wideo")
    exit()

# Pętla po klatkach wideo
while True:
    # Odczytanie klatki
    ret, frame = video.read()

    # Sprawdzenie, czy odczyt klatki się powiódł
    if not ret:
        break

    # Konwersja klatki na odcienie szarości
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Zastosowanie algorytmu Canny'ego do wykrywania krawędzi
    edges = cv2.Canny(gray_frame, 50, 150)

    # Zastosowanie transformacji Hougha dla detekcji linii prostych
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=50, minLineLength=50, maxLineGap=10)

    # Rysowanie wykrytych linii na klatce oryginalnej
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)

    # Wyświetlenie klatki oryginalnej z wykrytymi liniami
    cv2_imshow(frame)

    # Przerwanie pętli, jeśli naciśnięto klawisz 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Zamknięcie wideo i zniszczenie okna wyświetlania
video.release()
cv2.destroyAllWindows()

import matplotlib.pyplot as plt
video_path = "dorga.mkv"
video = cv2.VideoCapture(video_path)

# Pusta lista do przechowywania klatek jako obrazów
frames = []

# Pętla po klatkach w filmie
while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break

    # Konwersja klatki z BGR do RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Dodanie klatki do listy
    frames.append(frame_rgb)

video.release()

# Wyświetlenie sekwencji klatek jako animacji
fig = plt.figure(figsize=(8, 6))

for frame in frames:
    plt.imshow(frame)
    plt.axis('off')
    plt.show()

# Ścieżka do filmu
video_path = 'droga.mkv'

# Otwieranie filmu
video = cv2.VideoCapture(video_path)

# Sprawdzenie, czy film jest otwarty
if not video.isOpened():
    print("Nie można otworzyć pliku wideo")
    exit()

# Pobranie rozmiarów klatek wideo
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Definicja parametrów tekstu
text = "Zofia"
font_scale = 1
thickness = 2
font = cv2.FONT_HERSHEY_SIMPLEX

# Pętla po klatkach wideo
while True:
    # Odczytanie klatki
    ret, frame = video.read()

    # Sprawdzenie, czy odczyt klatki się powiódł
    if not ret:
        break

    # Dodanie tekstu z Twoim imieniem w prawym dolnym rogu klatki
    org = (width - 200, height - 50)
    cv2.putText(frame, text, org, font, font_scale, (0, 0, 255), thickness, cv2.LINE_AA)

    # Wyświetlenie klatki z dodanym tekstem
    cv2_imshow(frame)

    # Przerwanie pętli, jeśli naciśnięto klawisz 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Zamknięcie wideo i zniszczenie okna wyświetlania
video.release()
cv2.destroyAllWindows()