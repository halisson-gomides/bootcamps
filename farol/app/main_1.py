from nicegui import ui


@ui.page('/')
def principal()->None:
    ui.query('body').classes('bg-amber-100')
    with ui.row().classes('items-center'):
        ui.image('img/logo_farol_na_quebrada-removebg.png').classes('w-24')
        ui.label("Bem-vindo ao Farol na Quebrada").classes("text-xl font-medium text-wrap text-stone-500")

ui.run(title="Minha primeira pagina web em python", language='pt-BR', favicon='img/logo_farol_na_quebrada.jpg')