import flet as ft

def main(page: ft.Page):
    page.bgcolor="#5647de"
    mensagem=ft.Text("Escolha aopção correta!")
    resposta_correta= "mag-7"

    def verificar_resposta(e):
        if e.control.content == resposta_correta:
            mensagem.value ="Parabéns"
        else:
            mensagem.value = "Resposta errada"
        page.update()    
        # page.add(ft.Text(e.control.content))
    page.title = "Game: Adivinha a imagem"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(
        ft.Column(
            controls=[
                ft.Text(
                    "Qual é o nome dessa arma no free fire? ",
                    size=24,
                    weight="bold"
                ),
                ft.Image(
                    src="imagem/mag-7.webp",
                    height=200
                ),
                ft.Row(
                    controls=[
                        ft.Button(
                            content="trogon",
                            on_click= verificar_resposta
                        ),
                        ft.Button(
                            content="mp40",
                            on_click= verificar_resposta
                        ),
                        ft.Button(
                            content="mag-7",
                            on_click= verificar_resposta
                        )
                    ],
                      alignment=ft.MainAxisAlignment.CENTER
                ),
                mensagem
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.run(main)