import flet as ft

def main(page: ft.Page):
    mensagem=ft.Text("Escolha aopção correta!")
    resposta_correta= "Gato"

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
                    "Qual é o nome desse desenho ? ",
                    size=24,
                    weight="bold"
                ),
                ft.Image(
                    src="imagem/cat.jpg",
                    height=200
                ),
                ft.Row(
                    controls=[
                        ft.Button(
                            content="Cachorro",
                            on_click= verificar_resposta
                        ),
                        ft.Button(
                            content="Gato",
                            on_click= verificar_resposta
                        ),
                        ft.Button(
                            content="Coelho",
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