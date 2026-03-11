
import pypdf
import json

def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as f:
            reader = pypdf.PdfReader(f)
            text_data = []
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text_data.append({
                    'page': page_num + 1,
                    'text': page.extract_text()
                })
        return json.dumps(text_data, indent=2)
    except Exception as e:
        return json.dumps({'error': str(e)})

if __name__ == '__main__':
    pdf_path = 'c:\\Users\\Admin\\Desktop\\f1-strategy-dashboard-cursor\\F1 2026 Chinese GP Deep Dive.pdf'
    extracted_text = extract_text_from_pdf(pdf_path)
    print(extracted_text)
