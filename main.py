import re


def decrypt_unicode_rtf(rtf_string):
    
    unicode_matches = re.findall(r'\\uc\d+\\u(\d+)', rtf_string)
    

    clean_text = re.sub(r'\\uc\d+\\u\d+', '', rtf_string)
    clean_text = re.sub(r'\\[^ ]+', '', clean_text)  
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()  
    

    decoded_text = ""
    if unicode_matches:
        for code in unicode_matches:
            try:
                
                decoded_text += chr(int(code))
            except ValueError:
                decoded_text += f"[Ошибка: неверный код {code}]"
    
   
    if decoded_text:
        result = f"Оригинальная строка: '{rtf_string}' | Расшифрованный текст: '{decoded_text}'"
    else:
        result = f"Оригинальная строка: '{rtf_string}' | Расшифрованный текст: '{clean_text}' (Unicode отсутствует)"
    
    return result


print("Введите строку в формате RTF с Unicode ):")
input_string = input("> ")


decrypted_result = decrypt_unicode_rtf(input_string)
print(decrypted_result)


output_path = r"PATH TO OUTPUT"
rtf_header = r'{\rtf1\ansi\ansicpg1251\deff0{\fonttbl{\f0\fnil\fcharset0 Calibri;}}' + '\n'
rtf_footer = r'}'
output_content = rtf_header
output_content += r'\pard\sa200\sl276\slmult1\b\f0\fs24 Расшифровка введенной строки\par' + '\n'
output_content += r'\pard\sa200\sl276\slmult1\f0\fs22 '
output_content += f"{decrypted_result.replace('{', r'\{').replace('}', r'\}')}\par" + '\n'
output_content += rtf_footer

try:
    with open(output_path, 'w', encoding='ansi') as file:
        file.write(output_content)
    print(f"Результат сохранен в {output_path}")
except Exception as e:
    print(f"Ошибка при сохранении файла: {e}")
