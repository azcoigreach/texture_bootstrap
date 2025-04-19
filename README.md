# Bootstrap Textual App

## Overview
This is a bootstrap application built using the [Textual](https://github.com/Textualize/textual) framework. It serves as a robust starting platform for creating terminal-based user interfaces and new projects.

## Features
- **Multiple Screens:**
  - **Help Screen:** Displays instructions on how to return to the main screen with key binding (`h`).
  - **Settings Screen:** Offers configurable input fields to adjust settings (press `b` to go back).
  - **Demo Modal:** A modal dialog that can be closed with keyboard shortcuts (`m` or `Esc`).

- **Tabbed Interface:** Organized using TabbedContent into several tabs:
  - **Controls:** Demonstrates interactive controls (buttons, checkboxes, radio buttons, switches, and more).
  - **Forms:** Provides text input, masked inputs, multiline text area, and a submit button.
  - **Data:** Features a data table and a directory tree for data visualization.
  - **Display:** Renders markdown content, pretty printed dictionaries, and static display elements.
  - **Misc:** Includes indicators like loading spinners and progress bars.
  - **Advanced:** Offers advanced features such as logs, tooltips, nested tabs, and content switching.

- **Reactive Updates:** The app displays the current time which updates every second using reactive properties.

- **Keyboard Shortcuts:**
  - `q`: Quit the app
  - `h`: Show Help screen
  - `s`: Show Settings screen
  - `m`: Show Modal dialog

## Usage

### Requirements
 - Python 3.9 or later
 - Textual library (install via `pip install textual`)

### Running the Application

Run the following command in your terminal:
```
python main.py
```

### Navigating the UI

Use the provided keyboard shortcuts or interact with the UI using your mouse/keyboard as indicated by the on-screen prompts.

## Testing

A basic testing mechanism is built into this project to facilitate debugging and ensure that core functionality works as expected.

### How to Run Tests

1. Install `pytest` if you haven't already:
   ```
   pip install pytest
   ```

2. Run the tests with the following command:
   ```
   pytest
   ```

Tests are located in the `tests/` directory and include smoke tests for UI composition and reactive updates.

## Development Notes

This project is designed as a robust, AI-developed starting template. It includes extensive inline comments throughout the codebase to provide context and assist with future development.

Feel free to extend the features and testing mechanisms as needed for your projects.