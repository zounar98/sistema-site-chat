# App de mensagem
# BOTÃO INICIAR CHAT
# POPUP PARA ENTRAR NO CHAT
# AÇÃO AO ENTRAR NO CHAT:
    # MENSAGEM ONLINE
    # CAMPO E BOTÃO ENVIAR MENSAGEM
# EXIBIÇÃO DE MENSAGENS
# NOME: TEXTO DA MENSAGEM

import flet as ft 

def main(pagina):
    texto = ft.Text("Hashzap")

    chat = ft.Column()

    nome_usuario = ft.TextField(label="Apelido")

    def enviar_mensagem_tunel(mensagem):
        tipo = mensagem["tipo"]
        if tipo == "mensagem":
            texto_mensagem = mensagem["texto"]
            usuario_mensagem = mensagem["usuario"]
        # adicionar a mensagem ao chat
            chat.controls.append(ft.Text(f"{usuario_mensagem}: {texto_mensagem}"))
        else:
            usuario_mensagem = mensagem["usuario"]
            chat.controls.append(ft.Text(f"{usuario_mensagem}: entrou no chat",
                                         size=12, italic=True, color=ft.colors.ORANGE_500))

        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        pagina.pubsub.send_all({"texto": campo_mensagem.value, "usuario": nome_usuario.value,
                                "tipo": "mensagem"})
        # limpar campo de mensagem
        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem = ft.TextField(label="Digite uma mensagem", on_submit=enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    def entrar_popup(evento):
        pagina.pubsub.send_all({"usuario": nome_usuario.value, "tipo": "entrada"})
        # adicionar chat
        pagina.add(chat)
        # fechar popup
        popup.open = False
        # remover botão iniciar chat
        pagina.remove(botao_iniciar)
        pagina.remove(texto)
        # criar campo de mensagem de usuário
        # criar botão de enviar mensagem do usuário
        pagina.add(ft.Row(
            [campo_mensagem, botao_enviar_mensagem]
            ))
        pagina.update()

    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Bem vindo ao Hashzap"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_popup)]
        )

    def entrar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()


    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=entrar_chat) 

    pagina.add(texto)
    pagina.add(botao_iniciar)

   
ft.app(target=main, view=ft.WEB_BROWSER) # view=ft.WEB_BROWSER