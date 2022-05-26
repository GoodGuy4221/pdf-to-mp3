from gtts import gTTS
import pdfplumber
from pathlib import Path
from art import tprint


def pdf_to_mp3(file_path='test.pdf', language='ru'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        print(f'Файл pdf найден: {Path(file_path).name}')
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            print(f'Начинаю конвертировать')
            pages = [page.extract_text() for page in pdf.pages]
            text = ''.join(pages)
            text = text.replace('\n', '')
            audio = gTTS(text=text, lang=language)
            file_name = Path(file_path).stem
            audio.save(f'{file_name}.mp3')
            return f'Файл {file_name}.mp3 сохранен, наслаждайтесь прослушиванием!'
    return 'Файл не найден, проверьте путь!'


def main():
    tprint('PDF TO MP3')
    file_path = input('Введите путь до файла PDF\n')
    lang = input('Введите язык в формате: en, ru\n')
    if lang in ('en', 'ru'):
        print(pdf_to_mp3(file_path=file_path, language=lang))
    else:
        print(pdf_to_mp3(file_path=file_path))


if __name__ == '__main__':
    main()
