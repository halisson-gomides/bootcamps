from nicegui import ui


@ui.page('/')
def principal()->None:
    ui.query('body').classes('bg-amber-100')
    with ui.row().classes('items-center'):
        ui.image('img/logo_farol_na_quebrada-removebg.png').classes('w-24')
        ui.label("Bem-vindo ao Farol na Quebrada").classes("text-xl font-medium text-wrap text-stone-500")

    with ui.left_drawer().classes('bg-orange-500') as left_drawer:
        ui.label('Menu lateral')

    # with ui.footer(value=False) as footer:
    with ui.footer(value=False).classes('bg-dark') as footer:
        with ui.splitter().classes('w-1/3') as splitter:
            with splitter.before:
                ui.label('© Todos os direitos reservados.')
            with splitter.after:
                ui.link("Contato", 'mailto:farol@naquebrada.com.br').classes('text-white px-3')

    with ui.page_sticky(position='bottom-right', x_offset=20, y_offset=20):
        ui.button(on_click=footer.toggle, icon='contact_support', color='dark').props('fab')

ui.run(title="Minha primeira pagina web em python", language='pt-BR', favicon='img/logo_farol_na_quebrada.jpg')