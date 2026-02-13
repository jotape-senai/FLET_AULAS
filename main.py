import flet as ft

def main(page: ft.Page):
    page.title = "Olá Mundo!"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(
        ft.Column(
            controls=[
            ft.Text("Topo da tela"),
            ft.Button(content="Botão do meio"),
            ft.Text("Base da tela")
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.run(main)