from nicegui import ui

def render_menu():
    ui.query('body').classes('bg-amber-100')
    with ui.header().classes(replace='row items-center').classes('bg-transparent') as header:
        ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=dark')
        ui.image('img/logo_farol_na_quebrada-removebg.png').classes('w-24')
        ui.label("Farol na Quebrada").classes("text-xl font-medium text-wrap text-stone-500")
    
    with ui.left_drawer(value=False).classes('bg-orange-500') as left_drawer:
        ui.button('Quem Somos', color='dark', on_click=lambda: ui.navigate.to('/quem')).classes('w-full').props('outline')
        ui.button('Junte-se a nós', color='dark', on_click=lambda: ui.navigate.to('/juntese')).classes('w-full').props('outline')

@ui.page('/')
def principal()->None:
    render_menu()    

    # with ui.footer() as footer:
    with ui.footer(value=False).classes('bg-dark') as footer:
        with ui.splitter().classes('w-1/3') as splitter:
            with splitter.before:
                ui.label('© Todos os direitos reservados.')
            with splitter.after:
                ui.link("Contato", 'mailto:farol@naquebrada.com.br').classes('text-white px-3')

    with ui.page_sticky(position='bottom-right', x_offset=20, y_offset=20):
        ui.button(on_click=footer.toggle, icon='contact_support', color='dark').props('fab')

    ui.label('Bem-vindo à página principal.')

@ui.page('/quem')
def quem_somos()->None:
    render_menu()  
    ui.label("Quem Somos").classes("text-xl font-medium text-wrap text-stone-500 py-3")
    ui.label("Somos uma ONG muito legal!")
    ui.link("Voltar", "/")

@ui.page('/juntese')
def junte_se()->None:
    render_menu()  
    ui.label("Junte-se a nós").classes("text-xl font-medium text-wrap text-stone-500 py-3")
    with ui.card().classes('w-5/6'):
        ui.label("Preencha o formulário abaixo para entrarmos em contato.")
        ui.input('Nome', placeholder='Entre com seu nome...').classes('w-1/2')
        ui.input('E-mail', placeholder='Entre com seu e-mail...').classes('w-1/3')
        (ui.input('WhatsApp', placeholder='Entre com seu telefone...')
         .props('mask="(##)#####-####"')
         .classes('w-1/3'))
    with ui.row():
        ui.button("Enviar", color='green', on_click=lambda: ui.navigate.to('/'))
        ui.button("Voltar", color='grey', on_click=lambda: ui.navigate.to('/'))

ui.run(title="Minha primeira pagina web em python", language='pt-BR', favicon='img/logo_farol_na_quebrada.jpg')