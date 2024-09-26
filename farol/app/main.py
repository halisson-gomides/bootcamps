from nicegui import ui, app

app.add_static_files(url_path="/img", local_directory="img")
ui.markdown.default_classes('text-lg')
@ui.page('/')
def principal()->None:
    with open('README.md', 'r', encoding='utf-8') as f:
        mk = f.read()

    ui.markdown(mk, extras=['tables'])

ui.run()