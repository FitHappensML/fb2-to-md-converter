# FB2 to TXT/MD Converter & Reader

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

This project is a Python-based utility for converting `.fb2` (FictionBook) files into `.txt` (plain text) or `.md` (Markdown). The tool offers two interfaces: a user-friendly web UI built with Streamlit for reading and converting, and a command-line interface (CLI) for fast processing and automation.

## ✨ Key Features

*   **Dual Interfaces**:
    *   🎨 **Web UI (Streamlit)**: Upload your files, read books directly in the browser, and download the result in your desired format.
    *   ⚙️ **Command-Line Interface (CLI)**: Quickly convert files from your terminal, perfect for scripting and batch processing.
*   **Smart Formatting**: An option to convert FB2 tags (like subtitles and emphasis) into corresponding Markdown syntax.
*   **Dual Export Formats**: Save your books as clean `.txt` or as formatted `.md` files.
*   **Built-in Reader**: The web interface provides a comfortable reading experience, rendering formatted text in real-time.
*   **Metadata Extraction**: Automatically extracts the book title and author's name and prepends them to the output file.

## 📸 Web Interface Screenshot

![Streamlit App Screenshot](./assets/screenshot_01.png)

## 🚀 Installation

This project requires Python 3.8 or newer.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/fb2_converter.git
    cd fb2_converter
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    # Create the environment
    python -m venv .venv

    # Activate on Windows
    .\.venv\Scripts\activate

    # Activate on macOS/Linux
    source .venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## 🛠️ Usage

You can use the utility via the web interface or the command line.

### 1. Web Interface (Streamlit)

This is the easiest way to read and convert individual files.

**To start the application:**
From the root project directory, run the following command:
```bash
streamlit run app.py
```
Your web browser should automatically open with the application.

**How to use it:**
1.  **Upload a file**: In the sidebar on the left, click "Browse files" and select a file (you can try the one in `examples/`).
2.  **Adjust the view**: Use the "Render with smart formatting" checkbox to control how the text is displayed in the reader.
3.  **Read**: The main area of the page will display the converted book text.
4.  **Download**: Download buttons for both `.txt` and `.md` formats will appear in the sidebar.

### 2. Command-Line Interface (CLI)

Ideal for quick conversions and integration into scripts. The examples below use the sample book included in the repository.

**Note:** Because the sample filename contains spaces, please enclose the path in quotes.

*   **Simple conversion to `.txt` (default format):**
    ```bash
    python cli.py "examples/The Adventures of Sherlock Holmes.fb2"
    ```
    *(This will create a .txt file in the examples folder.)*

*   **Conversion to Markdown (`.md`) with Smart Formatting:**
    ```bash
    python cli.py "examples/The Adventures of Sherlock Holmes.fb2" -f md
    ```
    *(This will create a .md file with headers and bold/italic styling.)*

*   **Conversion with a specific output filename:**
    ```bash
    python cli.py "examples/The Adventures of Sherlock Holmes.fb2" "sherlock.txt" -f txt
    ```
    *(This saves the result as `sherlock.txt` in the root folder.)*

*   **View all available options and help:**
    ```bash
    python cli.py -h
    ```

## 📂 Project Structure

```
fb2_converter/
├── assets/           # Images and screenshots
├── examples/         # Sample FB2 files for testing
├── converter.py      # Core: Contains the main conversion logic.
├── cli.py            # Code for the Command-Line Interface.
├── app.py            # Code for the Streamlit web application.
├── requirements.txt  # List of dependencies for pip.
└── README.md         # This file.
```

## 💡 Future Improvements (To-Do)

- [ ] Implement batch processing for the CLI (allow specifying a directory as input).
- [ ] Add support for more export formats (e.g., HTML).
- [ ] Handle more FB2 tags for richer formatting (e.g., quotes, poems).
- [ ] Deploy the Streamlit app to a service like Streamlit Cloud for public access.

## ⚖️ Legal Note regarding Examples

The sample file provided in the `examples/` directory (*The Adventures of Sherlock Holmes*) is in the **Public Domain**. You are free to use, modify, and distribute it without copyright restrictions.

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
