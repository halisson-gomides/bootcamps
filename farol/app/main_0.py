from nicegui import ui


@ui.page('/')
def principal()->None:
    ui.label("Hello Word")
    ui.query('body').classes('bg-amber-100')

ui.run(title="Minha primeira pagina web em python", language='pt-BR', favicon='img/logo_farol_na_quebrada.jpg')