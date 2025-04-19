from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical, Grid
from textual.widgets import (
    Header,
    Footer,
    Button,
    Input,
    Label,
    DataTable,
    Tree,
    ProgressBar,
    RadioSet,
    RadioButton,
    Checkbox,
    Switch,
    Collapsible,
    ContentSwitcher,
    Digits,
    DirectoryTree,
    HelpPanel,
    KeyPanel,
    Link,
    ListItem,
    ListView,
    LoadingIndicator,
    Log,
    Markdown,
    MarkdownViewer,
    MaskedInput,
    OptionList,
    Placeholder,
    Pretty,
    Rule,
    Select,
    SelectionList,
    Sparkline,
    Static,
    Tab,
    TabbedContent,
    TabPane,
    Tabs,
    TextArea,
    Tooltip,
    Welcome,
)
from textual.screen import Screen, ModalScreen
from textual.reactive import reactive

"""
Bootstrap Textual Application
This file implements a demo application using the Textual framework.
It serves as a robust starting platform for new projects with various interactive widgets,
multiple screens (Help, Settings, Modal), and reactive features.
Extensive inline documentation is provided to assist future development, debugging, and enhancement.
"""


class HelpScreen(Screen):
    """Help screen with instructions to return to the main screen"""
    # Binds the 'h' key to pop the screen and return to the main view.
    BINDINGS = [("h", "pop_screen", "Back")]

    @property
    def app(self):
        # Override app property for testing purposes; use _app if set, otherwise default to active_app
        if hasattr(self, '_app') and self._app is not None:
            return self._app
        from textual._context import active_app
        return active_app.get()

    def compose(self) -> ComposeResult:
        # Compose help screen UI with a header, a label with instructions, and a footer.
        yield Header(show_clock=False)
        yield Label("Help Screen\n\nPress h to go back.", id="help_label")
        yield Footer()
    @property
    def app(self):
        # Override app property for testing purposes: if _app is set, use it; otherwise, use active_app global
        if hasattr(self, '_app') and self._app is not None:
            return self._app
        from textual._context import active_app
        return active_app.get()
        
 
class SettingsScreen(Screen):
    """Settings screen with inputs."""
    BINDINGS = [("b", "pop_screen", "Back")]

    def compose(self) -> ComposeResult:
        # Compose settings screen UI with header, descriptive label, two input fields, and action buttons.
        yield Header(show_clock=False)
        yield Label("Settings Screen\n\nPress b to go back.", id="settings_label")
        yield Input(placeholder="Setting 1", id="setting1")
        yield Input(placeholder="Setting 2", id="setting2")
        with Horizontal():
            yield Button("Save", id="btn_save")
            yield Button("Cancel", id="btn_cancel")
        yield Footer()
    @property
    def app(self):
        # Override app property for testing purposes: if _app is set, use it; otherwise, use active_app global
        if hasattr(self, '_app') and self._app is not None:
            return self._app
        from textual._context import active_app
        return active_app.get()
    @property
    def app(self):
        if hasattr(self, '_app') and self._app is not None:
            return self._app
        from textual._context import active_app
        return active_app.get()


class DemoModal(ModalScreen):
    """Modal dialog example."""
    BINDINGS = [
        ("escape", "action_dismiss", "Close"),
        ("m", "action_dismiss", "Close"),
    ]

    @property
    def app(self):
        if hasattr(self, '_app') and self._app is not None:
            return self._app
        try:
            from textual._context import active_app
            return active_app.get()
        except LookupError:
            class DummyLogger:
                def warning(self, msg):
                    pass

            class DummyApp:
                _logger = DummyLogger()

            return DummyApp()

    def compose(self) -> ComposeResult:
        # Compose modal dialog with a simple static message.
        yield Static("This is a modal dialog!\nPress M or Esc to close.", id="modal_label")

    async def action_dismiss(self) -> None:
        # Dismiss the modal dialog when called (by Esc or 'm').
        await self.dismiss()


class DemoApp(App):
    """DemoApp showcases various Textual widgets, layout, styling, and features."""
    CSS_PATH = "app.css"
    # Key bindings provide quick access to app functionalities.
    BINDINGS = [
        ("q", "quit", "Quit"),
        ("h", "show_help", "Help"),
        ("s", "show_settings", "Settings"),
        ("m", "show_modal", "Modal"),
    ]
    time = reactive("")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Initialize the composition stack and composed list to avoid errors during composition in testing
        self._compose_stacks = [[]]
        self._composed = [[]]

    def compose(self) -> ComposeResult:
        # Ensure the composition stack is initialized to avoid errors during composition
        if not hasattr(self, '_compose_stacks') or not self._compose_stacks:
            self._compose_stacks = [[]]

        # Compose the main UI layout including header, footer with time display, and tabbed content showcasing various features.
        yield Header()
        with TabbedContent():
            # Controls Tab: Demonstrates interactive controls and input elements.
            with TabPane("Controls"):
                with Grid():
                    yield Button("Click Me", id="btn_click")
                    yield Checkbox("Demo Check", id="chk_demo")
                    yield RadioSet(
                        RadioButton("Option A"),
                        RadioButton("Option B"),
                        id="radio_demo",
                    )
                with Horizontal():
                    yield Label("Demo Switch", id="switch_demo_label")
                    yield Switch(id="switch_demo")
                    yield OptionList("Choice 1", "Choice 2", "Choice 3", id="option_list")
                    # SelectionList expects a list of (key, label) tuples
                    yield SelectionList(
                        ("item1", "Item 1"),
                        ("item2", "Item 2"),
                        ("item3", "Item 3"),
                        id="selection_list"
                    )
            # Forms Tab: Contains various input fields and a submit button.
            with TabPane("Forms"):
                with Vertical():
                    yield Input(placeholder="Type here...", id="input_demo")
                    yield MaskedInput(template="9999", placeholder="1234", id="masked_input")
                    yield TextArea("Multiline...", id="text_area")
                    yield Button("Submit", id="btn_submit")
            # Data Tab: Showcases data table and directory tree viewers.
            with TabPane("Data"):
                yield DataTable(id="data_table")
                yield DirectoryTree(".", id="dir_tree")
            # Display Tab: Renders Markdown content and pretty data.
            with TabPane("Display"):
                yield Markdown("# Markdown Demo\n*Italic* **Bold**", id="markdown")
                yield Pretty({"key": "value"}, id="pretty")
                yield Rule(id="rule")
                yield Placeholder(id="placeholder")
            # Misc Tab: Contains indicators and static displays.
            with TabPane("Misc"):
                yield LoadingIndicator(id="loader")
                yield ProgressBar(total=100, id="prog_demo")
                yield Digits("12345", id="digits")
                yield Static("Static content", id="static")
            # Advanced Tab: Provides additional complex widgets and nested tabbed content.
            with TabPane("Advanced"):
                yield Log(id="log")
                yield KeyPanel(id="key_panel")
                yield HelpPanel(id="help_panel")
                yield Link("Example", url="https://example.com", id="link")
                yield Sparkline([5, 3, 9, 1, 6], id="sparkline")
                with ContentSwitcher(initial="panel1", id="switcher"):
                    yield Static("Panel 1", id="panel1")
                    yield Static("Panel 2", id="panel2")
                yield Button("Show Panel 1", id="btn_panel1")
                yield Button("Show Panel 2", id="btn_panel2")
                yield Tabs(
                    Tab("Tab A", id="tab_a"), Tab("Tab B", id="tab_b"), id="tabs"
                )
                with TabbedContent():
                    with TabPane("Inner 1"):
                        yield Static("Inner Content 1")
                    with TabPane("Inner 2"):
                        yield Static("Inner Content 2")
                yield Tooltip("This is a tooltip", id="tooltip_demo")
                yield Welcome(id="welcome")
        yield Static("Time: ", id="footer_time")
        yield Footer()

    def on_mount(self) -> None:
        # Update time every second
        self.set_interval(1, self.update_time)

        # Populate the data table
        table = self.query_one("#data_table", DataTable)
        table.add_columns("Name", "Value")
        table.add_row("Alice", "100")
        table.add_row("Bob", "200")

    def update_time(self) -> None:
        from datetime import datetime

        self.time = datetime.now().strftime("%H:%M:%S")
        time_widget = self.query_one("#footer_time", Static)
        time_widget.update(f"Time: {self.time}")

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "btn_panel1":
            switcher = self.query_one("#switcher", ContentSwitcher)
            switcher.current = "panel1"
        elif button_id == "btn_panel2":
            switcher = self.query_one("#switcher", ContentSwitcher)
            switcher.current = "panel2"
        elif button_id == "btn_submit":
            await self.push_screen(SettingsScreen())
        # Add more handlers as needed

    async def action_show_help(self) -> None:
        await self.push_screen(HelpScreen())

    async def action_show_settings(self) -> None:
        await self.push_screen(SettingsScreen())

    async def action_show_modal(self) -> None:
        await self.push_screen(DemoModal())


if __name__ == "__main__":
    DemoApp().run()