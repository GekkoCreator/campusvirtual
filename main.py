import flet
from flet import Page, Column, ElevatedButton, Image, Text, alignment, Row, IconButton, Icons, Container
import subprocess
import webbrowser
import os

def main(page: Page):
    page.title = "Generador de Informes"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.window.width = 500
    page.window.height = 500
    icon_path = "icono.ico"
    if not os.path.exists(icon_path):
        print(f"Advertencia: No se encontró el archivo de ícono en la ruta '{icon_path}'.")
    else:
        page.window.icon = os.path.abspath(icon_path)

    def ejecutar_pregrado(e):
        subprocess.Popen(["python", "informes_pregrado.py"], creationflags=subprocess.CREATE_NO_WINDOW)

    def ejecutar_posgrado(e):
        subprocess.Popen(["python", "informes_posgrado.py"], creationflags=subprocess.CREATE_NO_WINDOW)

    def ejecutar_educontinua(e):
        subprocess.Popen(["python", "informes_educontinua.py"], creationflags=subprocess.CREATE_NO_WINDOW)

    def abrir_documento(e):
        if os.path.exists("manual.pdf"):
            subprocess.Popen(["start", "manual.pdf"], shell=True)  # Para Windows
        else:
            print("Archivo 'manual.pdf' no encontrado.")

    def abrir_vinculo(e):
        webbrowser.open("https://outlook.office365.com/mail/")

    def abrir_archivo(e):
        if os.path.exists("campus.pdf"):
            subprocess.Popen(["start", "campus.pdf"], shell=True)  # Para Windows
        else:
            print("Archivo 'campus.pdf' no encontrado.")

    page.add(
        Column(
            alignment="center",
            horizontal_alignment="center",
            spacing=20,
            controls=[
                Column(
                    spacing=0,
                    controls=[
                        Container(height=5, bgcolor="#00dba7", width=600),
                        Container(height=5, bgcolor="#7700ca", width=600),
                        Container(height=5, bgcolor="#06ff3b", width=600),
                    ],
                ),
                Image(src="logo.png", width=300, height=100),
                Text("Generador de Informes Campus Virtual", size=20, weight="bold"),
                Column(
                    alignment="center",
                    horizontal_alignment="center",
                    spacing=10,
                    controls=[
                        Row(
                            alignment="center",
                            controls=[
                                ElevatedButton("Pregrado", on_click=ejecutar_pregrado, bgcolor="#00dba7", color="#FFFFFF"),
                                
                            ],
                        ),
                        Row(
                            alignment="center",
                            controls=[
                                ElevatedButton("Posgrado", on_click=ejecutar_posgrado, bgcolor="#7700ca", color="#FFFFFF"),
                                
                            ],
                        ),
                        Row(
                            alignment="center",
                            controls=[
                                ElevatedButton("Educación Continua", on_click=ejecutar_educontinua, bgcolor="#06ff3b", color="#FFFFFF"),
                                
                            ],
                        ),
                    ],
                ),
                Row(
                    alignment="center",
                    spacing=20,
                    controls=[
                        IconButton(content=Image(src="info.png", width=20, height=20), on_click=abrir_documento),
                        IconButton(content=Image(src="web.png", width=20, height=20), on_click=abrir_vinculo),
                        IconButton(content=Image(src="autor.png", width=20, height=20), on_click=abrir_archivo),
                    ],
                )
            ],
        )
    )

flet.app(target=main)
