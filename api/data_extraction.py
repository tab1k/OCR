import re
from datetime import datetime



def extract_full_name(text):
    # Ищем строку "первого официального опубликования)" и извлекаем следующие три слова
    match = re.search(r'первого официального опубликования\)\.\s*([^\n]+)', text)
    if match:
        next_words = match.group(1)
        print("Следующие слова после 'первого официального опубликования)':", next_words)  # Отладочный вывод
        # Теперь извлекаем первые три слова из строки, используя простое разделение по пробелам
        words = next_words.split()
        full_name = ' '.join(words[:3])  # Берем первые три слова
        print("Извлечено полное имя:", full_name)  # Отладочный вывод
        return full_name
    else:
        return None

def extract_position(text):
    # Ищем ключевое слово или фразу, указывающую на должность
    match = re.search(r'акционерного общества "Фонд гарантирования страховых выплат"\s*([^\n]+)', text)
    if match:
        position_text = match.group(1)
        print("Извлеченная должность:", position_text)  # Отладочный вывод
        return position_text.strip()  # Удаляем лишние пробелы в начале и конце текста
    else:
        return None


def extract_birth_info(text):
    # Ищем строку, содержащую информацию о дате и месте рождения
    match = re.search(r'(Дата и место рождения|Дата рождения)\s*([^\n]+)\n', text)
    if match:
        birth_info = match.group(2).strip()
        return birth_info
    else:
        return None


def extract_citizenship(text):
    # Ищем строку, содержащую информацию о гражданстве
    match = re.search(r'Гражданство\s*([^\n]+)\n', text)
    if match:
        citizenship_info = match.group(1).strip()
        return citizenship_info
    else:
        return None


def extract_passport_number(text):
    match = re.search(r'Паспорт №\s*([^\n,]+)', text)
    if match:
        return match.group(1).strip()
    else:
        return None


def extract_passport_issue_date(text):
    match = re.search(r'выдан\s*(\d{2}\.\d{2}\.\d{4})', text)
    if match:
        date_str = match.group(1).strip()
        # Преобразовываем строку с датой в формат YYYY-MM-DD
        date_obj = datetime.strptime(date_str, "%d.%m.%Y")
        formatted_date = date_obj.strftime("%Y-%m-%d")
        return formatted_date
    else:
        return None

def extract_issuing_authority(text):
    match = re.search(r',\s*([^,]+),\s*ИИН', text)
    if match:
        return match.group(1).strip()
    else:
        return None

def extract_iin(text):
    match = re.search(r'ИИН\s*([^\n]+)', text)
    if match:
        return match.group(1).strip()
    else:
        return None


def extract_insurance_company_name(text):
    match = re.search(r'\(для услугополучателя –\s*юридического\s*лица\)\s*"([^"]+)"', text)
    if match:
        return match.group(1).strip()
    else:
        return None

# Образование

def extract_education_institution(text):
    match = re.search(r'\s\d\s+\d\s+\d\s+\d\s+\d\s+([\s\S]+?)\s+\d{4}\s*-\s*\d{4}\s+[\s\S]+?\s+(?:№\s*\d+)?', text)
    if match:
        return match.group(1).strip()
    else:
        return None







def extract_education_period(text):
    match = re.search(r'\d{4}-\d{4}', text)
    if match:
        return match.group().strip()
    else:
        return None

def extract_education_specialty(text):
    match = re.search(r'(?<=Специальность: ).*', text)
    if match:
        return match.group().strip()
    else:
        return None

def extract_diploma_details(text):
    match = re.search(r'№\s+\d+\s+от\s+\d{4}', text)
    if match:
        return match.group().strip()
    else:
        return None












