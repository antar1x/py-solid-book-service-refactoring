import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content


# --- Display ---
class IBookDisplay(ABC):
    @abstractmethod
    def display(self, book: Book) -> None: ...

class ConsoleDisplay(IBookDisplay):
    def display(self, book: Book) -> None:
        print(book.content)

class ReverseDisplay(IBookDisplay):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


# --- Print ---
class IBookPrinter(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None: ...

class ConsolePrinter(IBookPrinter):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)

class ReversePrinter(IBookPrinter):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


# --- Serialize ---
class IBookSerializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str: ...

class JsonSerializer(IBookSerializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})

class XmlSerializer(IBookSerializer):
    def serialize(self, book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")

    ReverseDisplay().display(sample_book)
    print(XmlSerializer().serialize(sample_book))
