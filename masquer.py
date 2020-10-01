from IPython.display import HTML 
import random

def cacher_code(text = "Montrer/Cacher le code",for_next=True,output=False,for_markdown=False):
    this_cell = """$('div.cell.code_cell.rendered.selected')"""
    next_cell = this_cell + '.next()'
    toggle_text = text  # text shown on toggle link
    target_cell = this_cell  # target cell to control with toggle
    js_hide_current = ''  # bit of JS to permanently hide code in current cell (only when toggling next cell)

    if for_next:
        target_cell = next_cell
        toggle_text += ' '#next cell
        js_hide_current = this_cell + '.find("div.input").hide();'

    js_f_name = 'code_toggle_{}'.format(str(random.randint(1,2**64)))

    if output:
        html = """
    <script>
        function {f_name}() {{
            {cell_selector}.find('div.input').toggle();
            {cell_selector}.find('div.output').toggle();
        }}

        {js_hide_current}
    </script>

    <a href="javascript:{f_name}()">{toggle_text}</a>
    """.format(
    f_name=js_f_name,
    cell_selector=target_cell,
    js_hide_current=js_hide_current, 
    toggle_text=toggle_text
    )
    elif for_markdown:
        html = """
    <script>
        function {f_name}() {{
            {cell_selector}.find('div.inner_cell').toggle();
        }}

        {js_hide_current}
    </script>

    <a href="javascript:{f_name}()">{toggle_text}</a>
    """.format(
    f_name=js_f_name,
    cell_selector=target_cell,
    js_hide_current=js_hide_current, 
    toggle_text=toggle_text
    )
    else:
        html = """
    <script>
        function {f_name}() {{
            {cell_selector}.find('div.input').toggle();
        }}

        {js_hide_current}
    </script>

    <a href="javascript:{f_name}()">{toggle_text}</a>
    """.format(
    f_name=js_f_name,
    cell_selector=target_cell,
    js_hide_current=js_hide_current, 
    toggle_text=toggle_text
    )

    return HTML(html)