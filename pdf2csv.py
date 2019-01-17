import io,os,csv,re
 
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
 
def extract_text_by_page(pdf_path):
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh, 
                                      caching=True,
                                      check_extractable=True):
            resource_manager = PDFResourceManager()
            fake_file_handle = io.BytesIO()
            converter = TextConverter(resource_manager, fake_file_handle)
            page_interpreter = PDFPageInterpreter(resource_manager, converter)
            page_interpreter.process_page(page)
 
            text = fake_file_handle.getvalue()
            yield text
 
            # close open handles
            converter.close()
            fake_file_handle.close()
def extract_text_from_pdf(pdf_path):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
 
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh, 
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)
 
        text = fake_file_handle.getvalue()
 
    # close open handles
    converter.close()
    fake_file_handle.close()
 
    if text:
        return text
 
def extract_text(pdf_path):
    for page in extract_text_by_page(pdf_path):
        print(page)
        print()
def export_as_csv(pdf_path, csv_path):
    filename = os.path.splitext(os.path.basename(pdf_path))[0]
    bldno,bldown,bldnme = [],[],[]
    counter = 1
    with open(csv_path, 'w') as csv_file:
        writer = csv.writer(csv_file)
        for page in extract_text_by_page(pdf_path):
            text = page
            print text
            key1,key2,key3,key4,key5,key6 = 'FACNO/LD','RPA Name','Interest Type','Placed in','RPA Description','Design FAC'
            facno = [m.start() for m in re.finditer(key1,text)]
            rpa = [m.start() for m in re.finditer(key2,text)]
            inttype = [m.start() for m in re.finditer(key3,text)]
            placed = [m.start() for m in re.finditer(key4,text)]
            rpadesc = [m.start() for m in re.finditer(key5,text)]
            desfac = [m.start() for m in re.finditer(key6,text)]
            for el1,el2 in zip(facno,rpa):
                bldno.append(text[el1+len(key1):el2])
            for el1,el2 in zip(inttype,placed):
                bldown.append(text[el1+len(key3):el2])
            for el1,el2 in zip(rpadesc,desfac):
                bldnme.append(text[el1+len(key5):el2])
            writer.writerow([bldno,bldown,bldnme])
 

if __name__ == '__main__':
    pdf_path = 'AZ_FISP_2018_11_16_building_data_FMO.pdf'
    csv_path = 'AZ_FISP_2018_11_16_building_data_FMO.csv'
    export_as_csv(pdf_path, csv_path)