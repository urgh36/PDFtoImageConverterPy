from PyPDF2 import PdfFileReader
from PIL import Image

# Функция для конвертации PDF в текстовый файл
def pdf_to_text(pdf_file, text_file):
    with open(pdf_file, "rb") as input_file:
        pdf = PdfFileReader(input_file)
        text = ""
        for page_num in range(pdf.getNumPages()):
            page = pdf.getPage(page_num)
            text += page.extract_text()
    
    with open(text_file, "w", encoding="utf-8") as output_file:
        output_file.write(text)

# Функция для конвертации изображения в PDF
def image_to_pdf(image_file, pdf_file):
    img = Image.open(image_file)
    img.save(pdf_file, "PDF", resolution=100.0)

if __name__ == "__main__":
    # Конвертация PDF в текстовый файл
    pdf_to_text("input.pdf", "output.txt")
    print("PDF успешно сконвертирован в текстовый файл.")

    # Конвертация изображения в PDF
    image_to_pdf("input.jpg", "output.pdf")
    print("Изображение успешно сконвертировано в PDF.")
