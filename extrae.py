import os
import PyPDF2

def extract_text_between_keywords(pdf_path, output_path, start_keyword, end_keyword):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        first_page = reader.pages[0]
        text = first_page.extract_text()
    
    # Buscar el índice de inicio y fin de las palabras clave
    start_index = text.find(start_keyword)
    end_index = text.find(end_keyword)

    if start_index != -1 and end_index != -1:
        # Extraer el texto entre las palabras clave
        extracted_text = text[start_index + len(start_keyword):end_index]
        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write(extracted_text)

# Directorio que contiene los archivos PDF
pdf_directory = 'C:/Users/luis.murcia/OneDrive - Autonal SAS/Escritorio/extraer pdf/pdf'

# Directorio donde se guardarán los archivos de texto extraídos
output_directory = 'C:/Users/luis.murcia/OneDrive - Autonal SAS/Escritorio/extraer pdf/texto'

# Palabras clave
start_keyword = "DE LAS SIGUIENTES POLIZAS SOAT:"
end_keyword = "AGRADEZCO SEA GIRADO A LA MAYOR BREVEDAD PARA SER ENVIADO A LA"

# Iterar sobre todos los archivos PDF en el directorio
for filename in os.listdir(pdf_directory):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(pdf_directory, filename)
        output_filename = os.path.splitext(filename)[0] + '_extracto.txt'
        output_path = os.path.join(output_directory, output_filename)
        extract_text_between_keywords(pdf_path, output_path, start_keyword, end_keyword)
