from datetime import datetime
import hashlib
import hmac
import pickle
import logging
import time
import json
import os

now = datetime.now()

version = "F. 0.2.0v" #Version

logging.basicConfig(filename='_log_.txt', level=logging.DEBUG)
logging.debug(f"{version} Запущен. \n#После завершения работы всегда удаляйте лог во избежание переполнения повторов.\n")

class File:
  
  def check(filename):
    try:
      with open(f"{filename}", 'r'):
        
        pass
        return True
        
    except FileNotFoundError:
      
      return False
  
  def rename_file(filename, rename):
    if File.check(filename):
      os.rename(filename, rename)
      logging.info(f"Файл {filename} переименован..")
    else:
      logging.warning(f"Файл отсутствует, переименование невозможно!")
  
  def delete(filename):
    if File.check(filename):
      try:
        os.remove(filename)
        logging.info("Файл {} удалён в {}:{}:{} МСК.".format(filename, now.hour, now.minute, now.second))
      except Exception as e:
        logging.error(f"Ошибка при работе с файлом {filename} : {e}")
    else:
      logging.error(f"Файл {filename} не существует, удаление невозможно.")
      
  def size(filename):
    try:
      with open(f"{filename}", 'rb') as byte:
        byte.seek(0, 2)
        file_size = byte.tell()
        return file_size
    except FileNotFoundError:
      logging.error(f"Файл {filename} не существует, считывание невозможно.")
      
      return None 
      
    except Exception as e:
      logging.error(f"Ошибка при работе с файлом {filename} : {e}")
  
      return None 
  
  def size_converter(filename, file_size):
    if File.check(filename):
      for unit in ["B", "KB", "MB", "GB", "TB"]:
        if file_size < 1024.0:
          return f"{file_size:.2f}{unit}"
          
        file_size /= 1024.0
      return f"{file_size:.2f} PB"
    else:
      
      return "enable"
      
      logging.warning("size_converter() отказано. причина: отсутствие файла.")
  
  def timer(value):
    try:
      pass 
    except Exception as e:
      logging.error(f"timer() остановил свою работу, {e}")
      
      
  class Ordinary:
    
    def reader_len(filename):
      if File.check(filename):
        try:
          with open(f"{filename}", 'r') as file:
            for text_len in file:
              lens = len(text_len)
              return lens
        except Exception as e:
          logging.error(f"Ошибка при работе с файлом {filename} : {e}")
          
          return None 
          
      else:
        logging.error(f"Файл {filename} не существует, чтение невозможно.")
        
        return None 
    
    def writer(filename, write, encoding='utf-8'):
      try:
        with open(f"{filename}", 'w', encoding=f'{encoding}') as file:
          file.write(f"{write}")   
      except Exception as e:
        logging.error(f"Ошибка при работе с файлом {filename} : {e}")
      
    def reader(filename, value='', encoding='utf-8', end=''):
      if File.check(filename):
        try:
          with open(f"{filename}", 'r', encoding=f'{encoding}') as file:
            for text in file:
              print(f"{value}" + text, end=f'{end}')     
        except Exception as e:
          logging.error(f"Ошибка при работе с файлом {filename} : {e}")
      else:
        logging.error(f"Файл {filename} не существует, чтение невозможно.")
    
    def appendr(filename, write, encoding='utf-8', form='\n'):
      if File.check(filename):
        try:
          with open(f"{filename}", 'a', encoding=f'{encoding}') as file:
            file.write(f"{form}{write}")
        except Exception as e:
          logging.error(f"Ошибка при работе с файлом {filename} : {e}")
      else:
        logging.error(f"Файл {filename} не существует, дозапись невозможна.")   
      
  class Binary:
    
    def binary_writer(filename, data_write, mode='b'):
      try:
        with open(f"{filename}", 'wb') as binary_file:
          if mode == 'b':
            pickle.dump(data_write, binary_file)
      except Exception as e:
        logging.error(f"Ошибка при работе с файлом {filename} : {e}")    
        
    def binary_reader(filename):
      if File.check(filename):
        try:
          with open(f"{filename}", 'rb') as binary_file:
            reading = pickle.load(binary_file)
            return reading
        except Exception as e:
          logging.error(f"Ошибка при работе с файлом {filename} : {e}")
          
          return None
          
      else:
        logging.error(f"Бинарный файл {filename} не существует, чтение невозможно")
        
        return None
    
    def json_writer(filename, js_write):
      try:
        with open(f"{filename}", 'w') as file_js:
          json.dump(f"{js_write}", file_js, ensure_ascii=False, indent='4')
      except Exception as e:
        logging.error(f"Ошибка при работе с файлом {filename} : {e}")
    
    def json_reader(filename):
      if File.check(filename):
        try:
          with open(f"{filename}", 'r') as file_js:
            json_data = json.load(file_js)
            return json_data
        except Exception as e:
          logging.error(f"Ошибка при работе с файлом {filename} : {e}")
          
      else:
        logging.error(f"Бинарный файл {filename} не существует, чтение невозможно")
        
  
# Да, лучше вынести в отдельный конфиг либо в переменную окружения, но мне лень.
_HMAC_KEY = b"XoylY+ol_275I#tldol792_8ix*sy@c!"  # Минимум 32 байта

def __version__(version: str):
  
    """Проверяет и поддерживает целостность версии с HMAC подписью"""
    
    version_file = "version.txt"
    hmac_file = "version.hmac"
    
    # Если файла версии нет - создаем оба файла
    if not File.check(version_file):
        with open(version_file, 'w') as f:
            f.write(version)
            logging.info(f"{version_file.capitalize()} создан...\n")
        # Генерируем HMAC
        sig = hmac.new(_HMAC_KEY, version.encode(), hashlib.sha256).hexdigest()
        with open(hmac_file, 'w') as f:
            f.write(sig)
            logging.warning("HMAC подпись готова.\n")
        return
    
    # Читаем текущую версию
    with open(version_file, 'r') as f:
        current_version = f.read().strip()
    
    # Если файл HMAC отсутствует - пересоздаем оба файла
    if not File.check(hmac_file):
        os.remove(version_file)
        logging.warning("Перезапись файлов...\n")
        __version__(version)
        return
    
    # Проверяем подпись
    with open(hmac_file, 'r') as f:
        stored_hmac = f.read().strip()
        logging.info("Проверка подписи....\n")
    
    # Вычисляем текущий HMAC
    current_hmac = hmac.new(_HMAC_KEY, current_version.encode(), hashlib.sha256).hexdigest()
    
    # Если подпись не совпадает - перезаписываем
    if not hmac.compare_digest(current_hmac, stored_hmac):
        os.remove(version_file)
        os.remove(hmac_file)
        logging.critical("Нарушение подписи!")
        __version__(version)

# Инициализация версии
__version__(version)
                
