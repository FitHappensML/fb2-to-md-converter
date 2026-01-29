# converter.py

# Import necessary libraries
# BeautifulSoup is used for parsing the XML-like structure of FB2 files.
# Tag is used to check if an element is a tag, not just a string.
from bs4 import BeautifulSoup
from bs4.element import Tag

def _get_formatted_text(tag: Tag) -> str:
    """
    Recursively processes a tag to handle inline formatting like <emphasis>.
    This is used when smart_formatting is enabled.
    
    Args:
        tag (Tag): A BeautifulSoup Tag object.

    Returns:
        str: A string with inline formatting converted to Markdown.
    """
    parts = []
    # Iterate over all direct children of the tag
    for item in tag.children:
        if isinstance(item, Tag):
            # If the child is an <emphasis> tag, format it as italics
            if item.name == 'emphasis':
                parts.append(f'*{item.get_text(strip=True)}*')
            # For any other nested tags, recursively process them
            else:
                parts.append(_get_formatted_text(item))
        else:
            # If the item is just a string (NavigableString), append it directly
            parts.append(str(item))
    
    return "".join(parts)

def convert_fb2_to_txt(fb2_content: str, smart_formatting: bool = False) -> str:
    """
    Converts the content of an FB2 file to a plain text string.

    Args:
        fb2_content (str): The string content of the FB2 file.
        smart_formatting (bool): If True, applies Markdown-like formatting 
                                 for subtitles and emphasis.

    Returns:
        str: The extracted and formatted text content.
    """
    # Use 'lxml-xml' parser because FB2 is an XML format, not HTML.
    # This is more strict and correct for this file type.
    soup = BeautifulSoup(fb2_content, 'lxml-xml')

    # A list to hold all parts of the final text
    text_parts = []

    # --- 1. Extract Metadata ---
    # Find the <description> tag which contains book info.
    description = soup.find('description')
    if description:
        # Find book title
        title_tag = description.find('book-title')
        if title_tag:
            text_parts.append(f"Title: {title_tag.get_text(strip=True)}\n")

        # Find author info (can be composed of first-name, last-name, etc.)
        author_tag = description.find('author')
        if author_tag:
            first_name = author_tag.find('first-name')
            last_name = author_tag.find('last-name')
            author_str = ' '.join(filter(None, [
                first_name.get_text(strip=True) if first_name else '',
                last_name.get_text(strip=True) if last_name else ''
            ]))
            if author_str:
                text_parts.append(f"Author: {author_str.strip()}\n")
        
        # Add a separator after the metadata block
        if len(text_parts) > 0:
            text_parts.append("="*40 + "\n\n")

    # --- 2. Extract Main Body Content ---
    body = soup.find('body')
    if not body:
        # If there is no <body> tag, return what we have (metadata)
        return "".join(text_parts)

    # Find all relevant block-level tags in the order they appear.
    # This approach is simpler than recursion and works for most books.
    for element in body.find_all(['p', 'subtitle', 'empty-line']):
        
        if element.name == 'p':
            if smart_formatting:
                # Process paragraph with smart formatting for inline tags
                paragraph_text = _get_formatted_text(element).strip()
            else:
                # Just get the plain text
                paragraph_text = element.get_text(strip=True)
            
            if paragraph_text:
                text_parts.append(paragraph_text + '\n\n')

        elif element.name == 'subtitle':
            subtitle_text = element.get_text(strip=True)
            if subtitle_text:
                if smart_formatting:
                    # Format subtitle as a Markdown H3 header
                    text_parts.append(f"### {subtitle_text}\n\n")
                else:
                    text_parts.append(subtitle_text + '\n\n')
        
        elif element.name == 'empty-line':
            # Add an extra newline to create a visual break
            text_parts.append('\n')

    return "".join(text_parts)

# --- Main block for testing the script directly ---
if __name__ == '__main__':
    # Sample FB2 content from your example
    sample_fb2 = """
    <FictionBook>
        <description>
            <title-info>
                <book-title>Пример книги</book-title>
                <author>
                    <first-name>Иван</first-name>
                    <last-name>Иванов</last-name>
                </author>
            </title-info>
        </description>
        <body>
            <p>— Времена меняются, — вздохнул седой мужчина, сидевший в кресле напротив молодого человека.</p>
            <p>Парень, находившийся перед ним, был достаточно свеж, но, несмотря на молодость лица, имел уже ярко выраженную седину в волосах.</p>
            <subtitle>* * *</subtitle>
            <p>А также на парте появилась ещё одна небольшая надпись, которую он не сразу заметил.</p>
            <p><emphasis>«Ты молодец!»</emphasis></p>
            <empty-line/>
            <p>Конец первой книги.</p>
        </body>
    </FictionBook>
    """

    print("--- Running Test with smart_formatting=False ---")
    result_plain = convert_fb2_to_txt(sample_fb2, smart_formatting=False)
    print(result_plain)

    print("\n" + "-"*50 + "\n")

    print("--- Running Test with smart_formatting=True ---")
    result_smart = convert_fb2_to_txt(sample_fb2, smart_formatting=True)
    print(result_smart)